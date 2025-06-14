import broadlink
import sys
import os

# --- Device Config ---
DEVICE_IP = "192.168.50.222"
DEVICE_MAC = bytes.fromhex("e87072081bcd")

# --- Check for argument ---
if len(sys.argv) != 2:
    print("Usage: python3 send_ir.py <command_name>")
    sys.exit(1)

command_name = sys.argv[1]
input_path = os.path.join("commands", f"{command_name}.ir")

# --- Load IR packet ---
if not os.path.exists(input_path):
    print(f"❌ IR command '{command_name}' not found in {input_path}")
    sys.exit(1)

with open(input_path, "rb") as f:
    ir_packet = f.read()

# --- Connect to device ---
device = broadlink.gendevice(0x5f36, (DEVICE_IP, 80), DEVICE_MAC)
device.auth()

# --- Send IR ---
device.send_data(ir_packet)
print(f"✅ Sent IR command '{command_name}'")
