# Govee-H6117-BLE
Covers my findings from reverse engineering some of the bluetooth packets exchanged between my phone and the Govee H6117 led strip lights. This is a simple write up containing notes and understandings of BLE and the Govee H6117 led strip.
---
## Goal
Control the light strip's _brightness, color, on/off state_ without using the _original app or Govee's developer API_.

## Device information
The Govee H6117 uses two means of communication: WiFi and Bluetooth Low energy

## Communication
The following are the service and characteristic that we are interested in if we want to change the state of the light strip.
- Opcode / write command: `0x52`
- Service UUID: `00010203-0405-0607-0809-0a0b0c0d1910`
  - Characteristic: `00010203-0405-0607-0809-0a0b0c0d2b11` (Read, Write)
    - Value: See breakdown
### Data Breakdown
The data exchanged between the client and server is a 160 bit or 20 byte data field.
Note:
- I have separated out the important parts with spaces in the following examples
- First byte - The overall mode
- Second byte - What we want to do i.e. turn off/on (`0x01`), set the brightness (`0x04`), or change the color (`0x05`) of the lights
- Last byte - XOR checksum calculated by enumerating through each byte and xoring it to the last. i.e. `0 ^ 0x33 -> 0x33 ^ 0x01 ...`
#### Off
`33 01``00``00000000000000000000000000000000``32`
#### On
`33 01``01``0000000000000000000000000000000033`


## Bluetooth Low Energy / GATT quick reference
- There are two types of UUIDs
  - 16 bit (still actually 128 bits) - Have Specific meanings - assigned by Bluetooth SIG
    - EX: `0x2A00` (Device Name) is actually `00002A00-0000-1000-8000-00805F9B34FB`. Note the `2A00` padded by 0s at the beginning. [A full list of these can be found page 61](https://www.bluetooth.com/wp-content/uploads/Files/Specification/HTML/Assigned_Numbers/out/en/Assigned_Numbers.pdf)
  - 128 bit (Vendor Specific)
- GATT
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
  - Find a packet that performs the action you intended to record and take note of the opcode. Also while you've got this packet open: If there is a value field, right click -> `Apply as Column`
  - Filter for that opcode: `btatt.opcode == opcodehere`
- Use `nRF Connect` Android app for probing

## References
- https://developerhelp.microchip.com/xwiki/bin/view/applications/ble/introduction/bluetooth-architecture/bluetooth-host-layer/bluetooth-generic-attribute-profile-gatt/Data-Organization/
- https://developerhelp.microchip.com/xwiki/bin/view/applications/ble/introduction/bluetooth-architecture/bluetooth-host-layer/bluetooth-generic-attribute-profile-gatt/UUIDs/
- https://www.bluetooth.com/wp-content/uploads/Files/Specification/HTML/Assigned_Numbers/out/en/Assigned_Numbers.pdf
- https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax
