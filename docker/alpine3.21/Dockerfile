FROM alpine:3.21
ARG PROTOC_VERSION=30.2
RUN apk add wget unzip \
    && wget -O /protoc.zip "https://github.com/protocolbuffers/protobuf/releases/download/v${PROTOC_VERSION}/protoc-${PROTOC_VERSION}-linux-x86_64.zip" \
    && unzip /protoc.zip -d /usr/local/protoc
# 验证安装
RUN protoc --version