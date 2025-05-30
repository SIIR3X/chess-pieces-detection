import os
import glob
from PIL import Image

def load_piece_images(piece_dir):
    """
    Load piece images from the specified directory.

    Args:
        piece_dir (str): Path to the directory containing piece images.

    Returns:
        dict: A dictionary where keys are piece types (e.g., 'wp', 'bp') and values are lists of PIL Image objects.
    """
    piece_dict = {}
    piece_types = [d for d in os.listdir(piece_dir) if os.path.isdir(os.path.join(piece_dir, d))]

    for piece_type in piece_types:
        path = os.path.join(piece_dir, piece_type, '*.png')

        image_paths = glob.glob(path)
        images = []
        for image_path in image_paths:
            try:
                img = Image.open(image_path).convert("RGBA")
                images.append(img)
            except Exception as e:
                print(f"Error loading image {image_path}: {e}")
        
        if images:
            piece_dict[piece_type] = images

    return piece_dict

def load_board_images(board_dir):
    """
    Load board images from the specified directory.

    Args:
        board_dir (str): Path to the directory containing board images.

    Returns:
        list: A list of file paths to the board images.
    """
    paths = glob.glob(os.path.join(board_dir, '*.png'))
    return [p for p in paths if os.path.isfile(p)]
