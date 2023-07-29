FROM python:3.9-slim-buster

RUN useradd -m appuser

WORKDIR /app

COPY --chown=appuser:appuser . .

USER appuser

RUN pip3 install -r requirements.txt

EXPOSE 5000

CMD ["python3", "main.py"]