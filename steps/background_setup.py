# pylint: disable=too-many-locals,no-member
# pylint: disable=too-many-branches,too-many-statements
# pylint: disable=invalid-name
# pylint: disable=no-name-in-module
""" Steps to use in the background set up of the features """
from uuid import uuid4
from behave import given

from liveobs_ui.page_object_models.common.background_setup import \
    get_or_create_user, assign_user_roles, get_user_record, \
    create_locations_if_necessary


@given('the user {name} exists')
def ensure_user_record_exists(context, name):
    """
    Checks if user record is in the system, otherwise it creates it

    :param context: behave context
    :param name: name of the user to search for
    """
    user_model = context.client
    get_or_create_user(user_model, name)


@given('user {name} has the role of {role}')
def ensure_user_has_role(context, name, role):
    """
    Checks if user has role assigned, otherwise assigns it

    :param context: behave context
    :param name: name of the user to check
    :param role: role to verify/assign
    """
    user_model = context.client
    assign_user_roles(user_model, name, role)


@given('the user {name} is in the current Shift for {ward}')
def add_user_to_shift(context, name, ward):
    create_locations_if_necessary(context, parent_location_name=ward)
    shift_model = context.client.model('nh.clinical.shift')
    if not hasattr(context, 'shift'):
        context.shift = shift_model.create({'ward': context.ward.id})

    values = {}
    user = get_user_record(context.client, name)
    if 'Nurse' in name:
        values['nurses'] = [(4, user.id)]
    elif 'HCA' in name:
        values['hcas'] = [(4, user.id)]

    shift_model.write(context.shift.id, values)


@given("the patient {patient_name} is in {location} of {parent_location}")
def ensure_patient_in_system(context, patient_name, location, parent_location):
    """
    Make sure there's a patient in the system in the location specified

    :param context: Behave context
    :param patient_name: Name of the patient
    :param location: Location for the patient to be in
    :param parent_location: Parent of the location the patient should be in
    """
    create_locations_if_necessary(context, location, parent_location)
    # search for patient
    names = patient_name.split(' ')
    patient_model = context.client.model('nh.clinical.patient')
    patient_search = patient_model.search(
        [
            ['given_name', '=', names[0]],
            ['family_name', '=', names[1]]
        ]
    )
    # if patient not found then create them
    api_model = context.client.model('nh.eobs.api')
    if not patient_search:
        hospital_number = str(uuid4().int)[:8]
        patient_search = api_model.register(
            hospital_number,
            {
                'given_name': names[0],
                'family_name': names[1],
            }
        )
    else:
        patient_search = patient_search[0]
        hospital_number = patient_model.read(
            patient_search, ['other_identifier']).get('other_identifier')
    # search for spell for patient
    spell_model = context.client.model('nh.clinical.spell')
    spell_search = spell_model.search(
        [
            ['state', 'not in', ['completed', 'cancelled']],
            ['patient_id', '=', patient_search]
        ]
    )
    # if spell not found then create it
    if not spell_search:
        # Add pos to admin user
        user_model = context.client.model('res.users')
        user_model.write(1, {'pos_id': 1, 'pos_ids': [[6, 0, [1]]]})
        api_model.admit(
            hospital_number,
            {
                'location': context.ward.code,
            }
        )
    # check patient isn't in location then place them there
    patients_location = patient_model.read(
        patient_search, ['current_location_id']).get('current_location_id')
    # if patient isn't in either location send to parent location
    if patients_location[0] not in [context.ward.id, context.bed_id]:
        api_model.transfer(hospital_number, {'location': context.ward.code})
        patients_location = patient_model.read(
            patient_search, ['current_location_id']).get('current_location_id')
    # if current location is ward then place
    if patients_location[0] == context.ward.id:
        placement_model = context.client.model('nh.clinical.patient.placement')
        activity_model = context.client.model('nh.activity')
        placement_model.create_activity({}, {
            'suggested_location_id': context.bed_id,
            'patient_id': patient_search
        })
        placement_activity = activity_model.search([
            ['data_model', '=', 'nh.clinical.patient.placement'],
            ['patient_id', '=', patient_search],
            ['state', 'not in', ['completed', 'cancelled']]
        ])
        if not placement_activity:
            raise Exception("placement not found")
        else:
            placement_activity = placement_activity[0]
        activity_model.submit(
            placement_activity, {'location_id': context.bed_id})
        activity_model.complete(placement_activity)
    context.patient = patient_name


@given('the user {user_name} is allocated to {location} of {parent_location}')
def ensure_user_allocated_to_location(
        context, user_name, location, parent_location):
    """
    Make sure that the user allocated to the supplied location.

    :param context: Behave context
    :param user_name: Name of the user to find and allocate
    :param location: name of the location to allocate user to
    :param parent_location: Parent of the location to allocate to
    """
    user_model = context.client.model('res.users')
    location_model = context.client.model('nh.clinical.location')
    user_search = user_model.search(
        [
            ['name', '=', user_name]
        ]
    )
    if not user_search:
        raise Exception("User not in system")
    else:
        user_search = user_search[0]
    parent_location_search = location_model.search(
        [
            ['name', '=', parent_location]
        ]
    )
    if not parent_location_search:
        raise Exception("Parent location not found in system")
    else:
        parent_location_search = parent_location_search[0]
    location_search = location_model.search(
        [
            ['name', '=', location],
            ['parent_id', '=', parent_location_search]
        ]
    )
    if not location_search:
        raise Exception("Location not in system")
    else:
        location_search = location_search[0]
    user_locations = \
        user_model.read(user_search, ['location_ids']).get('location_ids')
    if location_search not in user_locations:
        user_locations.append(location_search)
        user_model.write(user_search, {
            'location_ids': [[6, 0, user_locations]]
        })
