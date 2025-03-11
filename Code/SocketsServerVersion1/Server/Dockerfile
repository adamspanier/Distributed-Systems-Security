FROM python:3
ADD server.py .
ADD config.yml .
ADD logs.csv .
RUN pip install sockets
RUN pip install datetime
CMD ["python", "./server.py"]
EXPOSE 1065
