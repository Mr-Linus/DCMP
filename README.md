# DCMP System

DCMP :whale2: :sweat_drops: is a Docker Container Management Platform using the django framework and python language and it is suitable for internal network deployment.

![build](https://travis-ci.org/Mr-Linus/DCMP.svg?branch=master) [![License](https://img.shields.io/badge/LICENSE-Apache-blue.svg)](https://github.com/Mr-Linus/DCMP/blob/master/LICENSE) ![PythonVersion](https://img.shields.io/badge/Python-3.6-brightgreen.svg) ![DjangoVersion](https://img.shields.io/badge/Django-2.0-green.svg)

Language:     English | [中文](https://github.com/Mr-Linus/DCMP/blob/master/readme_CN.md) 

### Features ###
- WEB MONITOR


Concise, efficient, data visualization

- Container MANAGEMENT



Efficient, responsive, second-level deployment

- ANALYSTICS


Data visualization, dynamic updates

- DEPLOY SERVICES


Multiple mirroring, load balancing, high availability

### Overview
- Promotion Page

![PromotionPage](https://github.com/Mr-Linus/DCMP/blob/master/img/Promotionpage.png)

- Login Page

![Login](https://github.com/Mr-Linus/DCMP/blob/master/img/login.png)

- Dashboard

![DashboardPage](https://github.com/Mr-Linus/DCMP/blob/master/img/dashboard.png)

- Containters Management

![Containers](https://github.com/Mr-Linus/DCMP/blob/master/img/containers.png)

- Containters Deploy

![Deploy](https://github.com/Mr-Linus/DCMP/blob/master/img/deploy.png)

- Swarm Monitor

![swarm](https://github.com/Mr-Linus/DCMP/blob/master/img/swarm.png)

- Images Management

![images](https://github.com/Mr-Linus/DCMP/blob/master/img/images.png)

- Volumes Management

![volumes](https://github.com/Mr-Linus/DCMP/blob/master/img/volumes.png)

- Networks Management

![networks](https://github.com/Mr-Linus/DCMP/blob/master/img/networks.png)

- Events Monitor

![events](https://github.com/Mr-Linus/DCMP/blob/master/img/events.png)

- User Management

![user](https://github.com/Mr-Linus/DCMP/blob/master/img/user.png)

### Development Test Environment
- Python 3.6 (Recommend)
- Django 2.0 (Necessary)
- Docker 18.03-ce
### Third party plugins (Necessary)
- django-bootstrap3
- psutil
- docker-py

Install plugins:
```shell
pip install django-bootstrap3
pip install psutil
pip install docker
```

### Usage
- Initialize Docker (PreStep):
```shell
docker swarm init #Please Your make sure your Docker engine is turned on 
```


- Refresh & Synchronize the database(Step 1):
```shell 
python manage.py makemigrations
python manage.py migrate
```

- Create Superuser(Step 2): 
```shell
python manage.py createsuperuser
```
> Superuser has the ability to create user.


- Run the website(Step 3):
```shell
python manage.py runserver
```

### Update Logs

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

### Schedule(Finished)
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

### Follow-up function
- [ ] i18N Internationalization 
- [x] Container Status Details
