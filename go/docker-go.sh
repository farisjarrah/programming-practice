#!/usr/bin/env bash

docker run --rm -it --name go-dev \
  -v ${PWD}/src:/go/src/ golang
