<h1 align=center>AAIT Official Forum </h1>
<p align=center>
<img src="https://img.shields.io/badge/version-0.0.1-red.svg"> <img src="https://img.shields.io/badge/founder-%E8%94%A1%E4%BB%B2%E6%99%A8-orange.svg"> <img src="https://img.shields.io/badge/%E5%9B%9B%E5%B7%9D%E8%BD%BB%E5%8C%96%E5%B7%A5-AAIT-brightgreen.svg"> <img src="https://img.shields.io/badge/status-Unfinished-lightgrey.svg">
</p>
   
<p align=center><b>注意, 这仍是一个未完成版本。</b></p>

> AAIT Official Forum is a UGC based website and mobile hybrid APP for members of AAIT to exchange ideas and share inspirations.

**By reading through this documentation you will:**
- Get a copy of this project;
- Running the development version of the project on your machine;
- Get to know how the project works, and write your first line of code;
- Contribute to the project.

## 1 About API

> 这一部分文档将对本项目服务端API规范进行说明

本项目服务端采用的是遵守 RESTful API规范的djangorestframework 框架开发API，RESTful API 的英文全称  REpresentational State Transfer ，用HTTP动词（GET,POST,PUT,DELETE)描述操作。

### 2 项目配置

>服务端采用的数据库为mysql数据库
初次使用需要在setting.py 中设置一下信息:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'aait_forum', #数据库名
        'USER': 'root',	#用户名
        'PASSWORD': 'root',#用户密码
        'HOST': '127.0.0.1',#数据库地址
        'PORT': '3306', #数据库端口
    }
}

>设置好了之后先导入数据库文件 aait_forum.sql 到数据库

### 3 goods的api

get访问127.0.0.1:8000/goods/
获取全部数据
get访问127.0.0.1:8000/goods_detail/id/id号
访问goods详情
post提交对应字段增加一行数据
put修改

### 3 Poromodo Clock的api

get访问127.0.0.1:8000/poromodoclock/
获取全部数据
get访问127.0.0.1:8000/poromodoclock_detail/id/id号
访问poromodoclock的详情

post提交对应字段增加一行数据

put修改







