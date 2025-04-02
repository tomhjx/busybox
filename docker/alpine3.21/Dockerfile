FROM alpine:3.21

# 安装依赖工具（wget/unzip）
apk add wget unzip

# 下载预编译的 protoc 二进制包
PROTOC_VERSION="30.2"
wget https://github.com/protocolbuffers/protobuf/releases/download/v${PROTOC_VERSION}/protoc-${PROTOC_VERSION}-linux-x86_64.zip

# 解压到 /usr/local
unzip protoc-${PROTOC_VERSION}-linux-x86_64.zip -d /usr/local

# 验证安装
protoc --version