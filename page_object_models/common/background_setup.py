"""
Page Object Model for Background setup
Contains the methods used in the Background steps
"""


def get_role_id_for_group(model, group):
    """
    Get the ID for the group
    :param model: Group Model
    :param group: Name of the group
    :return: ID for the group
    """
    group_search = model.search(
        [
            ['name', '=', group]
        ]
    )
    if not group_search:
        raise Exception("No group {} found".format(group))
    return group_search[0]


def get_role_id_for_category(category_model, user_role):
    """
    Get the ID for the category
    :param category_model: Category Model
    :param user_role: Name of the category
    :return: ID for the category
    """
    category_search = category_model.search(
        [
            ['name', '=', user_role]
        ]
    )
    if category_search:
        return category_search[0]
    else:
        raise Exception("No category {} found".format(user_role))


def get_or_create_user(client, name):
    """
    Checks if a user exists by given name, otherwise creates one with that name

    :param client: ERPPeek Client
    :param name: user name to search for
    :return: user credentials
    """
    user = get_user_credentials(client, name)
    if not user:
        user = create_user(client, name)
    return user


def create_user(client, name):
    """
    Creates a user record in the system with a specified name
    :param client: ERPPeek Client
    :param name: name for the user
    :return: user login credentials
    """
    user_model = client.model('res.users')
    location_model = client.model('nh.clinical.location')
    group_model = client.model('res.groups')
    employee_group = get_role_id_for_group(group_model, 'Employee')
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
    user_login = name.lower().replace(' ', '_').strip()
    user_model.create(
        {
            'name': name,
            'login': user_login,
            'password': user_login,
            'groups_id': [[6, 0, [employee_group]]],
            'location_ids': [[6, 0, []]],
            'pos_ids': [[6, 0, pos_id]]
        }
    )
    return user_login


def assign_user_roles(client, name, role):
    """
    Add a user role to a specified user

    :param client: ERPPeek Client
    :param name: name of the user to set the role for
    :param role: role for the user to set in the system
    """
    group_model = client.model('res.groups')
    category_model = client.model('res.partner.category')
    #
    # TODO EOBS-2335
    #
    if role == 'System Administrator':
        user_role = get_role_id_for_group(
            group_model,
            'NH Clinical {} Group'.format('Admin')
        )
    else:
        user_role = get_role_id_for_group(
            group_model,
            'NH Clinical {} Group'.format(role)
        )
    role_category = get_role_id_for_category(category_model, role)
    user = get_user_record(client, name)
    if user:
        user.write({
            'groups_id': [[4, user_role]],
            'category_id': [[6, 0, [role_category]]]
        })
    else:
        raise Exception("User %s is not in the system", name)


def get_user_record(client, name):
    """
    Find a specific user record in the system

    :param client: ERPPeek Client
    :param name: name of the user to find
    :return: record of the user
    """
    user_model = client.model('res.users')
    user_search = user_model.search(
        [
            ['name', '=', name]
        ]
    )
    if user_search:
        return user_model.browse(user_search[0])
    return None


def get_user_credentials(client, name):
    """
    Get the user record login credentials

    :param client: ERPPeek Client
    :param name: name of the user to search
    :return: user login credentials or None if user doesn't exist
    """
    user_search = get_user_record(client, name)
    if user_search:
        return user_search.login
    return None
