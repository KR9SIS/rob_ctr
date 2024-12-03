from dataclasses import dataclass, field


@dataclass
class FeedbackData:
    message_size: int  # Total message size in bytes
    reserved1: list[int] = field(default_factory=lambda: [0] * 3)

    digital_inputs: int = 0  # Digital inputs
    digital_outputs: int = 0  # Digital outputs
    robot_mode: int = 0  # Robot mode, 9 indicates an error
    time_stamp: int = 0  # Timestamp (in ms)

    reserved2: int = 0
    test_value: int = 0  # Memory structure test standard value 0x0123 4567 89AB CDEF
    reserved3: float = 0.0

    speed_scaling: float = 0.0  # Speed scaling
    linear_momentum_norm: float = 0.0  # Current robot momentum
    v_main: float = 0.0  # Control board voltage
    v_robot: float = 0.0  # Robot voltage
    i_robot: float = 0.0  # Robot current

    reserved4: float = 0.0
    reserved5: float = 0.0

    tool_accelerometer_values: list[float] = field(
        default_factory=lambda: [0.0] * 3
    )  # TCP acceleration
    elbow_position: list[float] = field(
        default_factory=lambda: [0.0] * 3
    )  # Elbow position
    elbow_velocity: list[float] = field(
        default_factory=lambda: [0.0] * 3
    )  # Elbow velocity

    q_target: list[float] = field(
        default_factory=lambda: [0.0] * 6
    )  # Target joint position
    qd_target: list[float] = field(
        default_factory=lambda: [0.0] * 6
    )  # Target joint speed
    qdd_target: list[float] = field(
        default_factory=lambda: [0.0] * 6
    )  # Target joint acceleration
    i_target: list[float] = field(
        default_factory=lambda: [0.0] * 6
    )  # Target joint current
    m_target: list[float] = field(
        default_factory=lambda: [0.0] * 6
    )  # Target joint torque
    q_actual: list[float] = field(
        default_factory=lambda: [0.0] * 6
    )  # Actual joint position
    qd_actual: list[float] = field(
        default_factory=lambda: [0.0] * 6
    )  # Actual joint speed
    i_actual: list[float] = field(
        default_factory=lambda: [0.0] * 6
    )  # Actual joint current
    i_control: list[float] = field(
        default_factory=lambda: [0.0] * 6
    )  # TCP sensor force value
    tool_vector_actual: list[float] = field(
        default_factory=lambda: [0.0] * 6
    )  # TCP actual Cartesian coordinates
    tcp_speed_actual: list[float] = field(
        default_factory=lambda: [0.0] * 6
    )  # TCP actual speed value
    tcp_force: list[float] = field(default_factory=lambda: [0.0] * 6)  # TCP force value
    tool_vector_target: list[float] = field(
        default_factory=lambda: [0.0] * 6
    )  # TCP target Cartesian coordinates
    tcp_speed_target: list[float] = field(
        default_factory=lambda: [0.0] * 6
    )  # TCP target speed value
    motor_temperatures: list[float] = field(
        default_factory=lambda: [0.0] * 6
    )  # Joint temperatures
    joint_modes: list[float] = field(
        default_factory=lambda: [0.0] * 6
    )  # Joint control mode
    v_actual: list[float] = field(default_factory=lambda: [0.0] * 6)  # Joint voltage

    hand_type: list[int] = field(default_factory=lambda: [0] * 4)  # Hand type
    user: int = 0  # User coordinates
    tool: int = 0  # Tool coordinates
    run_queued_cmd: int = 0  # Queue algorithm run flag
    pause_cmd_flag: int = 0  # Queue algorithm pause flag
    velocity_ratio: int = 0  # Joint speed ratio (0~100)
    acceleration_ratio: int = 0  # Joint acceleration ratio (0~100)
    jerk_ratio: int = 0  # Joint jerk ratio (0~100)
    xyz_velocity_ratio: int = 0  # Cartesian position speed ratio (0~100)
    r_velocity_ratio: int = 0  # Cartesian attitude speed ratio (0~100)
    xyz_acceleration_ratio: int = 0  # Cartesian position acceleration ratio (0~100)
    r_acceleration_ratio: int = 0  # Cartesian attitude acceleration ratio (0~100)
    xyz_jerk_ratio: int = 0  # Cartesian position jerk ratio (0~100)
    r_jerk_ratio: int = 0  # Cartesian attitude jerk ratio (0~100)

    brake_status: int = 0  # Robot brake status
    enable_status: int = 0  # Robot enable status
    drag_status: int = 0  # Robot drag status
    running_status: int = 0  # Robot running status
    error_status: int = 0  # Robot error status
    jog_status: int = 0  # Robot jog status
    robot_type: int = 0  # Robot type
    drag_button_signal: int = 0  # Drag button signal on control panel
    enable_button_signal: int = 0  # Enable button signal on control panel
    record_button_signal: int = 0  # Record button signal on control panel
    reappear_button_signal: int = 0  # Reappear button signal on control panel
    jaw_button_signal: int = 0  # Jaw control signal on control panel
    six_force_online: int = 0  # Six-axis force online status

    reserved6: list[int] = field(default_factory=lambda: [0] * 82)

    m_actual: list[float] = field(default_factory=lambda: [0.0] * 6)  # Actual torque
    load: float = 0.0  # Load weight in kg
    center_x: float = 0.0  # Offset distance in X direction (mm)
    center_y: float = 0.0  # Offset distance in Y direction (mm)
    center_z: float = 0.0  # Offset distance in Z direction (mm)
    user_value: list[float] = field(
        default_factory=lambda: [0.0] * 6
    )  # User coordinate values
    tools: list[float] = field(
        default_factory=lambda: [0.0] * 6
    )  # Tool coordinate values
    trace_index: float = 0.0  # Trace replay index
    six_force_value: list[float] = field(
        default_factory=lambda: [0.0] * 6
    )  # Raw six-axis force data
    target_quaternion: list[float] = field(
        default_factory=lambda: [0.0] * 4
    )  # Target quaternion [qw, qx, qy, qz]
    actual_quaternion: list[float] = field(
        default_factory=lambda: [0.0] * 4
    )  # Actual quaternion [qw, qx, qy, qz]

    reserved7: list[int] = field(default_factory=lambda: [0] * 24)
