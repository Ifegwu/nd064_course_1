# use the python base image
FROM python:3.8-alpine
LABEL  maintainer="Daniel Agbanyim"

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1 

# copy all the files from the current directory to the container working directory (e.g. `/app`)
COPY . /app

WORKDIR /app
# install dependencies
RUN pip install -r requirements.txt
RUN pwd
RUN ll 
RUN ls techtrends
# expose the port 3111
EXPOSE 3111 

# start the container
CMD ["python3", "app.py"]