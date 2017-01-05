# Documentation on Docker-Images provided by codeclou 


 * [all codeclou images on Docker Hub](https://hub.docker.com/u/codeclou/)


<p>&nbsp;</p>

------

<p>&nbsp;</p>

## Using image as Service with systemd on e.g. Ubuntu 16.04 Docker-Host

For the example the [docker-pyload](https://github.com/codeclou/docker-pyload) Image is used. These recommendations come without warranty and should be seen as general recommendations. You should check if they are appropriate for yourself and fit your companies security policies.


### (1) Create unpriviliged user on Docker-Host and prepare Volume Mounts

All Docker-Images provided by ubuntu run in non-root mode and use an user internally with UID 10777 and GID 10777.
Therefore Volumes that should be mounted need appropriate Permissions for the Docker-Container to be able to write to the directories.

Therefore we create a user called  `dockerworker` and a group called `dockerworker` on the Ubuntu Docker-Host
and set permissions for our designated Volume directories.

```
addgroup --gid 10777 dockerworker
adduser --uid 10777 --gid 10777 --no-create-home --disabled-password --disabled-login --gecos "" dockerworker
```

Set the permissions for designated Volumes.

```
mkdir -p /opt/pyload/downloads
chown -R dockerworker:dockerworker /opt/pyload/downloads
chmod -R u+rwx,g+rwx,o-rwx /opt/pyload/downloads


mkdir -p /opt/pyload/config
chown -R dockerworker:dockerworker /opt/pyload/config
chmod -R u+rwx,g+rwx,o-rwx /opt/pyload/config
```


<p>&nbsp;</p>
<p>&nbsp;</p>


### (2) Create Named Docker-Container

Create a named container. You specify the same parameters as with `run` but instead use `create --name [SERVICE_NAME]`

```bash
docker create \ 
    --name pyload \
    -v /opt/pyload/downloads:/pyload/downloads \
    -v /opt/pyload/config:/pyload/config \
    -p 8877:8000 \
    codeclou/docker-pyload:latest
```

Now your named Docker-Container can be started and stoped like this

```
docker start pyload
docker stop pyload
```


<p>&nbsp;</p>
<p>&nbsp;</p>

### (3) Create systemd config

To have your named Docker-Container started by SystemD from your Docker-Host, first create a `/etc/systemd/system/pyload.service` file with the following content.

```
[Unit]
Description=pyload container
Requires=docker.service
After=docker.service

[Service]
Restart=always
ExecStart=/usr/bin/docker start -a pyload
ExecStop=/usr/bin/docker stop -t 2 pyload
ExecStopPost=/bin/rm /opt/pyload/config/pyload.pid

[Install]
WantedBy=default.target
```

Reload Daemon, Start Docker Image and add to System Startup

```
systemctl daemon-reload
systemctl start pyload.service
systemctl enable pyload.service
```
