FROM python:3.12-alpine
WORKDIR /movie
COPY . /movie
RUN pip install -r requirements.txt
CMD ["python", "app.py"]