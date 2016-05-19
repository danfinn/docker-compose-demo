# docker-compose demo

This is a very basic docker-compose demo.  It will bring up a couple of different services (flask, redis, mongo) and create a very basic webapp.  When the environment is brought up, the mongo database is seeded with zip code information.  The webapp will then randomly pull a zip code from mongo and display that, as well as keeping track of the number of hits and displaying that as well.
