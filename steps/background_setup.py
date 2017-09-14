from behave import given
from haikunator import Haikunator


@given('a user exists with the {user_role} role')
def ensure_user_with_role(context, user_role):
    """
    Do a search for user with the specified role or create one

    :param context: Behave context
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
            ['groups_id', 'in', group_search]
        ]
    )
    if user_search:
        context.helpers.user = \
            user_model.read(user_search[0], ['login']).get('login')
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
        haiku = Haikunator()
        user_login = haiku.haikunate(token_length=0)
        user_model.create(
            {
                'name': user_login,
                'login': user_login,
                'password': user_login,
                'category_id': [[6, 0, [category_search]]],
                'groups_id': [[6, 0, group_search]],
                'location_ids': [[6, 0, []]],
                'pos_ids': [[6, 0, pos_id]]
            }
        )
        context.helpers.user = user_login
