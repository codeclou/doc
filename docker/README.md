# Docker-Images provided by codeclou 


[ALL codeclou DOCKER IMAGES](https://hub.docker.com/u/codeclou/)

## General Usage recommendations

## Using image as Service with systemd on e.g. Ubuntu 16.04 Docker-Host

For the example the [docker-pyload](https://github.com/codeclou/docker-pyload) Image is used.


### (1) Create unpriviliged user on Docker-Host and prepare Volume Mounts


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
