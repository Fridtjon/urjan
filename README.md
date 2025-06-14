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

1. Clone this repository
2. Install required Python packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Install blueutil:
   ```bash
   brew install blueutil
   ```

## Configuration

Update the following variables in `sony_remote_menu.py`:
- `DEVICE_IP`: Your Broadlink device IP
- `DEVICE_MAC`: Your Broadlink device MAC address
- `BLUETOOTH_MAC`: Your Sony device's Bluetooth MAC address

## Usage

Run the application:
```bash
python sony_remote_menu.py
```

The application will appear in your macOS menu bar. 