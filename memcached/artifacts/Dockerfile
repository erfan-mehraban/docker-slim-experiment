FROM scratch
LABEL docker-slim.version="linux|Transformer|1.37.6|26a36c88a94c677efd734e874ba081dabb84a224|2022-04-23_06:03:56AM"
LABEL docker-slim.source.image="memcached:1.6.15"


ENV PATH "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
ENV MEMCACHED_VERSION "1.6.15"
ENV MEMCACHED_SHA1 "badcfa0d65f5797cc9c2f957f3fbfedbd8c13411"

ADD files.tar /
USER memcache
EXPOSE 11211/tcp
ENTRYPOINT ["docker-entrypoint.sh"]
CMD ["memcached"]
