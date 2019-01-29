FROM python:3.4-jessie

ENV TZ="Asia/Shanghai"



RUN git clone https://github.com/Mr-Linus/DCMP.git
    && cd DCMP
    && pip install -r requirements.txt



EXPOSE 8000
CMD [ "bash","/DCMP/endpoint.sh" ]