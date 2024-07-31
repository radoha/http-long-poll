FROM registry.access.redhat.com/ubi8/python-38:1-131

WORKDIR /app

COPY requirements.txt .

RUN pip install --proxy http://webproxy.deutsche-boerse.de:8080 -r requirements.txt

COPY app.py .

EXPOSE 5000

USER 1001

CMD ["python", "app.py"]
