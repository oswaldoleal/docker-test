FROM python:3

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y git

RUN git clone https://github.com/oswaldoleal/docker-test.git

WORKDIR /docker-test

RUN pip install pymongo flask

CMD [ "python", "./app.py" ]