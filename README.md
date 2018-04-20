# DCMP System
## Docker Container Management Platform 
### Features ###
- WEB MONITOR


Concise, efficient, data visualization

- SHELL MANAGEMENT


Efficient, responsive, second-level deployment

- ANALYSTICS


Data visualization, dynamic updates

- DEPLOY SERVICES


Multiple mirroring, load balancing, high availability

### Overview
- Promotion Page

![PromotionPage](https://github.com/Mr-Linus/DCMP/blob/master/Promotionpage.png)

- Dashboard
![DashboardPage](https://github.com/Mr-Linus/DCMP/blob/master/dashboard.png)

> The project is currently in the construction phase.


### Development Test Environment
- Python 3.6 (Recommend)
- Django 2.0 (Necessary)

### Third party plugins (Necessary)
- django-bootstrap3
- psutil
- docker-py

```shell
pip install django-bootstrap3
pip install psutil
pip install docker
```

### Usage
- Change admin's password(Administrator username: admin): 
```shell
python manage.py changepassword
```

- Refresh & Synchronize the database:
```shell 
python manage.py makemigrations
python manage.py migrate
```

- Run the website
```shell
python manage.py runserver
```

### Update Logs
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

### Schedule
- [x]  Promotional page
- [x]  Sending email
- [x]  Saving Contacts
- [x]  Interactive management terminal
- [x]  Login Page
- [x]  Login interface
- [ ]  Docker Lib
- [ ]  Docker monitoring