""" Selectors for the observation form data entry"""

from selenium.webdriver.common.by import By

# Locator used in automation tests - BG Obs form
BLOOD_GLUCOSE_ENTRY_FIELD = (By.ID, 'parent_blood_glucose')

# Locator used in automation tests - NEWS Obs form
RESPIRATION_RATE_ENTRY_FIELD = (By.ID, 'parent_respiration_rate')
O2_SATURATION_ENTRY_FIELD = (By.ID, 'parent_indirect_oxymetry_spo2')
BODY_TEMP_ENTRY_FIELD = (By.ID, 'parent_body_temperature')
BPS_ENTRY_FIELD = (By.ID, 'parent_blood_pressure_systolic')
BPD_ENTRY_FIELD = (By.ID, 'parent_blood_pressure_diastolic')
PULSE_RATE_ENTRY_FIELD = (By.ID, 'parent_pulse_rate')
AVPU_ENTRY_FIELD = (By.ID, 'parent_avpu_text')
SUP_O2_ENTRY_FIELD = (By.ID, 'parent_oxygen_administration_flag')
O2_DEVICE_ENTRY_FIELD = (By.ID, 'parent_device_id')
FLOW_RATE_DATA_TYPE = (By.ID, 'parent_flow_rate')
CONCENTRATION_DATA_TYPE = (By.ID, 'parent_concentration')

# Locator used in automation tests - Neuro Obs form
EYES_OPEN_ENTRY_FIELD = (By.ID, 'parent_eyes')
BEST_VER_RESP_ENTRY_FIELD = (By.ID, 'parent_verbal')
BEST_MOT_RESP_ENTRY_FIELD = (By.ID, 'parent_motor')
PUP_RIGHT_SIZE_ENTRY_FIELD = (By.ID, 'parent_pupil_right_size')
PUP_RIGHT_REACT_ENTRY_FIELD = (By.ID, 'parent_pupil_right_reaction')
PUP_LEFT_SIZE_ENTRY_FIELD = (By.ID, 'parent_pupil_left_size')
PUP_LEFT_REACT_ENTRY_FIELD = (By.ID, 'parent_pupil_left_reaction')
LIMB_MOVE_LEFT_ARM_ENTRY_FIELD = (By.ID, 'parent_limb_movement_left_arm')
LIMB_MOVE_RIGHT_ARM_ENTRY_FIELD = (By.ID, 'parent_limb_movement_right_arm')
LIMB_MOVE_LEFT_LEG_ENTRY_FIELD = (By.ID, 'parent_limb_movement_left_leg')
LIMB_MOVE_RIGHT_LEG_ENTRY_FIELD = (By.ID, 'parent_limb_movement_left_arm')

# Locators used in automation tests - Weight Obs form
WAIST_MEASSURE_ENTRY_FIELD = (By.ID, 'parent_waist_measurement')

# Locators used in automation tests - Postural Blood Pressure Obs form
SIT_BP_SYS_ENTRY_FIELD = (By.ID, 'parent_systolic_sitting')
SIT_BP_DIAS_ENTRY_FIELD = (By.ID, 'parent_diastolic_sitting')
STAN_BP_SYS_ENTRY_FIELD = (By.ID, 'parent_systolic_standing')
STAN_BP_DIAS_ENTRY_FIELD = (By.ID, 'parent_diastolic_standing')

# Locators for mobile buttons
TAKE_OBSERVATION_BUTTON = (By.ID, 'take-observation')
POPUP_RISK = (By.CSS_SELECTOR, '#submit_observation strong')
NEWS_SCORE = (By.CSS_SELECTOR, 'div#submit_observation>h2')
