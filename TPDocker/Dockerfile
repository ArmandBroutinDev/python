FROM python:3.6-stretch

WORKDIR /home/armand/dev/TPDocker/app
COPY . .

RUN apt-get update
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN apt-get install -y vim
 
RUN pip3 install -r ./requirements.txt

EXPOSE 5000

CMD ["python3","./truc.py"]