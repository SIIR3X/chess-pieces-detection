import os
import sys
import argparse
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.utils.run_manager import clear_all_runs, clear_specific_run

def parse_args():
    """
    Parse command line arguments for clearing runs.

    Returns:
        argparse.Namespace: Parsed command line arguments.
    """
    parser = argparse.ArgumentParser(description="Delete one or all YOLO runs.")
    parser.add_argument("--run", type=str, help="Name of the run to delete (e.g., 'detect/chess-piece-detector2')")
    parser.add_argument("--all", action="store_true", help="Delete all runs")
    parser.add_argument("--dir", type=str, default="runs", help="Base runs directory")
    return parser.parse_args()

def main():
    """
    Main function to handle command line arguments and clear runs.

    This function checks if the user wants to delete a specific run or all runs,
    and calls the appropriate function from the run manager.
    """
    args = parse_args()

    if args.all:
        clear_all_runs(args.dir)
    elif args.run:
        clear_specific_run(args.run, args.dir)
    else:
        print("⚠️  Please specify --run <name> or use --all to delete everything.")

if __name__ == "__main__":
    main()
