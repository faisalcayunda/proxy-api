FROM python:3.11-slim
COPY . /app
WORKDIR /app
RUN apt-get update -qy && \
    apt-get install -qq -y && \
    apt-get install -y locales locales-all && \
    apt-get install -y build-essential gcc libpq-dev libcbor0 libedit2 libfido2-1 libxext6 libxmuu1 openssh-client xauth && \
    apt-get install -y python3-dev python3-pip python3-venv python3-virtualenv python3-wheel && \
    apt-get clean && \
    pip install --upgrade pip && \
    pip install --no-cache-dir -r ./requirementst.txt
EXPOSE 5000
CMD uvicorn main:app --port 5000 src.main:app --reload