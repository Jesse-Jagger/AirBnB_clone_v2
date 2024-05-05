#!/usr/bin/python3
# Keep it clean!

import os
from fabric.api import *
from datetime import datetime

env.hosts = ['54.236.125.12', '52.90.23.24']


def do_clean(number=0):
    """ Deletes out-of-date archives """

    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(i)) for i in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [i for i in archives if "web_static_" in i]
        [archives.pop() for j in range(number)]
        [run("rm -rf ./{}".format(i)) for i in archives]
