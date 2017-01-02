# Create Badges


### Generate

Generate Badges like this then add, commit and push.

```
docker run \
    -i -t \
    -v $(pwd)/input/:/pyapp/web \
    -v $(pwd)/generated/:/pyapp/data \
    codeclou/docker-python-web:latest \
    python cli.py
```


### Usage

**All Badged: [index.html](https://codeclou.github.io/doc/badges/generated/)**

Use:

```
![](https://codeclou.github.io/doc/badges/generated/docker-image-size-20.svg)	
```