FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

COPY start.sh /root/my-flask-store/start.sh
RUN chmod +x /root/my-flask-store/start.sh

ENTRYPOINT ["sh", "/root/my-flask-store/start.sh"]

