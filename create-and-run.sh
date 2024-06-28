#!/bin/bash
# Sudo used to fix error with multiuser ids
sudo podman build -t duck-generator . \
&& sudo podman run -d --name duck-generator-container duck-generator:latest