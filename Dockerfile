FROM python:3.13-slim

WORKDIR /code

COPY ./main.py /code/
COPY ./requirements.txt /code/
COPY ./src /code/src

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

CMD ["fastapi", "run", "main.py", "--port", "8000"]
