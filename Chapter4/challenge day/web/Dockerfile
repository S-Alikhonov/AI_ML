FROM python:3
WORKDIR /web
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . /web/
EXPOSE 5000
ENTRYPOINT [ "python" ]
CMD ["app.py"]
