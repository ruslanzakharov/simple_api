FROM python:3.10-slim

WORKDIR /simple_api
COPY . .
RUN apt update \
    && apt install -y libpq-dev gcc \
    && pip install --upgrade pip \
    && pip install poetry \
    && poetry config virtualenvs.create false \
    && poetry install

CMD ["uvicorn", "app.__main__:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
EXPOSE 8000