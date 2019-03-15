# cnnb

***

用Scrapy框架爬取宁波日报近期本地新闻,并把新闻保存在mongodb,保存在本地文件夹中,保存为json

---

环境: 

PyCharm 2018.3.5 (Professional Edition)

Scrapy 1.5.1

Python 3.7.0

newspaper3k 0.2.8

### 创建项目

```
scrapy startproject cnnb
scrapy genspider nbnews cnnb.com.cn
```

在项目目录中的settings.py文件中加上mongodb的信息。

```
mongo_host = 'localhost'
mongo_port = 27017
mongo_user = 'root'
mongo_passwd = '1997'
mongo_db_name = 'crawler'
mongo_db_collection = 'nbnews'
```

在pipelines.py中加入mongodb的操作语句,以及保存为txt的语句。scrapy自带保存为json、scv、xml、pickle、marshal,自带ftp远程输出。

### 选择

scrapy自带xpath和css选择器,不需要额外使用别的库。

```
news_list = response.xpath('//div[@class="articleList"]//ul[@class="fiveBox"]//li//a//@href').extract()
```

利用scrapy自带的xpath选择器,获得新闻文章url列表。用newspaper3k库以及获得的url获得每一篇新闻的具体内容与标题。

### 启动器

因为pycharm不能直接创建scrapy项目,不能像Django那样直接在pycharm启动项目,所以需要通过终端来启动。在pycharm启动也是需要通过终端。

```
from scrapy import cmdline
cmdline.execute('scrapy crawl nbnews'.split())
```

### 截图 : 

保存在本地以新闻的发布时间来划分
<img src="https://github.com/GGG1235/cnnb/blob/master/images/file1.png" width="375" alt="文件夹">

<img src="https://github.com/GGG1235/cnnb/blob/master/images/file2.png" width="375" alt="本地文件新闻列表">

<img src="https://github.com/GGG1235/cnnb/blob/master/images/json.png" width="375" alt="保存为json">

<img src="https://github.com/GGG1235/cnnb/blob/master/images/mongodb.png" width="375" alt="保存在mongodb">

<img src="https://github.com/GGG1235/raspberrypi/blob/master/images/1.png" width="375" alt="neofetch">
