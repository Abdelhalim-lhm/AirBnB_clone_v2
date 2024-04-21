#!/usr/bin/python3
""" Fabric script that generates a .tgz
    archive from the contents of the web_static
"""

from fabric.api import *
from datetime import datetime


def do_pack():
    """ function to make an achive """

    time = datetime.now().strftime("%Y%m%d%H%M%S")
    name = 'web_static_' + time + '.tgz'
    local('mkdir -p versions')
    archive = local('tar -cvzf versions/{} web_static'.format(name))
    if archive.succeeded:
        return name
    else:
        return None
