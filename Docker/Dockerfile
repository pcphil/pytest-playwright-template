FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN python -m pip install --no-cache-dir -r requirements.txt &&\
    python -m playwright install chromium &&\
    python -m playwright install --with-deps &&\
    chmod +x ./entrypoint.sh

ENTRYPOINT ["./Docker/entrypoint.sh"]