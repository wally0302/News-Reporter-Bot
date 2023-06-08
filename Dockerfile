FROM python:3.9

WORKDIR /app

COPY . /app

COPY user_ids.txt /app/user_ids.txt

RUN pip install -r requirements.txt

CMD ["python3", "main.py"]
