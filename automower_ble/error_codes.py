from enum import IntEnum


class ErrorCodes(IntEnum):
    UNEXPECTED_ERROR = 0
    OUTSIDE_WORKING_AREA = 1
    NO_LOOP_SIGNAL = 2
    WRONG_LOOP_SIGNAL = 3
    LOOP_SENSOR_PROBLEM_FRONT = 4
    LOOP_SENSOR_PROBLEM_REAR = 5
    LOOP_SENSOR_PROBLEM_LEFT = 6
    LOOP_SENSOR_PROBLEM_RIGHT = 7
    WRONG_PIN_CODE = 8
    TRAPPED = 9
    UPSIDE_DOWN = 10
    LOW_BATTERY = 11
    EMPTY_BATTERY = 12
    NO_DRIVE = 13
    MOWER_LIFTED = 14
    LIFTED = 15
    STUCK_IN_CHARGING_STATION = 16
    CHARGING_STATION_BLOCKED = 17
    COLLISION_SENSOR_PROBLEM_REAR = 18
    COLLISION_SENSOR_PROBLEM_FRONT = 19
    WHEEL_MOTOR_BLOCKED_RIGHT = 20
    WHEEL_MOTOR_BLOCKED_LEFT = 21
    WHEEL_DRIVE_PROBLEM_RIGHT = 22
    WHEEL_DRIVE_PROBLEM_LEFT = 23
    CUTTING_SYSTEM_BLOCKED = 24
    CUTTING_SYSTEM_BLOCKED_2 = 25
    INVALID_SUB_DEVICE_COMBINATION = 26
    SETTINGS_RESTORED = 27
    MEMORY_CIRCUIT_PROBLEM = 28
    SLOPE_TOO_STEEP = 29
    CHARGING_SYSTEM_PROBLEM = 30
    STOP_BUTTON_PROBLEM = 31
    TILT_SENSOR_PROBLEM = 32
    MOWER_TILTED = 33
    CUTTING_STOPPED_SLOPE_TOO_STEEP = 34
    WHEEL_MOTOR_OVERLOADED_RIGHT = 35
    WHEEL_MOTOR_OVERLOADED_LEFT = 36
    CHARGING_CURRENT_TOO_HIGH = 37
    ELECTRONIC_PROBLEM = 38
    CUTTING_MOTOR_PROBLEM = 39
    LIMITED_CUTTING_HEIGHT_RANGE = 40
    UNEXPECTED_CUTTING_HEIGHT_ADJ = 41
    LIMITED_CUTTING_HEIGHT_RANGE_2 = 42
    CUTTING_HEIGHT_PROBLEM_DRIVE = 43
    CUTTING_HEIGHT_PROBLEM_CURR = 44
    CUTTING_HEIGHT_PROBLEM_DIR = 45
    CUTTING_HEIGHT_BLOCKED = 46
    CUTTING_HEIGHT_PROBLEM = 47
    NO_RESPONSE_FROM_CHARGER = 48
    ULTRASONIC_PROBLEM = 49
    GUIDE_1_NOT_FOUND = 50
    GUIDE_2_NOT_FOUND = 51
    GUIDE_3_NOT_FOUND = 52
    GPS_NAVIGATION_PROBLEM = 53
    WEAK_GPS_SIGNAL = 54
    DIFFICULT_FINDING_HOME = 55
    GUIDE_CALIBRATION_ACCOMPLISHED = 56
    GUIDE_CALIBRATION_FAILED = 57
    TEMPORARY_BATTERY_PROBLEM = 58
    TEMPORARY_BATTERY_PROBLEM_2 = 59
    TEMPORARY_BATTERY_PROBLEM_3 = 60
    TEMPORARY_BATTERY_PROBLEM_4 = 61
    TEMPORARY_BATTERY_PROBLEM_5 = 62
    TEMPORARY_BATTERY_PROBLEM_6 = 63
    TEMPORARY_BATTERY_PROBLEM_7 = 64
    TEMPORARY_BATTERY_PROBLEM_8 = 65
    BATTERY_PROBLEM = 66
    BATTERY_PROBLEM_2 = 67
    TEMPORARY_BATTERY_PROBLEM_9 = 68
    ALARM_MOWER_SWITCHED_OFF = 69
    ALARM_MOWER_STOPPED = 70
    ALARM_MOWER_LIFTED = 71
    ALARM_MOWER_TILTED = 72
    ALARM_MOWER_IN_MOTION = 73
    ALARM_OUTSIDE_GEOFENCE = 74
    CONNECTION_CHANGED = 75
    CONNECTION_NOT_CHANGED = 76
    COM_BOARD_NOT_AVAILABLE = 77
    SLIPPED_MOWER_HAS_SLIPPED = 78
    INVALID_BATTERY_COMBINATION = 79
    CUTTING_SYSTEM_IMBALANCE = 80
    SAFETY_FUNCTION_FAULTY = 81
    WHEEL_MOTOR_BLOCKED_REAR_RIGHT = 82
    WHEEL_MOTOR_BLOCKED_REAR_LEFT = 83
    WHEEL_DRIVE_PROBLEM_REAR_RIGHT = 84
    WHEEL_DRIVE_PROBLEM_REAR_LEFT = 85
    WHEEL_MOTOR_OVERLOADED_REAR_RIGHT = 86
    WHEEL_MOTOR_OVERLOADED_REAR_LEFT = 87
    ANGULAR_SENSOR_PROBLEM = 88
    INVALID_SYSTEM_CONFIGURATION = 89
    NO_POWER_IN_CHARGING_STATION = 90
    SWITCH_CORD_PROBLEM = 91
    WORK_AREA_NOT_VALID = 92
    NO_ACCURATE_POSITION_FROM_SATELLITES = 93
    REFERENCE_STATION_COMMUNICATION_PROBLEM = 94
    FOLDING_SENSOR_ACTIVATED = 95
    RIGHT_BRUSH_MOTOR_OVERLOADED = 96
    LEFT_BRUSH_MOTOR_OVERLOADED = 97
    ULTRASONIC_SENSOR_1_DEFECT = 98
    ULTRASONIC_SENSOR_2_DEFECT = 99
    ULTRASONIC_SENSOR_3_DEFECT = 100
    ULTRASONIC_SENSOR_4_DEFECT = 101
    CUTTING_DRIVE_MOTOR_1_DEFECT = 102
    CUTTING_DRIVE_MOTOR_2_DEFECT = 103
    CUTTING_DRIVE_MOTOR_3_DEFECT = 104
    LIFT_SENSOR_DEFECT = 105
    COLLISION_SENSOR_DEFECT = 106
    DOCKING_SENSOR_DEFECT = 107
    FOLDING_CUTTING_DECK_SENSOR_DEFECT = 108
    LOOP_SENSOR_DEFECT = 109
    COLLISION_SENSOR_ERROR = 110
    NO_CONFIRMED_POSITION = 111
    CUTTING_SYSTEM_MAJOR_IMBALANCE = 112
    COMPLEX_WORKING_AREA = 113
    TOO_HIGH_DISCHARGE_CURRENT = 114
    TOO_HIGH_INTERNAL_CURRENT = 115
    HIGH_CHARGING_POWER_LOSS = 116
    HIGH_INTERNAL_POWER_LOSS = 117
    CHARGING_SYSTEM_PROBLEM_2 = 118
    ZONE_GENERATOR_PROBLEM = 119
    INTERNAL_VOLTAGE_ERROR = 120
    HIGH_INTERNAL_TEMPERATURE = 121
    CAN_ERROR = 122
    DESTINATION_NOT_REACHABLE = 123
    DESTINATION_BLOCKED = 124
    BATTERY_NEEDS_REPLACEMENT = 125
    BATTERY_NEAR_END_OF_LIFE = 126
    BATTERY_PROBLEM_3 = 127
    MULTIPLE_REFERENCE_STATIONS_DETECTED = 128
    AUXILIARY_CUTTING_MEANS_BLOCKED = 129
    IMBALANCED_AUXILIARY_CUTTING_DISC_DETECTED = 130
    LIFTED_IN_LINK_ARM = 131
    EPOS_ACCESSORY_MISSING = 132
    BLUETOOTH_COM_WITH_CS_FAILED = 133
    INVALID_SW_CONFIGURATION = 134
    RADAR_PROBLEM = 135
    WORK_AREA_TAMPERED = 136
    HIGH_TEMPERATURE_IN_CUTTING_MOTOR_RIGHT = 137
    HIGH_TEMPERATURE_IN_CUTTING_MOTOR_CENTER = 138
    HIGH_TEMPERATURE_IN_CUTTING_MOTOR_LEFT = 139
    WHEEL_BRUSH_MOTOR_PROBLEM = 141
    ACCESSORY_POWER_PROBLEM = 143
    BOUNDARY_WIRE_PROBLEM = 144
    CONNECTIVITY_PROBLEM = 701
    CONNECTIVITY_SETTINGS_RESTORED = 702
    CONNECTIVITY_PROBLEM_2 = 703
    CONNECTIVITY_PROBLEM_3 = 704
    CONNECTIVITY_PROBLEM_4 = 705
    POOR_SIGNAL_QUALITY = 706
    SIM_CARD_REQUIRES_PIN = 707
    SIM_CARD_LOCKED = 708
    SIM_CARD_NOT_FOUND = 709
    SIM_CARD_LOCKED_2 = 710
    SIM_CARD_LOCKED_3 = 711
    SIM_CARD_LOCKED_4 = 712
    GEOFENCE_PROBLEM = 713
    GEOFENCE_PROBLEM_2 = 714
    CONNECTIVITY_PROBLEM_5 = 715
    CONNECTIVITY_PROBLEM_6 = 716
    SMS_COULD_NOT_BE_SENT = 717
    COMMUNICATION_CIRCUIT_BOARD_SW_MUST_BE_UPDATED = 724