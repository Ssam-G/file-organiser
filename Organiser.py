import os
import shutil

# Simple file organiser script

def organise_folder(folder_path: str) -> None:
    if not os.path.isdir(folder_path):
        print("That path is not a folder. Check it and try again.")
        return

    items = os.listdir(folder_path)

    moved = 0
    skipped = 0
    skipped_file = 0

    for name in items:
        full_path = os.path.join(folder_path, name)

        # Skip folders (we only want to move files)
        if os.path.isdir(full_path):
            skipped += 1
            continue

        # Get file extension
        _, ext = os.path.splitext(name)
        ext = ext.lower().strip(".")

        # Files like "README" have no extension
        if ext == "":
            ext = "no_extension"

        destination_folder = os.path.join(folder_path, ext)
        destination_path = os.path.join(destination_folder, name)

        # Skip if file already exists in the destination folder
        if os.path.exists(destination_path):
            print(f"File {name} already exists in {ext} folder. \nSkipping.")
            skipped_file += 1
            continue

        # Create the destination folder if it doesn't exist
        os.makedirs(destination_folder, exist_ok=True)

        shutil.move(full_path, destination_path)
        moved += 1


    print(f"Done. \nMoved {moved} file(s). \nSkipped {skipped_file} file(s). \nSkipped {skipped} folder(s).")


if __name__ == "__main__":
    target = input("Enter the folder path to organise: ").strip()
    organise_folder(target)
