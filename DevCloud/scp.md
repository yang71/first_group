### 简介

- 使用Twisted异步网络库处理网络通讯
  - 高效率网络采集
- 包含各种中间件接口
  - 实现反爬取
- 比BeautifulSoup更完善

### 主要部件

- 引擎
  - 控制其他部件
- 爬虫文件Spiders
  - 提取数据
  - 发送新请求（新网址）
- 调度器Scheduler
  - 排队
- ITEM
  - 保存处理数据
- 下载器
- 管道文件
  - 保存文件
    - 数据库(MySQL MongoDB Redis)
    - 本地(txt CSV Json)
- 中间件
  - 下载器中间件
  - 爬虫文件中间件

### 具体原理

1. Spiders->引擎，网址/请求
2. 引擎->调度器，网址，排队等待爬取
3. 调度器->引擎，网址
4. 引擎->下载器，请求
   1. 下载器用来下载网页源码
5. 网络->下载器->引擎->Spiders,响应
6. Spiders提取数据发送给引擎
7. 引擎发送数据给管道文件、管道文件保存数据

### 新建项目

我在pycharm里面一键下载了scrapy但是在文件夹里的cmd包括系统cmd都没有scrapy甚至pip，然后只能手动加了Path

![img](https://www.laych.com/wp-content/uploads/2021/04/image.png)

之后在win+R cmd里面通过

```
pip install -i https://pypi.douban.com/simple scrapy
```

又下载安装了一遍，但是twisted什么的没安，不知道行不行，反正pycharm里面已经安过了，而且版本都是2.5.0

然后就是在pycharm里面新建项目了，找一个文件夹，进去Shift右键，就可以打开文件夹下的cmd窗口，通过`scrapy startproject muSpider`命令新建一个项目

![img](https://www.laych.com/wp-content/uploads/2021/04/image-1-1024x521.png)

然后pycharm列表就更新了，文件里也可以看到

![img](https://www.laych.com/wp-content/uploads/2021/04/image-4.png)

![img](https://www.laych.com/wp-content/uploads/2021/04/image-5.png)

![img](https://www.laych.com/wp-content/uploads/2021/04/image-6.png)

到现在，一个新的Scrapy项目就新建完成了，这些东西同学已经发到群里了，但是我觉得有时间还是自己操作一遍比较好

### 创建爬虫

关键命令：`scrapy genspider [爬虫名] [域名]`,创建爬虫文件

```
cmd命令：
1.pwd
当前cmd所属文件夹
2.ls
当前文件夹内文件信息
```

![img](https://www.laych.com/wp-content/uploads/2021/04/image-7.png)

这个cfg文件，用于打包部署

运行命令`scrapy genspider museum jb.mil.cn`

这个命令是运行在这个界面下的cmd中的：

![img](https://www.laych.com/wp-content/uploads/2021/04/image-10.png)

运行结果：

![img](https://www.laych.com/wp-content/uploads/2021/04/image-8.png)

![img](https://www.laych.com/wp-content/uploads/2021/04/image-9-1024x81.png)

生成的museum.py就是新建的爬虫文件

注意事项：

- 爬虫名不能和项目名一样
- Spiders文件夹里面存放的就是爬虫文件
- 中间件文件涉及反爬、代理
- 管道用于保存数据
- setting配置文件
  - 比如ROBOTSTXT_OBEY = TRUE/False #是否遵守ROBOTS协议

![img](https://www.laych.com/wp-content/uploads/2021/04/image-11.png)

![img](https://www.laych.com/wp-content/uploads/2021/04/image-12-1024x418.png)

耐克这个真的搞(www.nike.com/robots.txt)

### 爬虫文件museum.py

默认代码：

```
import scrapy #导入scrapy

class MuseumSpider(scrapy.Spider): #创建爬虫类，继承自scrapy.Spider，最基础的类
    name = 'museum' #爬虫名，必须唯一
    allowed_domains = ['jb.mil.cn'] #允许采集的域名
    start_urls = ['http://jb.mil.cn/'] #开始采集的网站，第一次采集的网站

    def parse(self, response): #解析相应数据，提取数据、网址等，这里的response就是网页源码
        pass #这里默认没写，需要自己写
```

之前说多Spiders文件作用是提取数据、发送新请求

### 分析网站（爬虫文件museum.py-def parse）

- 先填域名网址，然后重写pass，利用Selected选择器提取数据

Selectors选择器，本身基于parsel模块

- 正则表达式
- Xpath，从HTML中提取数据，一种语法
- CSS

#### XPath

- 可以在浏览器开发者工具找到所需结点的Xpath表达式，然后通过`xpath()`方法得到其内容，比如`response.xpath('xpath表达式')`
- xpath语法`www.w3school.com.cn/xpath`
- egde安装xpathhelper：https://www.cnblogs.com/watalo/p/13768986.html

#### Xpath简单语法：

- 获取title标签内的内容的xpath表达式
  - `//title/text()`,//title选择所有title结点，/text选择text文本
- .extract方法
  - `response.xpath('//title/text()').extract()`这样再稍修改就可以提取内容了，而且可以向数组一样选择顺序

`//tr/td[2]/text()`就是先找tr标签，再找下面的第二个td标签，提取文本

但是一般不会这么写，而是这样：

```
#提取IP PORT
selectors = response.xpath('//tr') #选择所有tr标签
for selector in selectors: #循环遍历tr标签下的td标签
    ip = selector.xpath('./td[2]/text()') #.这个点表示在当前结点继续选择
    port = selector.xpath('./td[2]/text()')

print(ip,port)
```

这么写是因为可能大的标签下的小标签不一样，可能对应不上

#### 运行爬虫

`scrapy crawl museum` 运行museum爬虫

`ip = selector.xpath('./td[2]/text()').get()` get()获取一个元素,getall()获取全部元素

#### 列表推导式爬取读个页面：

`start_urls = [f'http://jb.mil.cn/{page}' for page in range(1,999)]`注意最大页面要加一

#### 翻页操作：

`//a[@class="m=next_page"]/@href` 下一页页码

```
next_page = response.xpath('//a[@class="m=next_page"]/@href').get()
if next_page: #如果下一页存在，保证最后一页可以结束
    print(next_page)
```

拼接网址：

这两种一样：

```
next_url = 'https://www.xicidaili.com'+next_page
next_url = reponse.urljoin(next_page)
# 发出请求，Request是回调函数，递归循环，实现url的拼接
yield scrapy.Request(next_url,callback=self.parse) # 生成器
```

- Request()发出请求，类似requests.get()
- callback 是发出的请求得到的相应交给自己处理
- 回调函数不写括号

#### 保存数据

采用JSON格式对爬取的数据进行序列化，生成ip.json文件

```
scrapy crawl museum -o ip.json
```

采用CSV格式对爬取的数据进行序列化，生成ip.csv文件

```
scrapy crawl museum -o ip.csv
items = {
    'ip':ip,
    'port':port
}
yield items #保存数据
```