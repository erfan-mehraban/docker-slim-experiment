FROM scratch
LABEL docker-slim.version="linux|Transformer|1.37.6|26a36c88a94c677efd734e874ba081dabb84a224|2022-04-23_06:03:56AM"
LABEL docker-slim.source.image="redis:7.0.0"


ENV PATH "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
ENV GOSU_VERSION "1.14"
ENV REDIS_VERSION "7.0.0"
ENV REDIS_DOWNLOAD_URL "http://download.redis.io/releases/redis-7.0.0.tar.gz"
ENV REDIS_DOWNLOAD_SHA "284d8bd1fd85d6a55a05ee4e7c31c31977ad56cbf344ed83790beeb148baa720"

VOLUME ["/data"]
ADD files.tar /
WORKDIR /data
EXPOSE 6379/tcp
ENTRYPOINT ["docker-entrypoint.sh"]
CMD ["redis-server"]
