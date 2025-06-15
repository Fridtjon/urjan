# Urjan

A macOS menu bar application for controlling Sony devices using IR commands via Broadlink.

## Features

- Control Sony devices through IR commands
- Bluetooth device management
- Volume control
- Power management

## Requirements

- Python 3.x
- Broadlink device
- macOS
- blueutil (for Bluetooth control)

## Installation

### For Users
1. Download the latest release from the Releases page
2. Move `Urjan.app` to your Applications folder
3. Install blueutil:
   ```bash
   brew install blueutil
   ```
4. Create a `.env` file in the app bundle:
   ```bash
   # Right-click Urjan.app and select "Show Package Contents"
   # Navigate to Contents/Resources
   # Create .env file with your configuration:
   DEVICE_IP=your_broadlink_ip
   DEVICE_MAC=your_broadlink_mac
   DEVICE_TYPE=your_device_type
   COMMANDS_DIR=commands
   BLUETOOTH_MAC=your_sony_device_mac
   ```

### For Developers
1. Clone this repository
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
3. Install required Python packages:
   ```bash
   pip install -r requirements.txt
   ```
4. Install blueutil:
   ```bash
   brew install blueutil
   ```
5. Create a `.env` file in the project root with your configuration:
   ```
   DEVICE_IP=your_broadlink_ip
   DEVICE_MAC=your_broadlink_mac
   DEVICE_TYPE=your_device_type
   COMMANDS_DIR=commands
   BLUETOOTH_MAC=your_sony_device_mac
   ```

## Building the App

1. Make sure you're in the virtual environment:
   ```bash
   source venv/bin/activate
   ```

2. Build the app using PyInstaller:
   ```bash
   pyinstaller --name Urjan \
               --windowed \
               --add-data "commands:commands" \
               --add-data ".env:." \
               sony_remote_menu.py
   ```
   * `--windowed`: Creates a proper app bundle without a console window.
   * `--add-data`: Bundles the `commands` directory and your `.env` file.

The final app will be in the `dist` directory.

## Running the App

### Development Mode
```bash
python sony_remote_menu.py
```

### Standalone App
```bash
open dist/Urjan.app
```

The application will appear in your macOS menu bar.

## Troubleshooting

1. If the app doesn't appear in the menu bar:
   - Check that the `.env` file is properly configured
   - Verify that blueutil is installed
   - Check the system logs for any errors

2. If IR commands don't work:
   - Verify your Broadlink device is on the same network
   - Check that the IR command files exist in the commands directory
   - Verify the device IP and MAC address in the `.env` file

3. If Bluetooth doesn't work:
   - Make sure blueutil is installed
   - Verify the Bluetooth MAC address in the `.env` file
   - Check that your Sony device is in pairing mode 