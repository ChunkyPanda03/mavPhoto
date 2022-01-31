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
    p_output = "/tmp/camtest/"
    camera = gp.Camera()
    camera.init()
    file_path = camera.capture(gp.GP_CAPTURE_IMAGE)
   # file_name = gp.gp_file_set_name(file_path, datetime.date.strftime('%m.%d.%Y.%X'))
   # print(file_name)
    print('Camera file path: {0}/{1}'.format(file_path.folder, file_path.name))
    print(file_path.name)
   # if not os.path.isfile(p_output):
   #     os.mkdir(p_output)
    target = os.path.join(p_output, file_path.name)
    print('Copying image to', target)
    camera_file = camera.file_get(
        file_path.folder, file_path.name, gp.GP_FILE_TYPE_NORMAL)
    camera_file.save(target)
    d_Time = datetime.date.today()
    os.rename(target, "/tmp/camtest/" + d_Time.strftime('%m.%d.%Y.%X') + ".jpg")

def main():
    output = "/tmp/camtest/"
    capture(output)

main()