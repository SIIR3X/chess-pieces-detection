import os
import random
from PIL import Image
from src.utils.yolo import normalize_bbox
from src.utils.structure import get_output_paths

SQUARE_SIZE = 64
BOARD_SIZE = 8
IMAGE_SIZE = SQUARE_SIZE * BOARD_SIZE

PIECE_CLASSES = {
    'wp': 0, 'wn': 1, 'wb': 2, 'wr': 3, 'wq': 4, 'wk': 5,
    'bp': 6, 'bn': 7, 'bb': 8, 'br': 9, 'bq': 10, 'bk': 11,
}

def generate_board_image(index, board_paths, pieces_dict, output_base, split):
    """
    Generate a synthetic chess board image with random pieces.

    Args:
        index (int): Index for naming the output files.
        board_paths (list): List of paths to board images.
        pieces_dict (dict): Dictionary mapping piece types to lists of piece images.
        output_base (str): Base directory for saving output images and labels.
        split (str): Data split (e.g., 'train', 'val').

    Returns:
        None: Saves the generated image and label file to the specified output directory.
    """
    board_img_path = random.choice(board_paths)
    board_img = Image.open(board_img_path).convert("RGBA")
    board_img = board_img.resize((IMAGE_SIZE, IMAGE_SIZE))

    used_positions = set()
    piece_count = random.randint(10, 32)
    labels = []

    for _ in range(piece_count):
        piece_type = random.choice(list(pieces_dict.keys()))
        piece_img = random.choice(pieces_dict[piece_type]).resize((SQUARE_SIZE, SQUARE_SIZE))

        while True:
            row = random.randint(0, BOARD_SIZE - 1)
            col = random.randint(0, BOARD_SIZE - 1)
            if (row, col) not in used_positions:
                used_positions.add((row, col))
                break

        x = col * SQUARE_SIZE
        y = row * SQUARE_SIZE
        board_img.paste(piece_img, (x, y), mask=piece_img)

        class_id = PIECE_CLASSES.get(piece_type, -1)
        if class_id == -1:
            continue

        x_center, y_center, w_norm, h_norm = normalize_bbox(x, y, SQUARE_SIZE, SQUARE_SIZE, IMAGE_SIZE, IMAGE_SIZE)
        labels.append(f"{class_id} {x_center:.6f} {y_center:.6f} {w_norm:.6f} {h_norm:.6f}")

    filename = f"synthetic_board_{index:04d}.png"
    img_path, label_path = get_output_paths(output_base, split, filename)

    board_img.save(img_path)
    with open(label_path, "w") as f:
        f.write("\n".join(labels))
