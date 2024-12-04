import numpy as np

FeedbackData = np.dtype(
    [
        (
            "msg_len",
            np.uint16,
        ),
        ("reserved1", np.int16, (3,)),
        #
        #
        (
            "digital_input_bits",
            np.int32,
        ),
        (
            "digital_outputs",
            np.int32,
        ),
        (
            "robot_mode",
            np.int32,
        ),
        (
            "controller_timestamp",
            np.int32,
        ),
        #
        #
        (
            "run_time",  # reserved2
            np.int32,
        ),
        (
            "test_value",
            np.int32,
        ),
        (
            "safety_mode",  # reserved3
            np.float64,
        ),
        #
        #
        (
            "speed_scaling",
            np.float64,
        ),
        (
            "linear_momentum_norm",
            np.float64,
        ),
        (
            "v_main",
            np.float64,
        ),
        (
            "v_robot",
            np.float64,
        ),
        (
            "i_robot",
            np.float64,
        ),
        #
        #
        (
            "program_state",  # reserved4
            np.float64,
        ),
        (
            "safety_status",  # reserved5
            np.float64,
        ),
        #
        #
        ("tool_accelerometer_values", np.float64, (3,)),
        ("elbow_position", np.float64, (3,)),
        ("elbow_velocity", np.float64, (3,)),
        #
        #
        ("q_target", np.float64, (6,)),
        ("qd_target", np.float64, (6,)),
        ("qdd_target", np.float64, (6,)),
        ("i_target", np.float64, (6,)),
        ("m_target", np.float64, (6,)),
        ("q_actual", np.float64, (6,)),
        ("qd_actual", np.float64, (6,)),
        ("i_actual", np.float64, (6,)),
        ("i_control", np.float64, (6,)),
        ("tool_vector_actual", np.float64, (6,)),
        ("TCP_speed_actual", np.float64, (6,)),
        ("TCP_force", np.float64, (6,)),
        ("tool_vector_target", np.float64, (6,)),
        ("TCP_speed_target", np.float64, (6,)),
        ("motor_temperatures", np.float64, (6,)),
        ("joint_modes", np.float64, (6,)),
        ("v_actual", np.float64, (6,)),
        #
        #
        ("hand_type", np.uint8, (4,)),
        (
            "user_coordinate",
            np.uint8,
        ),
        (
            "tool_coordinate",
            np.uint8,
        ),
        (
            "is_run_queued_cmd",
            np.uint8,
        ),
        (
            "is_pause_cmd_flag",
            np.uint8,
        ),
        (
            "velocity_ratio",
            np.uint8,
        ),
        (
            "acceleration_ratio",
            np.uint8,
        ),
        (
            "jerk_ratio",
            np.uint8,
        ),
        (
            "xyz_velocity_ratio",
            np.uint8,
        ),
        (
            "r_velocity_ratio",
            np.uint8,
        ),
        (
            "xyz_acceleration_ratio",
            np.uint8,
        ),
        (
            "r_acceleration_ratio",
            np.uint8,
        ),
        (
            "xyz_jerk_ratio",
            np.uint8,
        ),
        (
            "r_jerk_ratio",
            np.uint8,
        ),
        #
        #
        (
            "brake_status",
            np.uint8,
        ),
        (
            "enable_status",
            np.uint8,
        ),
        (
            "drag_status",
            np.uint8,
        ),
        (
            "running_status",
            np.uint8,
        ),
        (
            "error_status",
            np.uint8,
        ),
        (
            "jog_status",
            np.uint8,
        ),
        (
            "robot_type",
            np.uint8,
        ),
        (
            "drag_button_signal",
            np.uint8,
        ),
        (
            "enable_button_signal",
            np.uint8,
        ),
        (
            "record_button_signal",
            np.uint8,
        ),
        (
            "reappear_button_signal",
            np.uint8,
        ),
        (
            "jaw_button_signal",
            np.uint8,
        ),
        (
            "six_force_online",
            np.uint8,
        ),  # 1037
        #
        #
        ("reserved6", np.uint8, (82,)),
        #
        #
        ("m_actual[6]", np.float64, (6,)),  # Actual torque
        (
            "load",
            np.float64,
        ),  # Load weight in kg
        (
            "centerX",
            np.float64,
        ),
        (
            "centerY",
            np.float64,
        ),
        (
            "centerZ",
            np.float64,
        ),
        ("user", np.float64, (6,)),
        ("tool", np.float64, (6,)),
        (
            "traceIndex",
            np.float64,
        ),
        ("six_force_value", np.float64, (6,)),
        ("target_quaternion", np.float64, (4,)),
        ("actual_quaternion", np.float64, (4,)),
        #
        #
        ("reserved7", np.uint8, (24,)),
    ]
)
