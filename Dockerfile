FROM python:3.10

WORKDIR /app

COPY . .

EXPOSE 5000

# install requirements
RUN pip install -r requirements.txt

ENV FLASK_APP=app.py
ENV FLASK_ENV=development

CMD ["flask", "run", "--host=0.0.0.0"]