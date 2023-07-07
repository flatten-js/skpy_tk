FROM python:3.9

RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt update && apt install -y ./google-chrome-stable_current_amd64.deb

WORKDIR /usr/local/src

RUN pip install pipenv

COPY Pipfile Pipfile.lock .
RUN pipenv install --system
# RUN pipenv install --dev --system

CMD ["python", "main.py"]
# CMD ["python", "-m", "debugpy", "--listen", "5678", "main.py"]