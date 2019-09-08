#!/usr/bin/env python3
'''Animates distances and measurment quality'''
from rplidar import RPLidar
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation


# import os
# import sys
# global myportnumber
# myportnumber = "0"
# if sys.platform == "win32":
#         # To see if COMx exists.
#         os.system("MODE.COM")
#         # If only one does then this will be yours.
#         # If more than one exists, remove your unit from the USB port.
#         raw_input("Remove the USB-Serial adaptor from the port then press ENTER:- ")
#         os.system("MODE.COM")
#         # Now find out which number does not exist and that is yours also.
#         # Replace the adaptor back into the same port as it came out of.
#         # myportnumber = raw_input("ENTER the number ONLY of your adaptor and press RETURN:- ")
#         # Now set up the port to RAW and say 1200 bps.
#         # NOTE:- The whitespaces must be adhered to.
#         os.system("MODE COM"+myportnumber+": BAUD=1200 PARITY=N DATA=8 STOP=1 to=on")
# exit()
PORT_NAME = 'COM3'
DMAX = 4000
IMIN = 0
IMAX = 50

def update_line(num, iterator, line):
    scan = next(iterator)
    offsets = np.array([(np.radians(meas[1]), meas[2]) for meas in scan])
    line.set_offsets(offsets)
    intens = np.array([meas[0] for meas in scan])
    line.set_array(intens)
    return line,

def run():
    lidar = RPLidar(PORT_NAME)
    fig = plt.figure()
    ax = plt.subplot(111, projection='polar')
    line = ax.scatter([0, 0], [0, 0], s=5, c=[IMIN, IMAX],
                           cmap=plt.cm.Greys_r, lw=0)
    ax.set_rmax(DMAX)
    ax.grid(True)

    iterator = lidar.iter_scans()
    ani = animation.FuncAnimation(fig, update_line,
        fargs=(iterator, line), interval=50)
    plt.show()
    lidar.stop()
    lidar.disconnect()

if __name__ == '__main__':
    run()
