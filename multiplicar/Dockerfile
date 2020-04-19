FROM alpine:3.10

RUN apk add --no-cache python3 \
    && pip3 install --upgrade pip

WORKDIR /multiplicar

COPY . /multiplicar

RUN pip3 --no-cache-dir install flask

CMD ["python3", "app.py"]