"""
This script is for photogrammetry measurements. It captures images from a phone via android debug bridge (ADB)
while rotating a Zaber rotation stage. The phone can be connected to the host computer over the wifi network.

Python Dependencies:
- zaber_motion
- pure-python-adb

Note: The adb needs to be started prior to running the script. Enter the following in a command prompt:
  adb tcpip 5555
  adb start-server
  adb connect device_ip_address:5555

To stop the server:
  adb kill-server
"""
import time
from ppadb.client import Client as AdbClient
from ppadb.device import Device as AdbDevice
from zaber_motion import Library, Units
from zaber_motion.ascii import Connection, Axis

def connect_to_phone() -> AdbDevice:
    """ Initializes the phone connection """
    print("Warning: adb server must be started first or the following will fail.")
    print("Connecting to phone...")

    # Default is "127.0.0.1" and 5037
    client = AdbClient(host="127.0.0.1", port=5037)
    devices = client.devices()

    if len(devices) == 0:
        raise RuntimeError("No phone found.")

    device = devices[0]
    print(f'Connected to {device}')
    return device


def take_photo(device: AdbDevice):
    """ Take a photo on the phone """
    # take a photo with volume up key
    device.shell('input keyevent 24')
    print(f'Captured photo on {device}')


def connect_to_stage(com_port: str, device_num: int, axis_num: int = 1) -> Axis:
    """ Connect to the specified zaber motorized stage """
    Library.enable_device_db_store()
    connection = Connection.open_serial_port(com_port)
    device_list = connection.detect_devices()
    print("Found {} Zaber Devices".format(len(device_list)))

    return device_list[device_num].get_axis(axis_num)


def run_cycle(axis: Axis, phone: AdbDevice, images_per_rotation: int, image_count: int, take_picture: bool = True):
    """ Capture a photogrammetry dataset """
    move_increment = 360.0 / images_per_rotation

    for i in range(image_count):
        print(f'Position {i + 1} of {image_count}.')

        if take_picture:
            take_photo(phone)
            time.sleep(0.25)  # Wait for a bit in case there's a delay taking the image

        axis.move_relative(move_increment, Units.ANGLE_DEGREES, True)
        time.sleep(0.25)  # Wait for vibrations to decay before capturing the image

    if take_picture:
        take_photo(phone)  # Take a photo at the final position

    print("Done")

def main(move_to_start: bool = False):
    """ Primary script method """
    phone = connect_to_phone()
    stage_axis = connect_to_stage("COM11", 0, 1)

    # We could move to a starting position here if desired.
    if move_to_start:
        stage_axis.move_absolute(10, Units.ANGLE_DEGREES, True)
        time.sleep(2)

    run_cycle(stage_axis, phone, 28, 30, True)


if __name__ == '__main__':
    main()
