#!/bin/sh
set -e -u

IMAGE_NAME=meeshkan/dependency-detector
docker build -t $IMAGE_NAME .
docker push $IMAGE_NAME

