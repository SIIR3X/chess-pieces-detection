import os
import sys
import random
import argparse
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.data.loader import load_piece_images, load_board_images
from src.generation.generator import generate_board_image

def parse_args():
    """
    Parse command line arguments for generating synthetic chessboards.

    Returns:
        argparse.Namespace: Parsed command line arguments.
    """
    parser = argparse.ArgumentParser(description="Generate synthetic chessboards with YOLO-format labels")
    parser.add_argument("--board_dir", type=str, default="data/raw/boards/", help="Directory of base board images")
    parser.add_argument("--piece_dir", type=str, default="data/raw/pieces/", help="Directory of chess piece images")
    parser.add_argument("--output_dir", type=str, default="data/dataset/", help="Output directory for generated data")
    parser.add_argument("--n_boards", type=int, default=1000, help="Total number of synthetic boards to generate")
    parser.add_argument("--seed", type=int, default=42, help="Random seed for reproducibility")
    parser.add_argument("--workers", type=int, default=8, help="Number of threads to use for generation")
    return parser.parse_args()

def main():
    """
    Main function to generate synthetic chessboards with YOLO-format labels.

    This function parses command line arguments, loads board and piece images,
    creates a train/validation split, and generates synthetic chessboard images
    with corresponding YOLO-format labels. The generated images and labels are
    saved to the specified output directory.
    """
    args = parse_args()

    # Load resources
    print("📥 Loading resources...")
    board_paths = load_board_images(args.board_dir)
    pieces_dict = load_piece_images(args.piece_dir)

    if not board_paths:
        print("❌ No board images found.")
        return
    if not pieces_dict:
        print("❌ No chess piece images loaded.")
        return

    # Create train/val split
    total = args.n_boards
    n_train = int(total * 0.8)
    n_val = total - n_train
    splits = ["train"] * n_train + ["val"] * n_val

    random.seed(args.seed)
    random.shuffle(splits)

    print(f"⚙️  Generating {n_train} training samples and {n_val} validation samples...")

    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        futures = []
        for i, split in enumerate(splits):
            futures.append(executor.submit(
                generate_board_image,
                i, board_paths, pieces_dict,
                args.output_dir, split
            ))

        for f in tqdm(futures, desc="🧠 Generating boards"):
            f.result()

    print("✅ Generation completed.")

if __name__ == "__main__":
    main()
