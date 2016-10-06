#FROM ubuntu:14.04
FROM citizenstig/wscmpbase


ENV DEBIAN_FRONTEND noninteractive

WORKDIR /opt/wscmp
COPY . /opt/wscmp

#RUN apt-get update && apt-get install -y git python3-dev python3-pip supervisor nginx && \
#    pip3 install -r requirements.txt
RUN cp /opt/wscmp/conf/nginx/wscmp.conf /etc/nginx/sites-enabled/default


#EXPOSE 80
#
#CMD ["/usr/bin/supervisord", "-c", "/opt/wscmp/conf/supervisor/supervisord.conf"]