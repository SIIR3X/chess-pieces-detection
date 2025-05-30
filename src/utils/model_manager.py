import os
import shutil
from ultralytics import YOLO

def get_model(model_name, models_dir="models"):
    """
    Loads or downloads a YOLO model into a dedicated models directory.

    Args:
        model_name (str): Model name or path (e.g. 'yolov8x.pt')
        models_dir (str): Directory where models are stored

    Returns:
        YOLO: Loaded YOLO model
    """
    os.makedirs(models_dir, exist_ok=True)
    model_path = os.path.join(models_dir, model_name)

    if not os.path.exists(model_path):
        print(f"📥 Downloading {model_name} to {models_dir}/...")
        model = YOLO(model_name)  # triggers download
        if os.path.exists(model_name):
            shutil.move(model_name, model_path)
        return model
    else:
        print(f"📦 Loading model from: {model_path}")
        return YOLO(model_path)
