# 工作进程数量
workers = 4
# 绑定的地址和端口
bind = '0.0.0.0:8000'
# 日志文件路径
accesslog = './access.log'
errorlog = './error.log'
# 日志级别
loglevel = 'info'
# gunicorn -c gunicorn.conf.py app:app