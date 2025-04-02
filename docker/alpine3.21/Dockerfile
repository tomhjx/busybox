FROM alpine:3.21

# 安装依赖工具（wget/unzip）
RUN apk add wget unzip

# 下载预编译的 protoc 二进制包
RUN wget https://github.com/protocolbuffers/protobuf/releases/download/v30.2/protoc-30.2-linux-x86_64.zip

# 解压到 /usr/local
RUN unzip protoc-30.2-linux-x86_64.zip -d /usr/local

# 验证安装
RUN protoc --version