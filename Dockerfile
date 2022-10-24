FROM ubuntu
RUN apt update
RUN apt install python3 -y
COPY python.py ./
EXPOSE 8000

CMD ["python3","./python.py"]

