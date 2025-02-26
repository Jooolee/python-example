import tomllib # python 3.11+
import tomlkit

# 读取 requirements.txt 文件
with open('requirements.txt', 'r') as f:
    requirements = f.read().splitlines()

# 读取 pyproject.toml 文件
try:
    with open('pyproject.toml', 'rb') as f:
        pyproject = tomllib.load(f)
except FileNotFoundError:
    pyproject = {}

# 创建或获取 [tool.poetry.dependencies] 部分
if 'tool' not in pyproject:
    pyproject['tool'] = {}
if 'poetry' not in pyproject['tool']:
    pyproject['tool']['poetry'] = {}
if 'dependencies' not in pyproject['tool']['poetry']:
    pyproject['tool']['poetry']['dependencies'] = {}

# 添加依赖到 [tool.poetry.dependencies] 部分
for requirement in requirements:
    package, version = requirement.split('==')
    pyproject['tool']['poetry']['dependencies'][package] = version

# 将修改后的 pyproject 写回到 pyproject.toml 文件
with open('pyproject.toml', 'w') as f:
    f.write(tomlkit.dumps(pyproject))