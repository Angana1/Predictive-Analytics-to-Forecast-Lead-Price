FROM python:3.7

WORKDIR /app1

COPY requirements.txt ./requirements.txt

RUN pip3 install -r requirements.txt

EXPOSE 8080

COPY . /app1

CMD streamlit run --server.port 8080 --server.enableCORS false app1.py