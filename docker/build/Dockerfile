# Dockerfile - CentOS 7
FROM centos:7

LABEL maintainer="Tom <tom_hejiaxi@163.com>"

RUN yum install -y \
        gcc \
        gcc-c++ \
        gd-devel \
        gettext \
        GeoIP-devel \
        libxslt-devel \
        make \
        perl \
        perl-ExtUtils-Embed \
        readline-devel \
        unzip \
        zlib-devel \
        patch \
        httpd-tools \
        nfs-utils \ 
        inotify-tools; \
        curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"; \
        install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl; \
        cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime