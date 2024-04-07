#!/usr/bin/python3
""" script that distributes an archive to the web servers """

from fabric.api import *
import os


def do_deploy(archive_path):
    """ function to deploy an archive """
    if !(os.path.exists(archive_path)):
        return False
    try:
        put(archive_path, '/tmp/')
        f_ext = archive_path.split('/', -1)
        f_name = file_ext.split('.', 0)
        data_path = '/data/web_static/release/'
        run('mkdir -p {}/{}'.format(data_path, f_name))
        run('tar -xzf /tmp/{} -C {}{}/'.format(f_ext, data_path, f_name))
        run('rm /tmp/{}'.format(f_ext))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(data_path, f_name))
        run('rm -rf {}{}/web_static'.format(data_path, f_name))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(data_path, f_name))
        return True
    except Exception as e:
        return False
