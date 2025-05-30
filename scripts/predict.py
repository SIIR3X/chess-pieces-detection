import argparse
from pathlib import Path
from ultralytics import YOLO

def parse_args():
    """
    Parse command line arguments for running inference with a trained YOLOv8 model.
    
    Returns:
        argparse.Namespace: Parsed command line arguments.
    """
    parser = argparse.ArgumentParser(description="Run inference with a trained YOLOv8 model")
    parser.add_argument("--model", type=str, required=True, help="Path to trained model .pt file")
    parser.add_argument("--source", type=str, required=True, help="Image or folder path for prediction")
    parser.add_argument("--output", type=str, default="predictions/", help="Folder to save predictions")
    parser.add_argument("--conf", type=float, default=0.25, help="Confidence threshold")
    parser.add_argument("--show", action="store_true", help="Display predictions with OpenCV")
    return parser.parse_args()

def main():
    args = parse_args()

    # Load model
    model = YOLO(args.model)

    # Run prediction
    results = model.predict(
        source=args.source,
        conf=args.conf,
        save=True,
        save_txt=True,
        project=args.output,
        name="",
        show=args.show,
        imgsz=512
    )

    print(f"✅ Predictions saved to: {args.output}")

if __name__ == "__main__":
    main()
