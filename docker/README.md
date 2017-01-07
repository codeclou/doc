# Documentation on Docker-Images provided by codeclou 


 * [all codeclou images on Docker Hub](https://hub.docker.com/u/codeclou/)

-----

**TOC**

 * :monkey: [Using images on macOS Docker-Host](#macos)
 * :monkey: [Using images as Services with SystemD + Prepare Volume Permissions](#ubuntu-systemd)
 * :monkey: [Using images from Jenkins](#jenkins)

------

<p>&nbsp;</p>

<a id="macos"></a>
## Using images on macOS Docker-Host

When using Docker-Images on macOS the UID and GID are automatically mapped to the user running the docker container.
Usually docker can be run without sudo as non-root user, therefore you do not need an extra unpriviledged user on the Docker-Host.


------

<p>&nbsp;</p>

<a id="ubuntu-systemd"></a>
## Using images as Services with SystemD on e.g. Ubuntu 16.04 Docker-Host

For the example the [docker-pyload](https://github.com/codeclou/docker-pyload) Image is used. These recommendations come without warranty and should be seen as general recommendations. You should check if they are appropriate for yourself and fit your companies security policies.


### (1) Create unpriviliged user on Docker-Host and prepare Volume Mounts

All Docker-Images provided by codeclou and marked with 'non-root' run in non-root mode and use an user internally with UID 10777 and GID 10777.
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


------

<p>&nbsp;</p>

<a id="jenkins"></a>
## Using images from Jenkins

Add Jenkins to dockerworker group and restart jenkins.

```
adduser jenkins dockerworker
```

In your `Jenkinsfile` set permissions at start.

```
stage('Build') {
    sh 'chgrp -R dockerworker ${WORKSPACE}'
    sh 'chmod -R g+w ${WORKSPACE}'
    sh "docker run --tty -v ${WORKSPACE}/:/icons/ codeclou/docker-xml-and-svg-tools:latest bash /icons/jenkins-convert-icons.sh"
}
```

Inside your runscripts or docker-entrypoints use:

```
umask u+rxw,g+rwx,o-rwx
```
