FROM python:slim

LABEL Maintainer="soriphoono"

WORKDIR /usr/app/src

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY src/main.py ./

CMD ["python", "./main.py"]