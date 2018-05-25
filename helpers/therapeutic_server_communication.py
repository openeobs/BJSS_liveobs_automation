"""
Functions for communicating with Therapeutic models on the server. Helpful for
things like setting up state at the beginning of tests.
"""


def get_current_therapeutic_obs_level_record(context, patient_name):
    """
    Private method that encapsulates the retrieval of the latest therapeutic
    level record.

    :param context:
    :param patient_name:
    :return:
    """
    level_model = context.client.model('nh.clinical.therapeutic.level')
    domain = [('patient', '=', context.patients[patient_name].id)]
    current_level_id = level_model.search(domain, order='id desc', limit=1)
    current_level = level_model.browse(current_level_id[0])
    return current_level
