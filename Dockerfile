FROM python:3.9.5-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    gettext \
    libpq-dev \
    libcurl4-openssl-dev \
    libssl-dev

ARG DEPLOY_PATH='/buy_hodl'
RUN mkdir -p $DEPLOY_PATH

ADD buy_hodl/ $DEPLOY_PATH/buy_hodl
ADD wsgi.py $DEPLOY_PATH/wsgi.py
ADD setup.cfg $DEPLOY_PATH/setup.cfg
ADD requirements.txt $DEPLOY_PATH/requirements.txt

WORKDIR $DEPLOY_PATH

RUN pip install --upgrade pip
RUN pip install -U setuptools wheel
RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "wsgi:application"]
