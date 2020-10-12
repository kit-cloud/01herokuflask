FROM python:3.8.0-buster

# Make a work directory
WORKDIR /app

#dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

#copy of source code
COPY /app .

#run the app
CMD ["python", "myproxy.py"]