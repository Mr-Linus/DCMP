#!/usr/bin/env bash

echo "Build Images..."
sudo docker login -u $username -p $password registry.cn-hangzhou.aliyuncs.com
echo "Build backend..."
sudo docker build -t registry.cn-hangzhou.aliyuncs.com/geekcloud/dcmp:backend .
echo "Build nginx..."
sudo docker build -f ./nginx.dockerfile -t registry.cn-hangzhou.aliyuncs.com/geekcloud/dcmp:nginx .

echo "Push Images..."
sudo docker push registry.cn-hangzhou.aliyuncs.com/geekcloud/dcmp:backend
sudo docker push registry.cn-hangzhou.aliyuncs.com/geekcloud/dcmp:nginx
sudo docker logout