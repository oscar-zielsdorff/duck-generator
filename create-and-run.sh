#!/bin/bash
podman build -t duck-generator . \
&& podman run -d --name duck-generator-container duck-generator:latest