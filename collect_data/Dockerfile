FROM python:3.9-buster

ENV TZ=Europe/Warsaw

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

COPY requirements.txt ./requirements.txt

RUN pip install -r ./requirements.txt

COPY api_call.py ./api_call.py

EXPOSE 27017

CMD python api_call.py