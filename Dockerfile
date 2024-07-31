FROM registry.access.redhat.com/ubi8/python-38:1-131

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY app.py .

USER 1001

CMD ["python", "app.py"]
