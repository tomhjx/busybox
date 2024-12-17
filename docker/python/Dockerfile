# 使用官方 Python 镜像作为基础镜像
FROM python:3.9-slim

# 设置工作目录
WORKDIR /app

# 更新系统包并安装必要的依赖
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    wget \
    gnupg \
    libnss3 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libdrm2 \
    libgbm1 \
    libxkbcommon0 \
    libxcomposite1 \
    libxrandr2 \
    libasound2 \
    libpangocairo-1.0-0 \
    libgtk-3-0 \
    libegl1-mesa \
    libopengl0 \
    dbus \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# 安装 Node.js（此处安装 Node.js 16.x LTS 版本，可以根据需要修改版本）
RUN curl -fsSL https://deb.nodesource.com/setup_16.x | bash - \
    && apt-get install -y nodejs \
    && node -v \
    && npm -v

# 安装 Playwright 及浏览器
RUN pip install playwright && playwright install --with-deps

# 设置容器启动时的默认命令
CMD ["python", "app.py"]
