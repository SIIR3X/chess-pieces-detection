import os
import sys
import argparse
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.utils.cleaner import clear_subfolders_content

def parse_args():
    """
    Parse command line arguments for clearing dataset subfolders.

    Returns:
        argparse.Namespace: Parsed command line arguments.
    """
    parser = argparse.ArgumentParser(description="Clear content of dataset subfolders")
    parser.add_argument("--dataset_dir", type=str, default="data/dataset/", help="Directory of the dataset to clear")
    return parser.parse_args()

def main():
    """
    Main function to clear the content of dataset subfolders.

    This function parses command line arguments and clears the content of all
    subfolders in the specified dataset directory without deleting the subfolders themselves.
    """
    args = parse_args()

    # Clear subfolders content
    print(f"🗑️  Clearing content of dataset subfolders in: {args.dataset_dir}")
    clear_subfolders_content(args.dataset_dir)
    print("✅  Content cleared successfully.")

if __name__ == "__main__":
    main()
