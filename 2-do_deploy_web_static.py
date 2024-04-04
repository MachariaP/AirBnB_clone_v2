#!/usr/bin/python3
# Fabfile to distribute an archive to a web server.
import os.path
from fabric.api import env, put, run, abort

env.hosts = ["54.172.89.45", "100.25.144.184"]

def do_deploy(archive_path):
    """Distributes an archive to a web server.

    Args:
        archive_path (str): The path of the archive to distribute.
    Returns:
        If the file doesn't exist at archive_path or an error occurs - False.
        Otherwise - True.
    """
    if not os.path.exists(archive_path):
        return False

    file = os.path.basename(archive_path)
    name = file.split(".")[0]

    try:
        put(archive_path, f"/tmp/{file}")
        run(f"rm -rf /data/web_static/releases/{name}/")
        run(f"mkdir -p /data/web_static/releases/{name}/")
        run(f"tar -xzf /tmp/{file} -C /data/web_static/releases/{name}/")
        run(f"rm /tmp/{file}")
        run(f"mv /data/web_static/releases/{name}/web_static/* /data/web_static/releases/{name}/")
        run(f"rm -rf /data/web_static/releases/{name}/web_static")
        run("rm -rf /data/web_static/current")
        run(f"ln -s /data/web_static/releases/{name}/ /data/web_static/current")
    except:
        abort("An error occurred while deploying.")
        return False

    return True