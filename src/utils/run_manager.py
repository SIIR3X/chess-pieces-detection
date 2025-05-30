import shutil
from pathlib import Path

def clear_all_runs(runs_dir="runs/"):
    """
    Clears all runs in the specified directory.

    Args:
        runs_dir (str): Directory containing the runs to clear. Default is "runs/".
    """
    runs_path = Path(runs_dir)
    if not runs_path.exists():
        print("No runs directory found.")
        return

    for sub in runs_path.iterdir():
        if sub.is_dir():
            print(f"🗑️  Deleting: {sub}")
            shutil.rmtree(sub)

    print("✅ All runs have been cleared.")

def clear_specific_run(run_name, runs_dir="runs/"):
    """
    Clears a specific run by its name in the specified directory.

    Args:
        run_name (str): Name of the run to clear.
        runs_dir (str): Directory containing the runs. Default is "runs/".
    """
    run_path = Path(runs_dir) / run_name

    if run_path.exists() and run_path.is_dir():
        print(f"🗑️  Deleting: {run_path}")
        shutil.rmtree(run_path)
        print("✅ Run deleted.")
    else:
        print(f"❌ Run '{run_name}' not found in {runs_dir}")
