FROM python:3.4-jessie

ENV TZ="Asia/Shanghai"

COPY ../DCMP/ /DCMP/

RUN  cd DCMP && pip install -r requirements.txt



EXPOSE 8000
CMD [ "bash","/DCMP/endpoint.sh" ]