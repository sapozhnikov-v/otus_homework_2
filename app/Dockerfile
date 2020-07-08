FROM python:3.8.3-slim

WORKDIR /usr/src/app/

# install dependencies
RUN pip install --upgrade pip
COPY requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

COPY . /usr/src/app/
RUN chmod +x start.sh

ENTRYPOINT ["bash", "start.sh"]
