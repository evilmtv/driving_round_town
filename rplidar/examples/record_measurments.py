#!/usr/bin/env python3
'''Records measurments to a given file. Usage example:

$ ./record_measurments.py out.txt'''
import sys
from rplidar import RPLidar
import numpy as np
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
polygon = Polygon([(-0.2, 0), (0.2, 0), (0.5, 0.5), (0.5, 1), (-0.5, 1), (-0.5, 0.5)])

PORT_NAME = 'COM3'


def run():
    '''Main function'''
    lidar = RPLidar(PORT_NAME)
    try:
        print('Recording measurements... Press Crl+C to stop.')
        '''
        new_scan : bool
            True if measurment belongs to a new scan
        quality : int
            Reflected laser pulse strength
        angle : float
            The measurment heading angle in degree unit [0, 360)
        distance : float
            Measured object distance related to the sensor's rotation center.
            In millimeter unit. Set to 0 when measurment is invalid.
        '''
        count = 0
        obstruction_flag = False
        obstruction_list = []
        for measurement in lidar.iter_measurments():
            count += 1
            # print(measurement)
            x=measurement[3]*np.cos(np.deg2rad(measurement[2]))
            y=measurement[3]*np.sin(np.deg2rad(measurement[2]))
            point = Point(x/1000, y/1000)
            if(polygon.contains(point)):
                obstruction_flag = True
                # print(x,y)
                obstruction_list.append((x,y))
            if (measurement[0] is True):
                if(obstruction_flag is True):
                    print("Obstruction detected at " + str(len(obstruction_list)) + " points!")
                    # print(obstruction_list)
                    obstruction_flag = False
                    obstruction_list = []
                else:
                    print("No obstruction detected.")
                # raise KeyboardInterrupt
                # print(count)
                pass
            # line = '\t'.join(str(v) for v in measurment)
            # print(line)
            # outfile.write(line + '\n')
    except KeyboardInterrupt:
        print('Stoping.')
    lidar.stop()
    lidar.stop_motor()
    import time
    time.sleep(5)
    lidar.disconnect()
    print("Stopped")
    # outfile.close()


if __name__ == '__main__':
    run()
