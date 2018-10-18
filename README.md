# auto_zimuzu
输入对应的电视剧节目号，去 http://www.zimuzu.tv 获取剧集列表并下载

## 使用
baseurl/剧集号/链接格式/feeds

例如 [http://118.24.4.20:5000/26779/magnet/feeds](http://118.24.4.20:5000/26779/magnet/feeds)

## 自己构建使用

进入`FlaskApp`文件夹创建docker image

```
docker build -t auto_zimuzu:v1 .
```

构建完成后运行

```
docker run --name zimuzu -d -p 5000:80 auto_zimuzu:v1
```

然后在浏览器里就可以运行啦
