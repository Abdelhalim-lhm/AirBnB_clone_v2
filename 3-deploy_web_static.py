#!/usr/bin/python3
""" script that create an archive and
    distributes it to the web servers
"""

from fabric.api import *
from datetime import datetime
import os
env.hosts = ['18.210.15.71', '54.157.136.110']


def do_pack():
    """ function to make an achive """

    time = datetime.now().strftime("%Y%m%d%H%M%S")
    f_name = 'versions/web_static_' + time + '.tgz'
    if os.path.isdir("versions") is False:
        local("mkdir versions")
    archive = local('tar -cvzf {} web_static'.format(f_name))
    if archive.succeeded:
        return f_name
    else:
        return None


def do_deploy(archive_path):
    """ function to deploy an archive """
    if not os.path.exists(archive_path):
        return False
    try:
        put(archive_path, '/tmp/')
        f_ext = archive_path.split('/')[-1]
        f_name = f_ext.split('.')[0]
        data_path = '/data/web_static/releases/'
        run('mkdir -p {}{}/'.format(data_path, f_name))
        run('tar -xzf /tmp/{} -C {}{}/'.format(f_ext, data_path, f_name))
        run('rm /tmp/{}'.format(f_ext))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(data_path, f_name))
        run('rm -rf {}{}/web_static'.format(data_path, f_name))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(data_path, f_name))
        print('New version deployed!')
        return True
    except:
        return False


def deploy():
    """ function to distrubute an archive """

    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
