FROM python:3.6-jessie

LABEL maintainer="Mr-Linus admin@geekfan.club"

ARG TZ="Asia/Shanghai"

ENV TZ ${TZ}

ARG  PROJECT_NAME="DCMP"

ENV PROJECT_NAME ${PROJECT_NAME}

COPY . /${PROJECT_NAME}

RUN  pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r /${PROJECT_NAME}/requirements.txt


EXPOSE 8000

CMD [ "bash", "/DCMP/endpoint.sh" ]
