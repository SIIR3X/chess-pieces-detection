import os
import shutil
import yaml
from ultralytics import YOLO

from src.utils.model_manager import get_model
from src.training.utils import ensure_model_local

def load_config(config_path):
    """
    Loads the training configuration from a YAML file.

    Args:
        config_path (str): Path to the YAML configuration file.

    Returns:
        dict: Parsed configuration dictionary.
    """
    with open(config_path, "r") as f:
        return yaml.safe_load(f)

def run_training(config_path):
    """
    Runs the YOLO training process based on the provided configuration.

    Args:
        config_path (str): Path to the YAML configuration file.
    """
    config = load_config(config_path)
    print("📖 Loaded configuration:")
    for k, v in config.items():
        print(f"  {k}: {v}")

    model_path = ensure_model_local(config["model"])
    model = get_model(config["model"])

    print("🚀 Starting training...")
    model.train(
        data=config["data"],
        epochs=config.get("epochs", 50),
        batch=config.get("batch", 16),
        imgsz=config.get("imgsz", 512),
        device=config.get("device", "0"),
        name=config.get("name", "yolo-run"),
        save=True,
        verbose=True,
        cache='disk',
        auto_augment='none',
        augment=False,
    )

    print("✅ Training complete. Running validation...")
    metrics = model.val()
    print(f"📊 Metrics:\n{metrics}")

    if export_format := config.get("export_format"):
        model.export(format=export_format)
        print(f"📦 Model exported to {export_format}")
