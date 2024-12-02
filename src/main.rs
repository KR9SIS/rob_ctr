use clap::{command, Parser, Subcommand};
use robot::{RobotConn, RobotFeedbackConn};

mod robot;
pub mod feedback;

/// Cli to control dobot robot
#[derive(Parser, Debug)]
#[command(about, long_about = None)]
struct Args {
    #[clap(subcommand)]
    command: Command,
}

#[derive(Debug, Subcommand)]
enum Command {
    On,
    Off,
    Move {
        x: f64,
        y: f64,
        z: f64,
        r: f64
    },
    Do {
        index: i32,
        status: i32
    },
    Feedback
}

fn main() -> anyhow::Result<()> {
    let args = Args::parse();

    let mut robot = RobotConn::connect()?;

    match args.command {
        Command::On => robot.enable_robot()?,
        Command::Off => robot.disable_robot()?,
        Command::Move { x, y, z, r } => robot.mov_j(x, y, z, r)?,
        Command::Do { index, status } => robot.set_do(index, status)?,
        Command::Feedback => {
            let feedback = RobotFeedbackConn::connect()?.receive_feedback()?;
            println!("{feedback:#?}");
        }
    }

    Ok(())
}
