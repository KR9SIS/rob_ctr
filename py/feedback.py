import numpy as np

FeedbackData = np.dtype(
    [
        ("msg_len", np.uint16, (1,)),
        ("reserved1", np.int16, (3,)),
        #
        #
        ("digital_input_bits", np.int32, (1,)),
        ("digital_outputs", np.int32, (1,)),
        ("robot_mode", np.int32, (1,)),
        ("controller_timestamp", np.int32, (1,)),
        #
        #
        ("run_time", np.int32, (1,)),  # reserved2
        ("test_value", np.int32, (1,)),
        ("safety_mode", np.float64, (1,)),  # reserved3
        #
        #
        ("speed_scaling", np.float64, (1,)),
        ("linear_momentum_norm", np.float64, (1,)),
        ("v_main", np.float64, (1,)),
        ("v_robot", np.float64, (1,)),
        ("i_robot", np.float64, (1,)),
        #
        #
        ("program_state", np.float64, (1,)),  # reserved4
        ("safety_status", np.float64, (1,)),  # reserved5
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
        ("user_coordinate", np.uint8, (1,)),
        ("tool_coordinate", np.uint8, (1,)),
        ("is_run_queued_cmd", np.uint8, (1,)),
        ("is_pause_cmd_flag", np.uint8, (1,)),
        ("velocity_ratio", np.uint8, (1,)),
        ("acceleration_ratio", np.uint8, (1,)),
        ("jerk_ratio", np.uint8, (1,)),
        ("xyz_velocity_ratio", np.uint8, (1,)),
        ("r_velocity_ratio", np.uint8, (1,)),
        ("xyz_acceleration_ratio", np.uint8, (1,)),
        ("r_acceleration_ratio", np.uint8, (1,)),
        ("xyz_jerk_ratio", np.uint8, (1,)),
        ("r_jerk_ratio", np.uint8, (1,)),
        #
        #
        ("brake_status", np.uint8, (1,)),
        ("enable_status", np.uint8, (1,)),
        ("drag_status", np.uint8, (1,)),
        ("running_status", np.uint8, (1,)),
        ("error_status", np.uint8, (1,)),
        ("jog_status", np.uint8, (1,)),
        ("robot_type", np.uint8, (1,)),
        ("drag_button_signal", np.uint8, (1,)),
        ("enable_button_signal", np.uint8, (1,)),
        ("record_button_signal", np.uint8, (1,)),
        ("reappear_button_signal", np.uint8, (1,)),
        ("jaw_button_signal", np.uint8, (1,)),
        ("six_force_online", np.uint8, (1,)),  # 1037
        #
        #
        ("reserved6", np.uint8, (82,)),
        #
        #
        ("m_actual[6]", np.float64, (6,)),  # Actual torque
        ("load", np.float64, (1,)),  # Load weight in kg
        ("centerX", np.float64, (1,)),
        ("centerY", np.float64, (1,)),
        ("centerZ", np.float64, (1,)),
        ("user", np.float64, (6,)),
        ("tool", np.float64, (6,)),
        ("traceIndex", np.float64, (1,)),
        ("six_force_value", np.float64, (6,)),
        ("target_quaternion", np.float64, (4,)),
        ("actual_quaternion", np.float64, (4,)),
        #
        #
        ("reserved7", np.uint8, (24,)),
        #
        #
        ("last24", np.double, (3,)),
    ]
)
if __name__ == "__main__":
    print(FeedbackData.itemsize)
