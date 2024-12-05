import numpy as np

FeedbackData = np.dtype(
    [
        # Meaning, Data type, Number of values
        ("msg_len", np.ushort, (1,)),
        ("reserved1", np.ushort, (3,)),
        #
        ("digital_input_bits", np.uint64, (1,)),
        ("digital_outputs", np.uint64, (1,)),
        ("robot_mode", np.uint64, (1,)),
        ("controller_timestamp", np.uint64, (1,)),
        #
        ("run_time", np.uint64, (1,)),  # reserved2
        ("test_value", np.ulonglong, (1,)),
        ("safety_mode", np.double, (1,)),  # reserved3
        #
        ("speed_scaling", np.double, (1,)),
        ("linear_momentum_norm", np.double, (1,)),
        ("v_main", np.double, (1,)),
        ("v_robot", np.double, (1,)),
        ("i_robot", np.double, (1,)),
        #
        ("program_state", np.double, (1,)),  # reserved4
        ("safety_status", np.double, (1,)),  # reserved5
        #
        ("tool_accelerometer_values", np.double, (3,)),
        ("elbow_position", np.double, (3,)),
        ("elbow_velocity", np.double, (3,)),
        #
        ("q_target", np.double, (6,)),
        ("qd_target", np.double, (6,)),
        ("qdd_target", np.double, (6,)),
        ("i_target", np.double, (6,)),
        ("m_target", np.double, (6,)),
        #
        ("q_actual", np.double, (6,)),
        ("qd_actual", np.double, (6,)),
        ("i_actual", np.double, (6,)),
        ("i_control", np.double, (6,)),
        ("tool_vector_actual", np.double, (6,)),
        ("TCP_speed_actual", np.double, (6,)),
        #
        ("TCP_force", np.double, (6,)),
        ("tool_vector_target", np.double, (6,)),
        ("TCP_speed_target", np.double, (6,)),
        ("motor_temperatures", np.double, (6,)),
        ("joint_modes", np.double, (6,)),
        ("v_actual", np.double, (6,)),
        #
        ("hand_type", np.byte, (4,)),
        #
        ("user_coordinate", np.byte, (1,)),
        ("tool_coordinate", np.byte, (1,)),
        #
        ("is_run_queued_cmd", np.byte, (1,)),
        ("is_pause_cmd_flag", np.byte, (1,)),
        #
        ("velocity_ratio", np.byte, (1,)),
        ("acceleration_ratio", np.byte, (1,)),
        ("jerk_ratio", np.byte, (1,)),
        ("xyz_velocity_ratio", np.byte, (1,)),
        ("r_velocity_ratio", np.byte, (1,)),
        ("xyz_acceleration_ratio", np.byte, (1,)),
        ("r_acceleration_ratio", np.byte, (1,)),
        ("xyz_jerk_ratio", np.byte, (1,)),
        ("r_jerk_ratio", np.byte, (1,)),
        #
        ("brake_status", np.byte, (1,)),
        ("enable_status", np.byte, (1,)),
        ("drag_status", np.byte, (1,)),
        ("running_status", np.byte, (1,)),
        ("error_status", np.byte, (1,)),
        ("jog_status", np.byte, (1,)),
        #
        ("robot_type", np.byte, (1,)),
        ("drag_button_signal", np.byte, (1,)),
        ("enable_button_signal", np.byte, (1,)),
        ("record_button_signal", np.byte, (1,)),
        ("reappear_button_signal", np.byte, (1,)),
        ("jaw_button_signal", np.byte, (1,)),
        ("six_force_online", np.byte, (1,)),  # 1037
        #
        ("reserved6", np.byte, (82,)),  # Size in bytes 82
        #
        ("m_actual[6]", np.double, (6,)),  # Actual torque
        #
        ("load", np.double, (1,)),  # Load weight in kg
        #
        ("centerX", np.double, (1,)),
        ("centerY", np.double, (1,)),
        ("centerZ", np.double, (1,)),
        #
        ("user", np.double, (6,)),
        ("tool", np.double, (6,)),
        #
        ("traceIndex", np.double, (1,)),
        #
        ("six_force_value", np.double, (6,)),
        #
        ("target_quaternion", np.double, (4,)),
        ("actual_quaternion", np.double, (4,)),
        #
        ("reserved7", np.byte, (24,)),
    ]
)
if __name__ == "__main__":
    print(FeedbackData.itemsize)  # Should be 1440
