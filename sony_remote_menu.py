import rumps
import subprocess
import broadlink
import os
import time
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# --- Config ---
DEVICE_IP = os.environ.get("DEVICE_IP")
DEVICE_MAC = bytes.fromhex(os.environ.get("DEVICE_MAC"))
DEVICE_TYPE = int(os.environ.get("DEVICE_TYPE"), 16)
COMMANDS_DIR = os.environ.get("COMMANDS_DIR")
BLUETOOTH_MAC = os.environ.get("BLUETOOTH_MAC")

# --- IR Send Helper ---
def send_ir(name):
    path = os.path.join(COMMANDS_DIR, f"{name}.ir")
    if not os.path.exists(path):
        rumps.alert(f"IR command '{name}' not found.")
        return
    try:
        device = broadlink.gendevice(DEVICE_TYPE, (DEVICE_IP, 80), DEVICE_MAC)
        device.auth()
        with open(path, "rb") as f:
            data = f.read()
        device.send_data(data)
    except Exception as e:
        rumps.alert(f"Failed to send '{name}': {e}")

class SonyRemoteApp(rumps.App):
    def __init__(self):
        super().__init__("Sony 🎶", icon=None, menu=[
            "Start Bluetooth & Connect",
            "Power",
            "Volume Up",
            "Volume Down",
            None,
            "Volume Up 5",
            "Volume Down 5",
            None,
            "Connect Mac Bluetooth",
            None,
            "Quit"
        ])

    @rumps.clicked("Start Bluetooth & Connect")
    def start_bt(self, _):
        send_ir("power")
        time.sleep(10)
        send_ir("home")
        time.sleep(5)
        send_ir("bluetooth")
        time.sleep(5)
        send_ir("volume_up")
        send_ir("volume_up")
        time.sleep(1)
        subprocess.run(["blueutil", "--connect", BLUETOOTH_MAC])
        

    @rumps.clicked("Power")
    def power(self, _):
        send_ir("power")

    @rumps.clicked("Volume Up")
    def vol_up(self, _):
        send_ir("volume_up")

    @rumps.clicked("Volume Down")
    def vol_down(self, _):
        send_ir("volume_down")

    @rumps.clicked("Volume Up 5")
    def vol_up_5(self, _):
        send_ir("volume_up")
        send_ir("volume_up")
        send_ir("volume_up")
        send_ir("volume_up")
        send_ir("volume_up")

    @rumps.clicked("Volume Down 5")
    def vol_down_5(self, _):
        send_ir("volume_down")
        send_ir("volume_down")
        send_ir("volume_down")
        send_ir("volume_down")
        send_ir("volume_down")

    @rumps.clicked("Connect Mac Bluetooth")
    def connect_bt(self, _):
        subprocess.run(["blueutil", "--connect", BLUETOOTH_MAC])

    @rumps.clicked("Quit")
    def quit(self, _):
        rumps.quit_application()

if __name__ == "__main__":
    SonyRemoteApp().run()
