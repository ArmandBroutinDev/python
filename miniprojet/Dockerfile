FROM python:3.6-slim

WORKDIR /home/armand/dev/miniprojet/app
COPY . .

RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 \
    python3-pip \
    vim 
 
RUN pip3 install -r ./requirements.txt

EXPOSE 5000

CMD ["python3","./app.py"]