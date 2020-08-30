# SanforProxy
基于深信服vpn的web代理登录接口实现的第三方代理客户端

由于本校的教务系统需要学校vpn才能登录，为便于在外部linux服务器访问内网api我开发了这个应用

目前仅能支持api调用，不能进行网页浏览

配置文件:config.py
```python
USER = ""
PWD = ""

URL = "" # 登录的url
PROXY_NAME = "" # 深信服的web代理vpn服务器的域名
PROXY_PORT = 0 # 端口
VERIFY = False # 是否验证证书
```
运行
```bash
mitmweb -k -s main.py
```