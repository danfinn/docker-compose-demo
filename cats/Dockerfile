#FROM ubuntu
#RUN apt-get update
#RUN apt-get -y install python-pip
#RUN pip install Flask
#copy hello_world.py /
#CMD ["python", "hello_world.py"]
#EXPOSE 5000

FROM python:alpine
RUN pip install Flask
RUN pip install pymongo
copy hello_world.py /
CMD ["python", "hello_world.py"]
EXPOSE 5000
