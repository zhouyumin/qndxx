## 青年大学习截图

### 思路

青年大学习结束页的文件名是固定名称即images/end.jpg

例如青年大学习网址是http://h5.cyol.com/special/daxuexi/10olekhqva3/index.html

则结束页是http://h5.cyol.com/special/daxuexi/10olekhqva3/images/end.jpg

所以知道了最新一期的青年大学习的url就能获得结束页截图

用Python爬虫去中青在线网站http://www.cyol.com 获取最新一期的青年大学习url

然后自己生成网页，再用手机访问就能搞定

## 使用说明

在当前项目下进入命令行

运行

``` powershell
pip install -r requirements.txt
```

等待相关库安装完成后运行

```powershell
python main.py
```

电脑直接访问localhost:8080就能查看截图，手机请和电脑在同一局域网中,访问电脑的ip加端口号8080查看截图

例如电脑的ipv4地址是192.168.1.115，则把网址192.168.1.115:8080发送到自己的微信点开就能查看

