import os
import shutil
import sys

def parse_args():
    if len(sys.argv) < 2:
        print("Usage: python script.py <source_directory> [destination_directory]")
        sys.exit(1)

    source_dir = sys.argv[1]
    dest_dir = sys.argv[2] if len(sys.argv) > 2 else "dist"

    return source_dir, dest_dir

def copy_files_by_extension(source_dir, dest_dir):
    if not os.path.exists(dest_dir):
        try:
            os.makedirs(dest_dir)
        except OSError as e:
            print(f"Error creating directory '{dest_dir}': {e}")
            sys.exit(1)

    for root, _, files in os.walk(source_dir):
        for file in files:
            file_path = os.path.join(root, file)

            # Determine the file extension or handle dotfiles specifically
            if file.startswith('.') and '.' not in file[1:]:
                file_extension = file[1:] or "dotfiles"
            else:
                file_extension = os.path.splitext(file)[1][1:] or "no_extension"

            ext_dir = os.path.join(dest_dir, file_extension)
            if not os.path.exists(ext_dir):
                try:
                    os.makedirs(ext_dir)
                except OSError as e:
                    print(f"Error creating directory '{ext_dir}': {e}")
                    continue  # Skip to the next file

            dest_path = os.path.join(ext_dir, file)

            # Check if file already exists
            if os.path.exists(dest_path):
                print(f"File '{dest_path}' already exists. Skipping.")
                continue  # Skip copying this file

            try:
                shutil.copy2(file_path, dest_path)
                print(f"Copied {file_path} to {dest_path}")
            except (shutil.SameFileError, IOError, PermissionError) as e:
                print(f"Error copying file '{file_path}' to '{dest_path}': {e}")
                continue  # Skip to the next file

def main():
    source_dir, dest_dir = parse_args()

    if not os.path.exists(source_dir):
        print(f"Source directory '{source_dir}' does not exist.")
        sys.exit(1)

    copy_files_by_extension(source_dir, dest_dir)
    print("File copying and sorting complete.")

if __name__ == "__main__":
    main()
