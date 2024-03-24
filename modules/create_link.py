import os
import shutil

def create_desktop_file(name: str, icon_link: str, exec_command: str, add_to_desktop: bool, add_to_menu: bool):
    apps = os.path.expanduser("~/.local/share/applications/")
    desktop_file_path = apps + name + ".desktop"
    if not os.path.exists(apps):
        os.mkdir(apps)
    with open(desktop_file_path, "w") as desktop_file:
        desktop_file.write("[Desktop Entry]\n")
        desktop_file.write("Version=1.0\n")
        desktop_file.write("Type=Application\n")
        desktop_file.write("Name=" + name + "\n")
        desktop_file.write("Icon=" + icon_link + "\n")
        desktop_file.write("Exec=" + exec_command + "\n")
        desktop_file.write("Terminal=false\n")
        desktop_file.write("Categories=Utility;\n")

    if add_to_desktop:
        desktop_path = os.path.expanduser("~/Desktop/")
        shutil.copyfile(desktop_file_path, desktop_path + name + ".desktop")

    if not add_to_menu:
        os.remove(desktop_file_path)
