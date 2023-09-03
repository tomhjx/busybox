FROM alpine:3.18

RUN apk --no-cache --update --verbose add curl grep bash tcpdump && \
    rm -rf /var/cache/apk/* /tmp/* /sbin/halt /sbin/poweroff /sbin/reboot