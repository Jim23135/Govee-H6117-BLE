# Govee-H6117-BLE
Covers my findings from reverse engineering some of the bluetooth packets exchanged between my phone and the Govee H6117 led strip lights. This barbones write up is meant to bring you (or me) up to speed on the basics of communicating with this specefic light strip.

## Goal
Control the light strip's _brightness, color, on/off state_ without using the _original app or Govee's developer API_.

## Device information
The Govee H6117 uses two means of communication: WiFi and Bluetooth Low energy

## Bluetooth Low Energy / GATT quick reference
There are two types of UUIDs
- 16 bit (still actually 128 bits) - Have specefic meanings - assigned by Bluetooth SIG
  - EX: `0x2A00` (Device Name) is actually `00002A00-0000-1000-8000-00805F9B34FB`. Note the `2A00` padded by 0s at the beginning. [A full list of these can be found page 61](https://www.bluetooth.com/wp-content/uploads/Files/Specification/HTML/Assigned_Numbers/out/en/Assigned_Numbers.pdf)
- Bluetooth device
  - Service 1
    - Characteristic 1
      - Descriptor
      - Descriptor
  - Characteristic 2
      - Descriptor
 - Service 2
   - Characteristic 1
     - Descriptor

## Miscellaneous
- Best way to log packets:
  - On Android, in `Developer options`, set `Enable Bluetooth HCI snoop log` to `Enabled`
  - Turn on Bluetooth and perform the actions that you want to log
  - Turn off Bluetooth
  - Use `adb bugreport` to download the Bluetooth log from your Android phone
  - Find `btsnoop_hci.log` in `bugreport.zip` and plug the log file into Wireshark
  - Filter in Wireshark for `btatt`
  - Find a packet that does the action you intended to record and take note of the opcode
  - Filter for that opcode: `btatt.opcode == opcodehere`

## References
- https://developerhelp.microchip.com/xwiki/bin/view/applications/ble/introduction/bluetooth-architecture/bluetooth-host-layer/bluetooth-generic-attribute-profile-gatt/Data-Organization/
- https://developerhelp.microchip.com/xwiki/bin/view/applications/ble/introduction/bluetooth-architecture/bluetooth-host-layer/bluetooth-generic-attribute-profile-gatt/UUIDs/
- https://www.bluetooth.com/wp-content/uploads/Files/Specification/HTML/Assigned_Numbers/out/en/Assigned_Numbers.pdf
- https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax
