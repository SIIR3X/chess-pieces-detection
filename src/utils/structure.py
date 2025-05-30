import os

def get_output_paths(output_base, split, filename):
    """
    Generate paths for saving images and labels.

    Args:
        output_base (str): Base output directory.
        split (str): Data split (e.g., 'train', 'val').
        filename (str): Name of the file to save.

    Returns:
        tuple: Paths for the image and label files.
    """
    image_dir = os.path.join(output_base, split, "images")
    label_dir = os.path.join(output_base, split, "labels")
    
    os.makedirs(image_dir, exist_ok=True)
    os.makedirs(label_dir, exist_ok=True)
    
    return os.path.join(image_dir, filename), os.path.join(label_dir, filename.replace(".png", ".txt"))
