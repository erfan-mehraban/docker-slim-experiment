FROM scratch
LABEL docker-slim.version="linux|Transformer|1.37.6|26a36c88a94c677efd734e874ba081dabb84a224|2022-04-23_06:03:56AM"
LABEL docker-slim.source.image="mongo:5.0.8"


ENV PATH "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
ENV GOSU_VERSION "1.12"
ENV JSYAML_VERSION "3.13.1"
ENV MONGO_PACKAGE "mongodb-org"
ENV MONGO_REPO "repo.mongodb.org"
ENV MONGO_MAJOR "5.0"
ENV MONGO_VERSION "5.0.8"
ENV HOME "/data/db"

VOLUME ["/data/configdb","/data/db"]
ADD files.tar /
EXPOSE 27017/tcp
ENTRYPOINT ["docker-entrypoint.sh"]
CMD ["mongod"]
