FROM alpine:3.10

RUN apk add --no-cache python3 \
    && pip3 install --upgrade pip

WORKDIR /restar

COPY . /restar

RUN pip3 --no-cache-dir install flask

EXPOSE 4000

CMD ["python3", "app.py"]