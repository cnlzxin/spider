爬虫: 爬取英文官方文档, 统计其中英语单词出现的频率, 并按降序排列, 这里以Python的文档为样本, 希望能成为英语学习者的好帮手


下载: 
```bash
$ git clone https://github.com/lzxin1/spider.git
```

运行:
```bash
$ cd ./spider/
$ scrapy crawl docs	# 生成 docs.json 文件
```

数据处理:
```bash
$ python3 docs2dict.py	# 在同目录下生成 dict_.json 文件
```


## TO DO

- 可以爬取任意英文网站文档
- 数据获取和处理一步到位
- 使用Web展示(`Django`)
- 添加词根/义, 删除简单词
- 多线程 && 代理池
- 分布式