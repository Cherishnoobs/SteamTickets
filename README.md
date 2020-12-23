# SteamTickets

Steamticket is a sharing website dedicated to displaying the latest discount information of steam

* Demo for SteamTickets

## 部署

本程序提供前后端分离拓展，以下主要为后端部署说明。

总的来说，分为以下几步：

* 安装程序与依赖
* 修改 Nosql 配置项
* 启用核心
* 运行

### 安装依赖

```
$ pip3 install -r requirements.txt
```



### 修改配置

#### REDIS

编辑 ./app/sql/Redis.py 。

```python
pool = redis.ConnectionPool(host='', port=6379, decode_responses=True) // 地址 + 端口 + 其他所需参数
r = redis.Redis(host='', port=6379, decode_responses=True) 
```

#### MONGO

编辑 ./app/sql/Mongo.py 。

```python
conn=MongoClient(host='',port=27017,username='',password='') // 地址 + 端口 + 用户 + 密码 + 其他所需参数
db = conn[''] // 所需 collection
```

#### 启用相应核心数据库

默认不会加载任何服务。若要开启相应服务，请**正确修改各配置后**启用加载核心。

编辑  ./app/api/__init__.py ，取消相应注释即可。

```python
from .sql.Mongo import Mongo
from .sql.Redis import Redis
```

#### 启动程序

```
$ python3 main.py
```

（若要更改程序的运行地址，请修改 `./main.py` ）



### 前后端分离 (可选)

不是必要的操作，但如果你想的话，请按照以下步骤配置。

1. 编辑 ./templates/index.html ,将 232 行处 {% for item in data %} 注释掉
2. 导入 Vue.js 改用 Vue-For
3. 启用后台接口 http://[hostname]/info/api/v1.0/discounts 与 http://[hostname]/info/api/v1.0/tickets
4. 将 API_URL  修改为 后端运行地址

## 开发

#### 目录

```
├── app
├── ├── __init__.py
├── ├── sql           // 数据库核心 //
├── ├── ├── __init__.py       // 开关
├── ├── ├── Redis.py              // Redis - 折扣信息
├── ├── ├── Mongo.py             // Mongo - 游戏信息
├── ├── api
├── ├── ├── __init__.py // 开关
├── ├── ├── Discount.py // 折扣信息视图类
├── ├── ├── Tickets.py // 游戏信息视图类
├── static           // 前端样式 //
├── ├── css	
├── ├── font
├── ├── images
├── ├── js
├── ├── webfonts
├── template
├── ├── index.html	// 主页
├── ├── about.html	// 介绍页面
├── main.py	// 程序入口
├── .gitignore
├── .flaskenv

```

## 说明

* 本程序会一次性加载全部允许的文件并缓存，所以若文件较多此过程可能会较慢（取决于你文件的数量与网络状况），但不影响正常运行

- 仅在小规模且请求情况下测试，运行稳定

## 声明

- 本程序仅供学习参考，请在达成目的后停止使用

- 使用后任何不可知事件都与原作者无关，原作者不承担任何后果

- [MIT License](https://choosealicense.com/licenses/mit/)

使用愉快。  ：）
