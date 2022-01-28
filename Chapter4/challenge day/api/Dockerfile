FROM python:3
WORKDIR /api
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . /api/
EXPOSE 8000
ENTRYPOINT ["python"]
CMD ["./src/app.py"]