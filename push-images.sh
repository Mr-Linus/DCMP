#!/usr/bin/env bash
echo "Pushing Images"
sudo docker login -u $username -p $password registry.cn-hangzhou.aliyuncs.com
sudo docker build -t registry.cn-hangzhou.aliyuncs.com/geekcloud/dcmp:latest .
sudo docker push registry.cn-hangzhou.aliyuncs.com/geekcloud/dcmp:latest
sudo docker logout