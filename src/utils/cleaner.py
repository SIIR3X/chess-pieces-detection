import shutil
from tqdm import tqdm
from pathlib import Path

def clear_subfolders_content(parent_folder):
    """
    Clears the content of all subfolders in the given parent folder,
    without deleting the subfolders themselves.
    """
    parent = Path(parent_folder)
    if not parent.exists():
        print(f"⚠️  Parent folder does not exist: {parent}")
        return

    for subfolder in parent.iterdir():
        if subfolder.is_dir():
            print(f"🗑️  Clearing subfolder: {subfolder}")
            
            for item in tqdm(list(subfolder.iterdir()), desc=f"Clearing {subfolder}"):
                try:
                    if item.is_file():
                        item.unlink()
                    elif item.is_dir():
                        for subitem in item.rglob("*"):
                            if subitem.is_file():
                                subitem.unlink()
                        item.rmdir()
                except Exception as e:
                    print(f"❌ Error deleting {item}: {e}")
