FROM scratch
LABEL docker-slim.version="linux|Transformer|1.37.6|26a36c88a94c677efd734e874ba081dabb84a224|2022-04-23_06:03:56AM"
LABEL docker-slim.source.image="postgres:14.3-alpine"


ENV PATH "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
ENV LANG "en_US.utf8"
ENV PG_MAJOR "14"
ENV PG_VERSION "14.3"
ENV PG_SHA256 "279057368bf59a919c05ada8f95c5e04abb43e74b9a2a69c3d46a20e07a9af38"
ENV PGDATA "/var/lib/postgresql/data"

VOLUME ["/var/lib/postgresql/data"]
ADD files.tar /
EXPOSE 5432/tcp
ENTRYPOINT ["docker-entrypoint.sh"]
CMD ["postgres"]
