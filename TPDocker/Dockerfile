FROM python:3.6-stretch

WORKDIR /home/armand/dev/TPDocker/app
COPY . .

RUN apt-get update \
    apt-get install python3 \
    apt-get install python3-pip \
    apt-get install vim
 
RUN pip3 install -r ./requirements.txt

EXPOSE 5000

CMD ["python","./truc.py"]