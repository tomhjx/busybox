FROM alpine:3.21
ARG PROTOC_VERSION=30.2
RUN apk update \
    # 添加临时构建依赖（wget/unzip）
    && apk add --no-cache --virtual .build-deps wget unzip \
    # 下载预编译的 Protobuf 工具包
    && wget -O /tmp/protoc.zip "https://github.com/protocolbuffers/protobuf/releases/download/v${PROTOC_VERSION}/protoc-${PROTOC_VERSION}-linux-x86_64.zip" \
    # 解压到系统目录
    && unzip /tmp/protoc.zip -d /usr/local \
    # 清理临时文件
    && rm /tmp/protoc.zip \
    # 删除临时依赖
    && apk del .build-deps

# 验证安装
RUN protoc --version