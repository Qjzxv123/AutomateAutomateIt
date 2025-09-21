import os

# Root directory containing the files to list
DIRECTORY_PATH = r"C:\Users\qjzxv\Desktop\AutomateAutomateIt\Icons"


def print_all_file_names(root_dir: str) -> None:
    if not os.path.isdir(root_dir):
        print(f"Directory not found: {root_dir}")
        return

    for current_dir, dirnames, filenames in os.walk(root_dir):
        dirnames.sort()
        filenames.sort()
        for name in filenames:
            print(name.replace("T_Icon_", "").replace(".PNG","")+": { name: \'\', icon: \'"+name.lower()+"\', type: \'solid\' },")

if __name__ == "__main__":
    print_all_file_names(DIRECTORY_PATH)