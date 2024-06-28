#!/bin/bash
podman build --userns=keep-id -t duck-generator . \
&& podman run -d --name duck-generator-container duck-generator:latest