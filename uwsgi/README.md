# build docker
```
docker rmi laofuzi/demo/uwsgi-demo:1.0
./build.sh
```

# run local
```

```

# run docker
```
docker rm -fv uwsgi-demo
docker run -it --name uwsgi-demo -p 10000:10000 -e PORT=10000 laofuzi/demo/uwsgi-demo:1.0

docker rm -fv uwsgi-demo
docker run -it --name uwsgi-demo -p 10000:10000 -e PORT=10000 -e UWSGI_THREADS=2 -e UWSGI_PROCESSES=2 laofuzi/demo/uwsgi-demo:1.0
```
# test
```
curl --request POST http://localhost:10000/service
```