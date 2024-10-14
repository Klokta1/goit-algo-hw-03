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

def copy_files_recursively(source_dir, dest_dir):
    if not os.path.exists(dest_dir):
        try:
            os.makedirs(dest_dir)
        except OSError as e:
            print(f"Error creating directory '{dest_dir}': {e}")
            sys.exit(1)

    try:
        for item in os.listdir(source_dir):
            source_path = os.path.join(source_dir, item)

            if os.path.isdir(source_path):
                copy_files_recursively(source_path, dest_dir)

            elif os.path.isfile(source_path):
                if item.startswith('.') and '.' not in item[1:]:
                    file_extension = item[1:] or "dotfiles"
                else:
                    file_extension = os.path.splitext(item)[1][1:] or "no_extension"

                ext_dir = os.path.join(dest_dir, file_extension)
                if not os.path.exists(ext_dir):
                    try:
                        os.makedirs(ext_dir)
                    except OSError as e:
                        print(f"Error creating directory '{ext_dir}': {e}")
                        continue

                dest_path = os.path.join(ext_dir, item)

                if os.path.exists(dest_path):
                    print(f"File '{dest_path}' already exists. Skipping.")
                    continue

                try:
                    shutil.copy2(source_path, dest_path)
                    print(f"Copied {source_path} to {dest_path}")
                except (shutil.SameFileError, IOError, PermissionError) as e:
                    print(f"Error copying file '{source_path}' to '{dest_path}': {e}")
                    continue
    except OSError as e:
        print(f"Error accessing directory '{source_dir}': {e}")

def main():
    source_dir, dest_dir = parse_args()

    if not os.path.exists(source_dir):
        print(f"Source directory '{source_dir}' does not exist.")
        sys.exit(1)

    copy_files_recursively(source_dir, dest_dir)
    print("File copying and sorting complete.")

if __name__ == "__main__":
    main()
