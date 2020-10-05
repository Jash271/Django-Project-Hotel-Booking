FROM python:3.6

WORKDIR /usr/src/app


COPY . . 

RUN pip install -r requirements.txt

EXPOSE 8000

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
