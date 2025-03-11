FROM python:3
ADD client.py .
ADD config.yml .
ADD logs.csv .
RUN pip install sockets
RUN pip install datetime
CMD ["python", "./client.py"]
EXPOSE 1065
