#!/usr/bin/env bash

docker run --rm -it --name go-dev \
  -v ${PWD}/src:/python/src/ python:latest /bin/bash
