FROM python:2.7

ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip && pip install -r requirements.txt

ENTRYPOINT ["python"]

CMD ["app.py"]
