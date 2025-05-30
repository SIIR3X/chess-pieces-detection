import os
import sys
import argparse
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.training.runner import run_training

def parse_args():
    """
    Parses command line arguments for training configuration.
    
    Returns:
        argparse.Namespace: Parsed command line arguments.
    """
    parser = argparse.ArgumentParser(description="Train YOLO model with configuration.")
    parser.add_argument(
        "--config",
        type=str,
        default="config/train_config.yaml",
        help="Path to the training configuration YAML file"
    )
    return parser.parse_args()

def main():
    """
    Main function to parse arguments and run the training process.
    """
    args = parse_args()
    run_training(config_path=args.config)

if __name__ == "__main__":
    main()
