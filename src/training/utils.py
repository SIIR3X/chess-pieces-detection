import os
import shutil
from ultralytics import YOLO

def ensure_model_local(model_name, target_dir="models"):
    """
    Downloads the pretrained model if not already in models/,
    and returns the local path.
    """
    os.makedirs(target_dir, exist_ok=True)
    local_path = os.path.join(target_dir, os.path.basename(model_name))

    if os.path.exists(local_path):
        return local_path

    print(f"📦 Downloading model: {model_name}")
    YOLO(model_name) # triggers internal download
    cache_path = os.path.expanduser(f"~/.cache/ultralytics/{model_name}")

    if os.path.exists(cache_path):
        shutil.copy(cache_path, local_path)
        print(f"✅ Copied model to: {local_path}")
        return local_path
    else:
        print("⚠️ Model not found in cache. Using default path.")
        return model_name
