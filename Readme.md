## 爬取programmableweb上api信息的爬虫

### 使用
安装好Scrapy环境后，打开终端依次执行如下命令

`scrapy crawl api_links`

`scrapy crawl api_info_links`

`scrapy crawl api_data`

最后再执行generate_api-csv文件

### 说明

**api_links** 爬取的链接如图红框所示，即所有api详情的链接，保存至**api_links.json**文件中

![](https://github.com/panxianhaoo/CrawlerOfProgrammableweb/raw/master/pics/api_links.png)

api_info_links爬取的则是上述链接中关于此api各种版本信息的链接，保存至**api_info_link.json**中

![](https://github.com/panxianhaoo/CrawlerOfProgrammableweb/raw/master/pics/api_info_links.png)

最后终于来到获取我们想要数据的地方，保存至**api_data.json**中

![](https://github.com/panxianhaoo/CrawlerOfProgrammableweb/raw/master/pics/api_data.png)

*步骤稍显麻烦，如果有更直接的方法请指教*

运行**generate_api-csv**，进行清理，原因主要是

1. api中的信息类别不一致(有些信息某些api没有)，需要进行剔除

2. 不是所有信息都需要，要取我们想要的数据，具体取了哪些数据请自行看代码

### 最后
由于需要做项目所以需要爬取programmableweb的数据，Github上并没有完全符合我需求的代码所以自己写了一个，很匆忙，本人并没有系统学习过scrapy，有错误是难免的，有错请指正或自行修改。

数据为2020年11月3日的数据

参考了https://github.com/zxp93/pw_crawler

