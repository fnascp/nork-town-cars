FROM python:3.10.10-bullseye

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

ENV FLASK_APP runner:app

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]