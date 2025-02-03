import time
from ppadb.client import Client as AdbClient
from zaber_motion import Library
from zaber_motion.ascii import Connection
from zaber_motion import Units

def connectPhone():
    # Need too send following commands in cmd:
    # adb tcpip 5555
    # adb start-server
    # adb connect device_ip_address:5555
    # to stop: adb kill-server

    client = AdbClient(host="127.0.0.1", port=5037) # Default is "127.0.0.1" and 5037
    devices = client.devices()

    if len(devices) == 0:
        print('No devices')
        quit()

    device = devices[0]

    print(f'Connected to {device}')

    return device, client

def takePhoto(phone):
    # take a photo with volume up
    phone.shell('input keyevent 24')
    print(f'Captured photo on {phone}')

def connectZaber(comPort, deviceNum):
    Library.enable_device_db_store()

    connection = Connection.open_serial_port(comPort)
    device_list = connection.detect_devices()
    print("Found {} Zaber Device".format(len(device_list)))

    return connection, device_list[deviceNum]

def runCycle(axis, phone, imagesPerCircle, iterations, afterMoveSleep, afterPhotoSleep, takePicture = True):

    increment = 360.0 / imagesPerCircle

    for i in range(iterations):

        print(f'Position {i + 1} of {iterations}')

        if takePicture:
            takePhoto(phone)
            time.sleep(afterPhotoSleep)

        axis.move_relative(increment, Units.ANGLE_DEGREES, True)
        time.sleep(afterMoveSleep)

    if takePicture:
        takePhoto(phone)

    print("Done")




if __name__ == '__main__':
    phone, client = connectPhone()
    connection, zaberDevice = connectZaber("COM11", 0)
    axis = zaberDevice.get_axis(1)
    #axis.move_relative(10, Units.ANGLE_DEGREES, True)
    time.sleep(2)
    runCycle(axis, phone, 28, 30, 0.25, 0.25, True)