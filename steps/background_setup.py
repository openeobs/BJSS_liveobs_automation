""" Steps to use in the background set up of the features """
from behave import given
from uuid import uuid4


@given('the user {user_name} exists with the {user_role} role')
def ensure_user_with_role(context, user_name, user_role):
    """
    Do a search for user with the specified role or create one

    :param context: Behave context
    :param user_name: Name for the user
    :param user_role: Role for the user
    """
    user_model = context.client.model('res.users')
    group_model = context.client.model('res.groups')
    group_search = group_model.search(
        [
            ['name', '=', 'NH Clinical {} Group'.format(user_role)]
        ]
    )
    if not group_search:
        raise Exception("No group {} found".format(user_role))
    user_search = user_model.search(
        [
            ['name', '=', user_name]
        ]
    )
    if user_search:
        found_user = user_model.read(user_search[0], ['login', 'groups_id'])
        if not group_search[0] in found_user.get('groups_id'):
            user_model.write(found_user.get('id'), {
                'groups_id': [
                    [6, 0, found_user.get('groups_id') + group_search]
                ]
            })
        context.helpers.user = found_user.get('login')
    else:
        category_model = context.client.model('res.partner.category')
        location_model = context.client.model('nh.clinical.location')
        category_search = category_model.search(
            [
                ['name', '=', user_role]
            ]
        )
        if category_search:
            category_search = category_search[0]
        else:
            raise Exception("No category {} found".format(user_role))
        location_search = location_model.search(
            [
                ['usage', '=', 'hospital']
            ]
        )
        pos_id = []
        if location_search:
            location = location_model.read(location_search[0], ['pos_id'])
            if location.get('pos_id'):
                pos_id.append(location['pos_id'][0])
        else:
            raise Exception("No hospital in system")
        user_login = user_name.lower().replace(' ', '_').strip()
        user_model.create(
            {
                'name': user_name,
                'login': user_login,
                'password': user_login,
                'category_id': [[6, 0, [category_search]]],
                'groups_id': [[6, 0, group_search]],
                'location_ids': [[6, 0, []]],
                'pos_ids': [[6, 0, pos_id]]
            }
        )
        context.helpers.user = user_login


@given("the patient {patient_name} is in {location} of {parent_location}")
def ensure_patient_in_system(context, patient_name, location, parent_location):
    """
    Make sure there's a patient in the system in the location specified

    :param context: Behave context
    :param patient_name: Name of the patient
    :param location: Location for the patient to be in
    :param parent_location: Parent of the location the patient should be in
    """
    # check parent location
    location_model = context.client.model('nh.clinical.location')
    context_model = context.client.model('nh.clinical.context')
    api_model = context.client.model('nh.eobs.api')
    eobs_context = context_model.search(
        [
            ['name', '=', 'eobs']
        ]
    )
    if not eobs_context:
        raise Exception('No eobs context found in system')
    # if parent location doesn't exist then create it
    parent_location_search = location_model.search(
        [
            ['name', '=', parent_location]
        ]
    )
    if not parent_location_search:
        hospital_search = location_model.search(
            [
                ['usage', '=', 'hospital']
            ]
        )
        if not hospital_search:
            hospital_search = location_model.create(
                {
                    'name': 'Test Hospital',
                    'code': 'TESTHOSP',
                    'type': 'pos',
                    'usage': 'hospital'
                }
            )
        parent_location_code = parent_location.replace(' ', '_').strip()
        parent_location_search = location_model.create(
            {
                'name': parent_location,
                'code': parent_location_code,
                'type': 'poc',
                'usage': 'ward',
                'parent_id': hospital_search[0],
                'context_ids': [[6, 0, eobs_context]]
            }
        )
        parent_location_search = parent_location_search.id
    else:
        parent_location_search = parent_location_search[0]
        parent_location_code = location_model.read(
            parent_location_search, ['code']).get('code')
    # check location
    location_search = location_model.search(
        [
            ['name', '=', location],
            ['parent_id', '=', parent_location_search]
        ]
    )
    # if location doesn't exist then create it under parent
    if not location_search:
        location_search = location_model.create(
            {
                'name': location,
                'code': location.replace(' ', '_').strip(),
                'type': 'poc',
                'usage': 'bed',
                'parent_id': parent_location_search,
                'context_ids': [[6, 0, eobs_context]]
            }
        )
        location_search = location_search.id
    else:
        location_search = location_search[0]
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
                'location': parent_location_code,
            }
        )
    # check patient isn't in location then place them there
    patients_location = patient_model.read(
        patient_search, ['current_location_id']).get('current_location_id')
    # if patient isn't in either location send to parent location
    if patients_location[0] not in [parent_location_search, location_search]:
        api_model.transfer(hospital_number, {'location': parent_location_code})
        patients_location = patient_model.read(
            patient_search, ['current_location_id']).get('current_location_id')
    # if current location is ward then place
    if patients_location[0] == parent_location_search:
        placement_model = context.client.model('nh.clinical.patient.placement')
        activity_model = context.client.model('nh.activity')
        placement_model.create_activity({}, {
            'suggested_location_id': location_search,
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
            placement_activity, {'location_id': location_search})
        activity_model.complete(placement_activity)
    context.patient = patient_name
