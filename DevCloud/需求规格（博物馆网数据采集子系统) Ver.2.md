## 1.导言

#### 1.1 目的
该文档介绍了博物馆网站信息采集子系统的功能需求和非功能需求，重点描述了系统的设计需求，将作为对该工具在概要设计阶段的设计输入。
本文档目标阅读对象为：
- 系统用户（其他子系统开发者）
- 本项目的设计、开发、测试、维护人员

#### 1.2 范围
该文档是根据需求导出目标系统的逻辑模型，准确回答“系统必须做什么”的问题，通过建立模型的方式来描述用户的需求，对目标系统提出完整、准确、清晰、具体的要求。

#### 1.3  版本更新信息

|修改编号|修改日期|修改位置|更新内容概述   |更新者      |
|----|----|:----|:------|:---|
| 001 | 4.20 | # | 建立基本框架并补完信息 | 类成昊  |
| 002 | 4.22 | 1，2，4 | 修改框架并增添内容 | 李晓腾 |

#### 1.4  项目地址
[博物馆网站信息采集子系统](https://github.com/yang71/first_group)

## 2.子系统定义
以下部分主要阐述项目来源、背景，项目要达到的目标以及系统整体结构。

#### 2.1 项目来源及背景
- 本项目是博物馆网站信息采集系统，主要功能包括数据爬取、数据加工、数据导入、数据更新等
- 由于博物馆网站众多，本产品致力于智能高效的搜集其他子系统需要的消息，如开馆时间、展品信息、展览信息、教育活动信息、学术研究信息等
- 删除不必要的信息，减少查询的工作量。
- 其他小组成员通过编辑筛选条件可以找出所需博物馆的信息，并且排除多余的垃圾信息，实现查找、阅读的高效与便捷。
- 筛选产品有筛选准确快速的优势、导入数据库查询定位快速准确、持续更新信息。

#### 2.2 项目要达到的目标
- 本项目设定的目标如下：
- 1.系统能够提供友好的用户界面，使操作人员的工作量最大限度的减少
- 2.系统具有良好的运行效率，能够高效的爬取信息，并进行加工处理
- 3.系统应有良好的可扩充性，可随时准备与其它小组的子系统进行对接
- 4.设计应具有灵活性，可配置，能够用于多家网站。
- 5.通过这个项目可以锻炼队伍，提高团队的开发能力和项目管理能力

#### 2.3 系统整体架构
![系统整体架构](https://shitu-query-bj.bj.bcebos.com/2021-04-22/02/93c3c686db645e3c?authorization=bce-auth-v1%2F7e22d8caf5af46cc9310f1e3021709f3%2F2021-04-21T18%3A10%3A34Z%2F300%2Fhost%2F3c4fd56ff2da87013b8b14237ad0aa123bf449cbb75a4bbc274dcaae1018efa8"系统整体架构")

## 3.环境配置

### 3.1 运行环境

#### 3.1.1 系统运行网络环境
- 本系统运用于小组成员内部的数据交流，通过网络进行数据传输，在建立的数据库中进行筛选，通过专用接口传输到app中，展示出来

#### 3.1.2 系统运行软件环境
- yCharm2018.3.1 PyCharm是一种Python IDE，带有一整套可以帮助用户在使用Python语言开发时提高其效率的工具，比如调试、语法高亮、Project管理、代码跳转、智能提示、自动完成、单元测试、版本控制。此外，该IDE提供了一些高级功能，以用于支持Django框架下的专业Web开发

### 3.2 语言
- Python3.7.5 Python是一种跨平台的计算机程序设计语言。 是一个高层次的结合了解释性、编译性、互动性和面向对象的脚本语言。最初被设计用于编写自动化脚本(shell)，随着版本的不断更新和语言新功能的添加，越多被用于独立的、大型项目的开发。本程序中主要利用python来进行网络爬虫

### 3.3 框架

#### 3.3.1 Scrapy框架简介

- Scrapy Scrapy是适用于Python的一个快速、高层次的屏幕抓取和web抓取框架，用于抓取web站点并从页面中提取结构化的数据。Scrapy用途广泛，可以用于数据挖掘、监测和自动化测试。 Scrapy吸引人的地方在于它是一个框架，任何人都可以根据需求方便的修改。它也提供了多种类型爬虫的基类，如BaseSpider、sitemap爬虫等，最新版本又提供了web2.0爬虫的支持。

#### 3.3.2 其他框架介绍

- Scrapy Engine(引擎)：负责Spider、ItemPipeline、Downloader、Scheduler中间的通讯，信号、数据传递等。
- Scheduler(调度器)：它负责接受引擎发送过来的Request请求，并按照一定的方式进行整理排列，入队，当引擎需要时，交还给引擎。
- Spider（爬虫）：它负责处理所有Responses,从中分析提取数据，获取Item字段需要的数据，并将需要跟进的URL提交给引擎，再次进入Scheduler(调度器)。
- Item Pipeline(管道)：它负责处理Spider中获取到的Item，并进行进行后期处理（详细分析、过滤、存储等）的地方。
- Downloader Middlewares（下载中间件）：一个可以自定义扩展下载功能的组件。
- Spider Middlewares（Spider中间件）：一个可以自定扩展和操作引擎和Spider中间通信的功能组件。

#### 3.3.3 框架工作流程

- 新建项目
  - 新建一个新的爬虫项目
- 明确目标
  - （编写items.py）：明确你想要抓取的目标
- 制作爬虫
  - （spiders/xxspider.py）：制作爬虫开始爬取网页
- 存储内容
  - （pipelines.py）：设计管道存储爬取内容

#### 3.3.4 创建框架工作实例

- 在pycharm中安装Scrapy所需要的包
  - 可以直接在setting中搜索scrapy下载，或者在pycharm中打开terminal通过输入命令pip install Scrapy来安装
- 创建一个scrapy项目
  - 在命令行终端输入Scrapy，若在命令行中显示版本等信息则证明安装成功，点击pycharm中file中的setting再点击project:下的interperter查看是否存在Scrapy包，以及观察上方project interpreter中的python版本是否正确

#### 3.3.5 scrapy框架的核心架构

- Scrapy引擎
  - 引擎是Scrapy架构的核心，负责数据和信号在组件间的传递
- 调度器
  - 存储带爬取的网址，并确定网址的优先级，决定下一次爬取的网址
- 下载中间件
  - 对引擎和下载器之间的通信进行处理（如设置代理、请求头等）
- 下载器
  - 对相应的网址进行高速下载，将互联网的响应返回给引擎，再由引擎传递给爬虫处理
- 爬虫中间件
  - 对引擎和爬虫之间的通信进行处理
- 爬虫
  - 对响应response进行处理，提取出所需的数据（可以存入items），也可以提取出接下来要爬取的网址
- 实体管道
  - 接收从爬虫中提取出来的item，并对item进行处理（清洗、验证、存储到数据库等）

## 4.功能需求规格说明

### 4.1 数据爬取：

爬取全国一级博物馆的网站信息，包括博物馆基本的介绍、参观信息（开放时间等）、展览信息、教育活动、经典藏品信息、学术研究信息等，对于展览信息可以定时更新。

#### 4.1.1 数据内容

- 主要的博物馆官网获取数据，包括藏品，教育活动，博物馆主要信息等。

#### 4.1.2 实现方法

- scrapy框架（见2.环境设置）

### 4.2 数据加工：

对于爬取的信息进行过滤和加工，抽取需要的内容。例如：对于展览页面，过滤掉无用信息，如页面广告，最终得到展览主题、展览时间、展览地点、展览介绍等信息，加工成能满足后续处理的形式。

#### 4.2.1 加工要求

- 对数据进行加工，去掉爬取过程中不合适的字符,存入数据库、
- 最好采用可配置的方式，能够用于多家博物馆网站的页面和内容

#### 4.2.2 实现方法

- Python
- MySQL

### 4.3 数据导入：

- 采用合适的方式保存抽取的数据，能够导入到数据库中。
  - [导入方法](https://blog.csdn.net/weixin_44540683/article/details/89973868)

### 4.4 数据更新：

支持数据的持续更新。例如：根据情况，每天或每周爬取一次新的数据，更新原有数据。

#### 4.4.1 分析要求

- 能够更新数据库中的内容，最好可以定时更新

#### 4.4.2 实现方法

- Python
- 部署到服务器

## 4.其他非功能需求
响应时间需求
-系统应能监测出各种非正常情况，如与设备的通信中断，无法连接数据库服务器等，避免出现长时间等待甚至无响应。

#### 4.1 安全需求
- 系统在传输数据时，必须保证数据的安全性
- 系统所提供的数据，必须符合道德伦理及法律要求

#### 4.2 可靠性需求
- 所有的数据都来自官方网站，以确保数据的正确性
- 支持大规模数据存储
- 系统的加载时间不大于5秒钟
- 系统支持的客户端人数为10人
- 系统运行过程中，不会发生内存泄漏和进程死锁
- 如果在运行过程中发生错误，系统一般不会回到发生错误前的状态
- 从系统运行过程中查找、修复错误的时间预期不超过1天

#### 4.3 开放性需求
- 系统应具有十分的灵活性，以适应将来功能扩展的需求
- 本系统运用于小组成员内部的数据交流，通过网络进行数据传输，在建立的数据库中进行筛选
- 管理员能轻松地对数据进行更新

#### 4.4 系统安全性需求
- 系统有严格的权限管理机制，有权限者方能进入修改程序和数据。需能够防止各类误操作可能造成的数据丢失，破坏。防止用户非法获取网页以及内容。