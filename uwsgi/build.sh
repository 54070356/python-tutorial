#!/bin/bash
REPO=laofuzi
PROJECT=demo
CONTAINER=uwsgi-demo

DOCKER_IMAGE=$REPO/$PROJECT/$CONTAINER:1.0

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

BUILDROOT=$DIR/../

cmd="docker build -t $DOCKER_IMAGE -f $DIR/Dockerfile ."

echo $cmd
eval $cmd
