FROM python:3.7-alpine
COPY . /CSV-Combiner-Cleaner
WORKDIR /CSV-Combiner-Cleaner

RUN pip install -r requirements.txt

RUN pip install -e .

ENTRYPOINT ["csv-combiner-cleaner"] 
