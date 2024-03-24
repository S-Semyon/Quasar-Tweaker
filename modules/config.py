import os
import json
from dataclasses import dataclass

if os.name == "nt":
    ABPATH = r"D:\Quasar Tweaker\tmp/"
    CONFIG_CATALOG = ABPATH + r"config/quasar_tweaker"
    CONFIG_FILE = CONFIG_CATALOG + r"/config.json"
else:
    HOME_DIR = os.getenv('HOME')
    CONFIG_PATH = os.path.join(HOME_DIR, ".config")
    CONFIG_CATALOG = os.path.join(CONFIG_PATH, 'quasar_tweaker')
    CONFIG_FILE = os.path.join(CONFIG_CATALOG, 'config.json')

if not os.path.exists(CONFIG_CATALOG):
    os.mkdir(CONFIG_CATALOG)

if not os.path.exists(CONFIG_FILE):
    data = {
        "buttons": {}
    }
    for i in range(1, 21):
        data["buttons"][f"button{i}"] = {
            "name":     f"Команда {i}",
            "command":  ""
        }
    data["buttons"]["button1"] = {
        "name": "apt-fast update",
        "command": "pkexec apt-fast -y upgrade"
    }
    data["buttons"]["button2"] = {
        "name": "apt-fast upgrade",
        "command": "pkexec apt-fast -y dist-upgrade"
    }
    data["buttons"]["button3"] = {
        "name": "apt-fast dist-upgrade",
        "command": "pkexec apt-fast -y dist-upgrade"
    }
    with open(CONFIG_FILE, "w", encoding="UTF-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


@dataclass
class Command(object):
    command_place: int
    button_name: str
    command_name: str
    command: str


def read(command_place: int) -> Command:
    with open(CONFIG_FILE, "r", encoding="UTF-8") as file:
        data = json.load(file)
    button_name = "button" + str(command_place)
    if button_name not in data["buttons"]:
        raise ValueError(command_place)
    button = data["buttons"][button_name]
    return Command(
        command_place,
        button_name,
        button["name"],
        button["command"]
    )
