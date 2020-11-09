FROM debian

ADD http://www.vcheng.org/ponysay/ponysay_3.0.2-1_all.deb /tmp
RUN apt-get update && apt-get install -y python3 && dpkg -i /tmp/ponysay_3.0.2-1_all.deb

ENTRYPOINT ["/usr/bin/ponysay"]
CMD ["Hey, netology”]
