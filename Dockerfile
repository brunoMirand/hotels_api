FROM python:2.7

ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip && pip install -r requirements.txt

ENTRYPOINT ["python"]

HEALTHCHECK --interval=30s --timeout=3s \
    CMD curl -f http://localhost:5000/healthcheck || exit 1

CMD ["app.py"]
