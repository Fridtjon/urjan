import broadlink

devices = broadlink.discover(timeout=5)

if not devices:
    print("No devices found.")
else:
    for dev in devices:
        print("Device found at", dev.host)
        print("MAC:", dev.mac.hex())
