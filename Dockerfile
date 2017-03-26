FROM python:3.6-alpine

RUN mkdir -p /deploy/api

COPY requirements.txt /deploy/
RUN apk --update add --virtual build-base \
  && apk add postgresql-dev libffi-dev \
  && python3 -m ensurepip \
  && pip install --upgrade pip

RUN pip install -r /deploy/requirements.txt

WORKDIR /deploy/
COPY . /deploy/

EXPOSE 5000

CMD ["gunicorn", "--config", "/deploy/gunicorn.cfg", "autoapp:app"]
