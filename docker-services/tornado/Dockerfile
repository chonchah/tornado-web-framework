FROM python:3.8

EXPOSE 4311

RUN mkdir -p /tornado
WORKDIR /tornado

COPY requirements.txt /tornado
COPY . /tornado

RUN pip install --no-cache-dir -r /tornado/requirements.txt

ENTRYPOINT ["python", "server.py"]
