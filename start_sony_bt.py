import broadlink
import subprocess
import time
import os

# --- Device Config ---
DEVICE_IP = "192.168.50.222"
DEVICE_MAC = bytes.fromhex("e87072081bcd")

COMMANDS_DIR = "commands"
DEVICE_TYPE = 0x5f36  # Update if needed
BLUETOOTH_MAC = "d8-0f-99-08-3e-a4" # BDV-N5200W


# --- IR Send Function ---
def send_ir(name):
    path = os.path.join(COMMANDS_DIR, f"{name}.ir")
    if not os.path.exists(path):
        print(f"❌ IR command '{name}' not found.")
        return
    with open(path, "rb") as f:
        packet = f.read()
    device.send_data(packet)
    print(f"📡 Sent: {name}")

# --- Setup BroadLink device ---
device = broadlink.gendevice(DEVICE_TYPE, (DEVICE_IP, 80), DEVICE_MAC)
device.auth()

# --- Send IR commands ---
send_ir("power")
time.sleep(10)  # Wait for Sony to boot up

send_ir("home")
time.sleep(5)

send_ir("bluetooth")
time.sleep(3)

send_ir("volume_down")
time.sleep(0.5)
send_ir("volume_up")

# --- Connect Mac via Bluetooth ---
print("🔗 Connecting to Sony Bluetooth from Mac...")
subprocess.run(["blueutil", "--connect", BLUETOOTH_MAC])
print("✅ Bluetooth connected.")
