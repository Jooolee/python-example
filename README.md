# python-example

### 环境
```shell
conda create -n flask_mysql_demo python=3.8

conda activate flask_mysql_demo

conda env list

conda deactivate

conda env export > environment.yml
conda env remove -n flask_mysql_demo
conda env create -f environment.yml
```

```shell
python app.py
```

```shell
# 启动
gunicorn -c gunicorn.conf.py app:app
# 后台运行
nohup gunicorn -c gunicorn.conf.py app:app &
# 进程查看
ps -ef | grep gunicorn
# 停止
kill -9 <PID>
# 测试
curl http://127.0.0.1:8000/users
```

```shell
# 不停服务重启：

pstree -ap | grep gunicorn

kill -HUP 126223
```

```shell
# 当前环境
conda activate flask_mysql_demo
# 生成requirements.txt依赖文件
pip freeze > requirements.txt
```