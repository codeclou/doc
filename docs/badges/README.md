# Create Badges

Generate Badges like this then add, commit and push.

```
docker run \
    -i -t \
    -v $(pwd)/input/:/pyapp/web \
    -v $(pwd)/generated/:/pyapp/data \
    codeclou/docker-python-web:latest \
    python cli.py
```
