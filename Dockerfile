FROM remote-docker.artifactory.dbgcloud.io/ubi8/python-38:1-131
WORKDIR /app
COPY requirements.txt .
RUN pip install --proxy http://webproxy.deutsche-boerse.de:8080 -r requirements.txt
COPY app.py .
EXPOSE 5000
USER 1001
ENTRYPOINT [ "python" ]
CMD ["app.py" ]
