# DCMP 

DCMP :whale2: :sweat_drops: 是一个使用Python语言和Django框架搭建的Docker容器管理平台，适用于内网部署.

![build](https://travis-ci.org/Mr-Linus/DCMP.svg?branch=master) [![License](https://img.shields.io/badge/LICENSE-Apache-blue.svg)](https://github.com/Mr-Linus/DCMP/blob/master/LICENSE) ![PythonVersion](https://img.shields.io/badge/Python-3.6-brightgreen.svg) ![DjangoVersion](https://img.shields.io/badge/Django-2.0-green.svg) [![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2FMr-Linus%2FDCMP.svg?type=shield)](https://app.fossa.io/projects/git%2Bgithub.com%2FMr-Linus%2FDCMP?ref=badge_shield)

Language:     [English](https://github.com/Mr-Linus/DCMP/blob/master/README.md)  | 中文


### 特点 ###
- WEB 监控

便捷、高效

- 容器管理

快速响应、秒级部署


- 数据可视化

数据同步，动态更新

- 服务管理

容器、镜像、网络、卷、消息

### 外观
- 宣传页

![PromotionPage](https://github.com/Mr-Linus/DCMP/blob/master/img/Promotionpage.png)

- 登陆

![Login](https://github.com/Mr-Linus/DCMP/blob/master/img/login.png)

- 仪表盘

![DashboardPage](https://github.com/Mr-Linus/DCMP/blob/master/img/dashboard.png)

- 容器管理

![Containers](https://github.com/Mr-Linus/DCMP/blob/master/img/containers.png)

- 容器部署

![Deploy](https://github.com/Mr-Linus/DCMP/blob/master/img/deploy.png)

- Swarm 监控

![swarm](https://github.com/Mr-Linus/DCMP/blob/master/img/swarm.png)

- 镜像管理

![images](https://github.com/Mr-Linus/DCMP/blob/master/img/images.png)

- 卷管理

![volumes](https://github.com/Mr-Linus/DCMP/blob/master/img/volumes.png)

- 网络管理

![networks](https://github.com/Mr-Linus/DCMP/blob/master/img/networks.png)

- 事件监控

![events](https://github.com/Mr-Linus/DCMP/blob/master/img/events.png)

- 用户管理

![user](https://github.com/Mr-Linus/DCMP/blob/master/img/user.png)

### 开发测试环境
- Python 3.6 (Recommend)
- Django 2.0 (Necessary)
- Docker 18.03-ce
- Redis 2.0.6 
### 第三方软件包
- django-bootstrap3
- psutil
- docker-py
- celery
> 安装:
```shell
pip install -r requirements.txt
```

### Docker版启动

```bash                                                                                                                                                          
# Create docker network 
docker network create dcmp
# Create redis as message queue
docker run -d --name dcmp-redis --net dcmp  redis  
# Run dcmp backend
docker run -itd --name dcmp-backend \
       -v /var/run/docker.sock:/var/run/docker.sock \
       --net dcmp  \
       registry.cn-hangzhou.aliyuncs.com/geekcloud/dcmp:backend
# Run DCMP frontend
docker run -itd --name dcmp-nginx \
       -p 8000:80 \
       --net dcmp \
       registry.cn-hangzhou.aliyuncs.com/geekcloud/dcmp:nginx
```                                                                                                                                                              
                                                                                                                                                                 
> 访问 DCMP: http://localhost:8000/
> 
> username:admin password:dcmpdcmp123

### 用法
- 初始化 Docker (PreStep):
```shell
docker swarm init #请确保你的Docker已经开启 
```


- 更新同步数据库(Step 1):
```shell 
python manage.py makemigrations
python manage.py migrate
```

- 创建超级用户(Step 2): 
```shell
python manage.py createsuperuser
```
> 超级用户具有创建用户功能


- 运行(Step 3):
```shell
python manage.py runserver
```

- 运行 Redis 服务(Step 4):
```shell
docker run --name dcmp-redis -p 6379:6379 redis
```

- 开启Celery Worker(Step 5):
```shell
celery -A DCMP worker -l info
```



### 更新日志
### Update Logs
#### V3.2.0 Date :2019/2/12
- Upgrade the struct of docker
#### V3.1.0 Date :2019/1/26
- Add ajax dynamic update function
#### V3.0.1 Date :2018/8/17
- Fix errors in Redis 
#### V3.0(Beta) Date :2018/7/12
- Add Celery to accelerate docker services
- Add Rabbitmq to processing messages
- Fix some bugs
#### V2.6(Beta) Date :2018/5/2 
- Add User ManageMent Function(Rewrite to User Management)
- Fix some bugs
#### V2.5 Date :2018/4/30
- Add Swarm Function
- Add Image Function
- Add Volume Function
- Add Network Function
- Fix some bugs
#### V2.4 Date :2018/4/29
- Add Deploy funtion
- Fix some bugs
#### V2.3 Date :2018/4/25
- Add container function 
- Fix some bugs
#### V2.2 Date :2018/4/21
- Add system lib
- Add docker lib
- Fix login bugs
#### V2.1 Date :2018/4/18
- Finish login/logout function
- Rewrite login static HTML page
- Fix bugs
#### V2.0 Date :2018/4/15
- Use Model Form instead of traditional HTML forms
- Compact code
- Rewrite : Models , Views  
- Add Django-BootStrap3 to render HTML Pages

#### V1.0 Date :2018/4/10
- Finish Promotional page
- Finish Sending email
- Finish Saving Contacts
- Finish Interactive management terminal

### 进度(Finished)
- [x]  Promotional page
- [x]  Sending email
- [x]  Saving Contacts
- [x]  Interactive Management terminal
- [x]  Index Dashboard
- [x]  Login Page
- [x]  Login Interface
- [x]  Docker Lib
- [x]  Docker Monitor
- [x]  Docker Swarm  Monitor
- [x]  Docker Container Management 
- [x]  Docker Deploy Function
- [x]  Docker Image Management 
- [x]  User Management
- [x]  Docker Network Management
- [x]  Docker Volume Management

### 后期功能
- [ ] i18N Internationalization 
- [x] Container Status Details
