FROM python:3.10

WORKDIR /app

COPY . .

EXPOSE 5000

# install requirements
RUN pip install -r requirements.txt

CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]