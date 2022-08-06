FROM python:3.10-alpine

WORKDIR /app

COPY . .

RUN apk add --no-cache git
RUN pip3 install -r requirements.txt

CMD ["python3", "main.py"]