def normalize_bbox(x, y, w, h, img_w, img_h):
    """
    Normalize bounding box coordinates to YOLO format.
    
    Args:
        x (int): X coordinate of the top-left corner.
        y (int): Y coordinate of the top-left corner.
        w (int): Width of the bounding box.
        h (int): Height of the bounding box.
        img_w (int): Width of the image.
        img_h (int): Height of the image.
    
    Returns:
        tuple: Normalized center x, center y, width, and height.
    """
    x_center = (x + w / 2) / img_w
    y_center = (y + h / 2) / img_h
    return x_center, y_center, w / img_w, h / img_h
