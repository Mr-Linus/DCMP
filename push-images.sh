#!/usr/bin/env bash

sudo docker build -t registry.cn-hangzhou.aliyuncs.com/geekcloud/dcmp:latest .
sudo docker push registry.cn-hangzhou.aliyuncs.com/geekcloud/dcmp:latest