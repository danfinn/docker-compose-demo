FROM python:alpine
RUN pip install Flask
RUN pip install pymongo
RUN pip install redis
COPY app.py /
COPY templates/ /templates/
CMD ["python", "app.py"]
EXPOSE 5000
