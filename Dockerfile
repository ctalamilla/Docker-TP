FROM python:3

RUN pip3 install sqlalchemy\
    && pip3 install psycopg2\
    && pip3 install pandas

COPY /python /filltables

EXPOSE 5432

CMD ["python3"]
