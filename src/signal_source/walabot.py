from __future__ import print_function  # WalabotAPI works on both Python 2 an 3.
from sys import platform
from os import system
from imp import load_source
from os.path import join
import time
import csv

if platform == 'win32':
    modulePath = join('C:/', 'Program Files', 'Walabot', 'WalabotSDK',
                      'python', 'WalabotAPI.py')
elif platform.startswith('linux'):
    modulePath = join('/usr', 'share', 'walabot', 'python', 'WalabotAPI.py')

wlbt = load_source('WalabotAPI', modulePath)
wlbt.Init()
codeDataTime = []
duration_time = 0
if_read_all = False


def set_if_read_all(flag):
    global if_read_all
    if_read_all = flag


def PrintSensorTargets(targets):
    system('cls' if platform == 'win32' else 'clear')
    if targets:
        for i, target in enumerate(targets):
            print('Target #{}:\nx: {}\ny: {}\nz: {}\namplitude: {}\n'.format(
                i + 1, target.xPosCm, target.yPosCm, target.zPosCm,
                target.amplitude))
    else:
        print('No Target Detected')


def savesignalfile(a):
    with open("Data.csv", "w") as datafile:
        datafilewirte = csv.writer(datafile)
        for signalx in zip(a):
            # data = '{}\n'.format(signalx)
            datafilewirte.writerow(a)


def PrintResults(targets):
    system('cls' if platform == 'win32' else 'clear')
    if targets:
        for i, target in enumerate(targets):
            print('Target #{}:\nx: {}\ny: {}\nz: {}\namplitude: {}\n'.format(
                i + 1, target.xPosCm, target.yPosCm, target.zPosCm,
                target.amplitude))
    else:
        print('No Target Detected')


def SensorApp():
    codeData = []
    # wlbt.SetArenaR - input parameters
    minInCm, maxInCm, resInCm = 30, 200, 3
    # wlbt.SetArenaTheta - input parameters
    minIndegrees, maxIndegrees, resIndegrees = -15, 15, 3
    # wlbt.SetArenaPhi - input parameters
    minPhiInDegrees, maxPhiInDegrees, resPhiInDegrees = -45, 45, 5
    # Set MTI mode
    mtiMode = False
    # Configure Walabot database install location (for windows)
    wlbt.SetSettingsFolder()
    # 1) Connect : Establish communication with walabot.
    wlbt.ConnectAny()
    # 2) Configure: Set scan profile and arena
    # Set Profile - to Sensor.
    wlbt.SetProfile(wlbt.PROF_SENSOR)
    # Setup arena - specify it by Cartesian coordinates.
    wlbt.SetArenaR(minInCm, maxInCm, resInCm)
    # Sets polar range and resolution of arena (parameters in degrees).
    wlbt.SetArenaTheta(minIndegrees, maxIndegrees, resIndegrees)
    # Sets azimuth range and resolution of arena.(parameters in degrees).
    wlbt.SetArenaPhi(minPhiInDegrees, maxPhiInDegrees, resPhiInDegrees)
    global incrementer
    incrementer = 0
    # 3) Start: Start the system in preparation for scanning.
    wlbt.Start()
    t0 = time.time()
    if not mtiMode:  # if MTI mode is not set - start calibrartion
        # calibrates scanning to ignore or reduce the signals
        wlbt.StartCalibration()
        while wlbt.GetStatus()[0] == wlbt.STATUS_CALIBRATING:
            wlbt.Trigger()
    while int(time.time() - t0) <= duration_time:

        wlbt.Trigger()
        Antenna = wlbt.GetAntennaPairs()
        I = Antenna[11]
        signal = wlbt.GetSignal(I)
        if if_read_all == False:
            codeData.append(signal[0][0])
        else:
            codeData.append(signal[0])
        # codeDataTime.append(signal[1])
        incrementer += 1

    # 7) Stop and Disconnect.
    print('The sample number is:', incrementer)
    wlbt.Stop()
    wlbt.Disconnect()
    return codeData


def get_sample_rate():
    return incrementer / duration_time


if __name__ == '__main__':
    SensorApp()
