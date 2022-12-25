FROM python:3.9-buster

WORKDIR /var/app

CMD pip install virtualenv \
    virtualenv venv \
    source venv/bin/activate

COPY app/requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

COPY app .

CMD python3 -v

CMD uvicorn app:app --reload --host=0.0.0.0