FROM python:3.4-jessie
ENV TZ="Asia/Shanghai"
RUN git clone https://github.com/Mr-Linus/DCMP.git && cd DCMP \
    && pip install -r requirements.txt \
    && python manage.py makemigrations \
    && python manage.py migrate \
    && echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@dcmp.com', 'dcmpdcmp123')" | python manage.py shell

EXPOSE 8000
CMD [ "python","DCMP/manage.py","runserver","0.0.0.0:8000" ]