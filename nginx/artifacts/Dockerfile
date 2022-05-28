FROM scratch
LABEL docker-slim.version="linux|Transformer|1.37.6|26a36c88a94c677efd734e874ba081dabb84a224|2022-04-23_06:03:56AM"
LABEL maintainer="NGINX Docker Maintainers <docker-maint@nginx.com>"

LABEL docker-slim.source.image="nginx:1.22.0"


ENV PATH "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
ENV NGINX_VERSION "1.22.0"
ENV NJS_VERSION "0.7.4"
ENV PKG_RELEASE "1~bullseye"

ADD files.tar /
EXPOSE 80/tcp
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["nginx","-g","daemon off;"]
