FROM python:3.9.9

WORKDIR /usr/app/src

COPY *.py ./

CMD [ "python", "./railway.py"]