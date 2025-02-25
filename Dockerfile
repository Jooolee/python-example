# 使用 Python 3.8 作为基础镜像
FROM python:3.8

# 设置工作目录
WORKDIR /app

# 临时禁用 pip 并行安装和进度条
RUN pip install --no-cache-dir --no-use-pep517 --progress-bar off -U pip==25.0.1

# 复制项目依赖文件
COPY requirements.txt .

# 安装项目依赖
RUN pip install --no-cache-dir -r requirements.txt

# 复制项目文件到工作目录
COPY . .

# 暴露 Gunicorn 监听的端口
EXPOSE 8000

# 启动 Gunicorn 服务
CMD ["gunicorn", "-c", "gunicorn.conf.py", "app:app"]


# docker build -t flask-gunicorn-app .
# docker run -p 8000:8000 flask-gunicorn-app