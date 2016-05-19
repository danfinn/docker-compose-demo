FROM mongo

COPY zips.json /tmp/zips.json
CMD mongoimport --host mongodb --db data --collection zips --file /tmp/zips.json
