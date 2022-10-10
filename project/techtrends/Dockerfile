# use the python base image
FROM python:3.8-slim-buster
LABEL  maintainer="Daniel Agbanyim"

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1 

WORKDIR /app

COPY requirements.txt requirements.txt

# install dependencies
RUN pip install -r requirements.txt

# copy all the files from the current directory to the container working directory (e.g. `/app`)
COPY . /app

RUN cd /app
# Initialize the database
RUN python3 init_db.py

# expose the port 3111
EXPOSE 3111 

# start the container
CMD ["python3", "app.py"]