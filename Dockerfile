FROM python:3.9

COPY . /src
WORKDIR /src

RUN apt-get update && apt-get install -y pkg-config
RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
