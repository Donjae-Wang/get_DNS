## 简单说明

这个是很早之前因为要获取git还有coursera的DNS随手写的一个自用的小脚本，后来套了个GUI的壳

get_DNS主要是通过爬取ipaddress获得DNS的，大家悠着点用哈

随手写的获取网页DNS的小程序，本来计划加上测速...额...现在太忙了...再说吧🤦‍  

**点击GET未响应是因为GUI里面进度条的问题，那个后面修复，功能是正常的不影响，如果想看进度条可以点start那个bat文件，CLI里有正常的进度条**，CLI的进度条是正常的   

QSS是套用[[GTRONICK](https://github.com/GTRONICK)]的[Aqua](https://github.com/GTRONICK/QSS/blob/master/Aqua.qss)

**release**在[get_DNS](https://github.com/Donjae-Wong/git_dns/releases/tag/V1.0.0)   

release也是pyinstaller随手打包的，没有精简包，所以有点大，解压后直接点main.exe就可以运行  

如果打包成一个文件启动速度会比较慢，所以就去掉-F了，如果觉得找的比较麻烦可以点右键创建个快捷方式  

  

## **功能介绍**  

git_dns.py稍微修改下可以直接当CLI工具使用

**Domain Name**输入框输入想获取DNS的域名，点GET就可以获取了  

（ps：可以带上https://那些，不过最好去掉，可能会有bug，比如想要查bing的DNS，可以输入cn.bing.com，批量的话用空格隔开）

想**全选+复制**就**双击Copy**  

**Open Hosts Folder**就是打开Host文件夹，Win10和Mac应该可以正常运行  

**DNS Flush**就是Win10修改之后刷新DNS用的，Mac无效