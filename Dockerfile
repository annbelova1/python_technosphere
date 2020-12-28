FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN mkdir /hometask
WORKDIR /hometask
COPY requirements.txt /hometask/
RUN pip install --upgrade pip && pip install -r requirements.txt
ADD . /hometask/