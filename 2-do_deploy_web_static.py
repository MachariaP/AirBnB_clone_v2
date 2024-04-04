#!/usr/bin/env python3
from fabric import Connection
from fabric import task
import os


env.hosts = ['54.172.89.45', '100.25.144.184']


@task
def do_deploy(c, archive_path):
    if not os.path.exists(archive_path):
        return False

    try:
        archive_name = os.path.basename(archive_path)
        archive_name_without_ext = archive_name.split('.')[0]

        c.put(archive_path, '/tmp/')
        c.run('mkdir -p /data/web_static/releases/{}/'
              .format(archive_name_without_ext))
        c.run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'
              .format(archive_name, archive_name_without_ext))
        c.run('rm /tmp/{}'.format(archive_name))
        c.run('rm -rf /data/web_static/current')
        c.run('ln -s /data/web_static/releases/{}/ /data/web_static/current'
              .format(archive_name_without_ext))
        print("New version deployed!")
        return True
    except Exception:
        return False
