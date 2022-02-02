from __future__ import print_function

import logging
import os
import subprocess
import sys
import datetime
import time

import gphoto2 as gp


def capture(p_output):
    logging.basicConfig(
        format='%(levelname)s: %(name)s: %(message)s', level=logging.WARNING)
    p_output = '/tmp/camtest/'
    camera = gp.Camera()
    camera.init()
    file_path = camera.capture(gp.GP_CAPTURE_IMAGE)
    print('Camera file path: {0}/{1}'.format(file_path.folder, file_path.name))
    print(file_path.name)
    print (os.path.isdir(p_output))
    if os.path.isdir(p_output) != True:
        os.path.mkdir(p_output)
    #create destination folder if folder does not exsist
    target = os.path.join(p_output, file_path.name)
    print('Copying image to', target)
    camera_file = camera.file_get(
        file_path.folder, file_path.name, gp.GP_FILE_TYPE_NORMAL)
    #grab file from camera
    camera_file.save(target)
    d_date = datetime.date.today()
    n_time = time.strftime("%H:%M:%S")
    os.rename(target, "/tmp/camtest/" + d_date.strftime("%m.%d.%Y.") + n_time + ".jpg")
    #this code will take a picture and then rename it to the date and time month.day.year.hour.minute.second
    #also this code has an issue with repeated captures and high exposure times why is that?

def main():
    output = "/tmp/camtest/"
    capture(output)

main()
