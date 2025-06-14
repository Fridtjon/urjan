import broadlink
import time
import sys
import os

# --- Device Config ---
DEVICE_IP = "192.168.50.222"
DEVICE_MAC = bytes.fromhex("e87072081bcd")
LEARN_TIMEOUT = 5  # Seconds to wait for IR signal

# --- Progress Bar Helper ---
def show_progress_bar(duration_secs):
    total_steps = 100
    step_duration = duration_secs / total_steps
    for i in range(total_steps + 1):
        bar = "#" * (i // 2)
        spaces = " " * (50 - len(bar))
        print(f"\r[{bar}{spaces}] {i}%", end='', flush=True)
        time.sleep(step_duration)
    print()  # Move to next line after done

# --- Check for argument ---
if len(sys.argv) != 2:
    print("Usage: python3 learn_ir.py <command_name>")
    sys.exit(1)

command_name = sys.argv[1]
output_dir = "commands"
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, f"{command_name}.ir")

# --- Connect to device ---
device = broadlink.gendevice(0x5f36, (DEVICE_IP, 80), DEVICE_MAC)
device.auth()

# --- Learn IR ---
print(f"📡 Ready to learn '{command_name}' IR signal.")
print("👉 Point your remote at the BroadLink and press the button during the progress bar:")

device.enter_learning()
show_progress_bar(LEARN_TIMEOUT)

print("⏳ Attempting to read signal...")

try:
    ir_packet = device.check_data()
    with open(output_path, "wb") as f:
        f.write(ir_packet)
    print(f"✅ Successfully saved '{command_name}' to {output_path}")
except Exception as e:
    print("❌ Error learning IR command:", e)
