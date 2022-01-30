FROM python:3
WORKDIR /api
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . /api/
RUN apt-get update && apt-get install -y python3-opencv
RUN pip install opencv-python
EXPOSE 8000
ENTRYPOINT ["python"]
CMD ["./src/app.py"]