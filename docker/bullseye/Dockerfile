# 使用官方的 Node.js 镜像，带 Python 环境的基础镜像
FROM node:16-bullseye

# 安装 Python 3.9 和必需的工具
RUN apt-get update && apt-get install -y \
    python3.9 \
    python3.9-venv \
    python3-pip \
    wget \
    gnupg \
    ca-certificates \
    --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

# 安装 Chrome 浏览器
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | gpg --dearmor > /usr/share/keyrings/google-chrome.gpg && \
    echo "deb [signed-by=/usr/share/keyrings/google-chrome.gpg] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list && \
    apt-get update && apt-get install -y \
    google-chrome-stable \
    --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

# 检查安装的 Node.js、Python 和 Chrome 版本
RUN node -v && \
    npm -v && \
    python3.9 --version && \
    google-chrome --version

# 设置工作目录
WORKDIR /app


# 默认命令（可根据实际情况调整）
CMD ["bash"]