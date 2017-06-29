# pylint: disable=invalid-name
""" Get the selector to use on the thing by the name of the thing """
from .observation_selectors import BLOOD_GLUCOSE_ENTRY_FIELD, \
    RESPIRATION_RATE_ENTRY_FIELD, O2_SATURATION_ENTRY_FIELD, \
    BODY_TEMP_ENTRY_FIELD, BPS_ENTRY_FIELD, BPD_ENTRY_FIELD, \
    PULSE_RATE_ENTRY_FIELD, AVPU_ENTRY_FIELD, SUP_O2_ENTRY_FIELD, \
    O2_DEVICE_ENTRY_FIELD, EYES_OPEN_ENTRY_FIELD, BEST_MOT_RESP_ENTRY_FIELD, \
    BEST_VER_RESP_ENTRY_FIELD, PUP_LEFT_REACT_ENTRY_FIELD, \
    PUP_LEFT_SIZE_ENTRY_FIELD, PUP_RIGHT_REACT_ENTRY_FIELD, \
    PUP_RIGHT_SIZE_ENTRY_FIELD, LIMB_MOVE_LEFT_ARM_ENTRY_FIELD, \
    LIMB_MOVE_LEFT_LEG_ENTRY_FIELD, LIMB_MOVE_RIGHT_ARM_ENTRY_FIELD, \
    LIMB_MOVE_RIGHT_LEG_ENTRY_FIELD, WAIST_MEASSURE_ENTRY_FIELD, \
    TAKE_OBSERVATION_BUTTON


def get_observation_form_field_selector(field_name):
    """ something about what this does

    """
    return {
        'Blood Glucose (mmol/L)': BLOOD_GLUCOSE_ENTRY_FIELD,
        'Respiration Rate': RESPIRATION_RATE_ENTRY_FIELD,
        'O2 Saturation': O2_SATURATION_ENTRY_FIELD,
        'Body Temperature': BODY_TEMP_ENTRY_FIELD,
        'Blood Pressure Systolic': BPS_ENTRY_FIELD,
        'Blood Pressure Diastolic': BPD_ENTRY_FIELD,
        'Pulse Rate': PULSE_RATE_ENTRY_FIELD,
        'AVPU': AVPU_ENTRY_FIELD,
        'Patient on supplemental O2': SUP_O2_ENTRY_FIELD,
        'O2 Device': O2_DEVICE_ENTRY_FIELD,
        'Eyes Open': EYES_OPEN_ENTRY_FIELD,
        'Best Verbal Response': BEST_VER_RESP_ENTRY_FIELD,
        'Best Motor Response': BEST_MOT_RESP_ENTRY_FIELD,
        'Pupil Right - Size': PUP_RIGHT_SIZE_ENTRY_FIELD,
        'Pupil Right - Reaction': PUP_RIGHT_REACT_ENTRY_FIELD,
        'Pupil Left - Size': PUP_LEFT_SIZE_ENTRY_FIELD,
        'Pupil Left - Reaction': PUP_LEFT_REACT_ENTRY_FIELD,
        'Limb Movement - Left Arm': LIMB_MOVE_LEFT_ARM_ENTRY_FIELD,
        'Limb Movement - Right Arm': LIMB_MOVE_RIGHT_ARM_ENTRY_FIELD,
        'Limb Movement - Left Leg': LIMB_MOVE_LEFT_LEG_ENTRY_FIELD,
        'Limb Movement - Right Leg': LIMB_MOVE_RIGHT_LEG_ENTRY_FIELD,
        'Waist Measurement (cm)': WAIST_MEASSURE_ENTRY_FIELD,
    }.get(field_name)


def get_button_selector(button_name):
    """
    something about what this does
    """
    return {
        'Take observation': TAKE_OBSERVATION_BUTTON,
    }.get(button_name)