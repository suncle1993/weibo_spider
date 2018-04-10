### login bug

微博selenium模拟登录bug

> 验证版本：
>
> chromedriver=2.37 and os = ubuntu 16.04 LTS

如果不增加chrome_options会出现chromedriver加载失败的报错，报错如下：

```
Traceback (most recent call last):
  File "/root/PycharmProjects/smart_login/sina_login/sina_login_by_selenium.py", line 54, in <module>
    cookies = login(name_input, passwd_input, url)
  File "/root/PycharmProjects/smart_login/sina_login/sina_login_by_selenium.py", line 14, in login
    driver = webdriver.Chrome('/root/qk_python/python/data/collect/weibo_spider/priv/chromedriver')
  File "/usr/local/lib/python3.5/dist-packages/selenium/webdriver/chrome/webdriver.py", line 75, in __init__
    desired_capabilities=desired_capabilities)
  File "/usr/local/lib/python3.5/dist-packages/selenium/webdriver/remote/webdriver.py", line 154, in __init__
    self.start_session(desired_capabilities, browser_profile)
  File "/usr/local/lib/python3.5/dist-packages/selenium/webdriver/remote/webdriver.py", line 243, in start_session
    response = self.execute(Command.NEW_SESSION, parameters)
  File "/usr/local/lib/python3.5/dist-packages/selenium/webdriver/remote/webdriver.py", line 312, in execute
    self.error_handler.check_response(response)
  File "/usr/local/lib/python3.5/dist-packages/selenium/webdriver/remote/errorhandler.py", line 242, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.WebDriverException: Message: unknown error: Chrome failed to start: exited abnormally
  (Driver info: chromedriver=2.37.544315 (730aa6a5fdba159ac9f4c1e8cbc59bf1b5ce12b7),platform=Linux 4.13.0-38-generic x86_64)
```

同时需要在get操作之前增加`driver.set_window_size(1124, 850)`进行窗口大小的预置（合适的值即可），否则得到的WebElement的状态is_displayed为False，即不可见，导致进行clear操作和send_keys操作时出现异常。异常如下：

```
Traceback (most recent call last):
  File "/root/PycharmProjects/smart_login/sina_login/sina_login_by_selenium.py", line 61, in <module>
    cookies = login(name_input, passwd_input, url)
  File "/root/PycharmProjects/smart_login/sina_login/sina_login_by_selenium.py", line 27, in login
    name_field.clear()
  File "/usr/local/lib/python3.5/dist-packages/selenium/webdriver/remote/webelement.py", line 95, in clear
    self._execute(Command.CLEAR_ELEMENT)
  File "/usr/local/lib/python3.5/dist-packages/selenium/webdriver/remote/webelement.py", line 628, in _execute
    return self._parent.execute(command, params)
  File "/usr/local/lib/python3.5/dist-packages/selenium/webdriver/remote/webdriver.py", line 312, in execute
    self.error_handler.check_response(response)
  File "/usr/local/lib/python3.5/dist-packages/selenium/webdriver/remote/errorhandler.py", line 242, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.InvalidElementStateException: Message: invalid element state: Element is not currently interactable and may not be manipulated
  (Session info: headless chrome=65.0.3325.162)
  (Driver info: chromedriver=2.37.544315 (730aa6a5fdba159ac9f4c1e8cbc59bf1b5ce12b7),platform=Linux 4.13.0-38-generic x86_64)
```

处理方法参考PhantomJs 的一个issue：https://github.com/ariya/phantomjs/issues/11637

### weibo cookies

cookies是一个字典组成的列表，对应的json字段为：

```json
[
　　{
　　　　"domain":".weibo.com",
　　　　"secure":false,
　　　　"value":"17*******95",
　　　　"expiry":1524120668,
　　　　"path":"/",
　　　　"httpOnly":false,
　　　　"name":"un"
　　},
　　{
　　　　"domain":".weibo.com",
　　　　"secure":false,
　　　　"value":"1523256667",
　　　　"path":"/",
　　　　"httpOnly":false,
　　　　"name":"SSOLoginState"
　　},
　　{
　　　　"domain":".weibo.com",
　　　　"secure":false,
　　　　"value":"e64ac1749cd3c5c902090afa644b2005",
　　　　"path":"/",
　　　　"httpOnly":false,
　　　　"name":"login_sid_t"
　　},
　　{
　　　　"domain":".weibo.com",
　　　　"secure":false,
　　　　"value":"0033WrSXqPxfM725Ws9jqgMF55529P9D9Wh1c52cTZxmZGynR7Exju6P5JpX5K2hUgL.FoecSK-fS0qfehe2dJLoI7XLxK-L1K-L128.dciL",
　　　　"expiry":1554792667.968006,
　　　　"path":"/",
　　　　"httpOnly":false,
　　　　"name":"SUBP"
　　},
　　{
　　　　"domain":".weibo.com",
　　　　"secure":false,
　　　　"value":"715037198114.4742.1523256662497",
　　　　"path":"/",
　　　　"httpOnly":false,
　　　　"name":"Apache"
　　},
　　{
　　　　"domain":".weibo.com",
　　　　"secure":false,
　　　　"value":"-",
　　　　"path":"/",
　　　　"httpOnly":false,
　　　　"name":"_s_tentry"
　　},
　　{
　　　　"domain":".weibo.com",
　　　　"secure":false,
　　　　"value":"0QS56w4__4ADzG",
　　　　"expiry":1554792667.968016,
　　　　"path":"/",
　　　　"httpOnly":false,
　　　　"name":"SUHB"
　　},
　　{
　　　　"domain":".weibo.com",
　　　　"secure":false,
　　　　"value":"_2A253z30LDeRhGeVI7lcU9yjJyz-IHXVUvenDrDV8PUNbmtBeLVL9kW9NT2uPIUWRgHFPE3AuKFXEZERx4hUh5nBy",
　　　　"path":"/",
　　　　"httpOnly":true,
　　　　"name":"SUB"
　　},
　　{
　　　　"domain":"weibo.com",
　　　　"secure":false,
　　　　"value":"b611234b8b979b26|undefined",
　　　　"expiry":1523257250,
　　　　"path":"/",
　　　　"httpOnly":false,
　　　　"name":"WBStorage"
　　},
　　{
　　　　"domain":"weibo.com",
　　　　"secure":false,
　　　　"value":"d45b2deaf680307fa1ec077ca90627d1",
　　　　"path":"/",
　　　　"httpOnly":false,
　　　　"name":"YF-V5-G0"
　　},
　　{
　　　　"domain":".weibo.com",
　　　　"secure":false,
　　　　"value":"6",
　　　　"expiry":1523861468.314959,
　　　　"path":"/",
　　　　"httpOnly":false,
　　　　"name":"wvr"
　　},
　　{
　　　　"domain":"weibo.com",
　　　　"secure":false,
　　　　"value":"ad83bc19c1269e709f753b172bddb094",
　　　　"path":"/",
　　　　"httpOnly":false,
　　　　"name":"YF-Ugrow-G0"
　　},
　　{
　　　　"domain":".weibo.com",
　　　　"secure":false,
　　　　"value":"ApXffXU5UHGGs-13Vzzw7YQaVApaegVR5dFhLupDmvs4yYATr0zMWzNN0sQFqJlPo-8BMrVI9cGEeu_HisyFGyQ.",
　　　　"expiry":1838616667.967975,
　　　　"path":"/",
　　　　"httpOnly":true,
　　　　"name":"SCF"
　　},
　　{
　　　　"domain":".weibo.com",
　　　　"secure":false,
　　　　"value":"1554792666",
　　　　"expiry":1554792666.968049,
　　　　"path":"/",
　　　　"httpOnly":false,
　　　　"name":"ALF"
　　},
　　{
　　　　"domain":".weibo.com",
　　　　"secure":false,
　　　　"value":"1523256662605:1:1:1:715037198114.4742.1523256662497:",
　　　　"expiry":1554360662,
　　　　"path":"/",
　　　　"httpOnly":false,
　　　　"name":"ULV"
　　},
　　{
　　　　"domain":".weibo.com",
　　　　"secure":false,
　　　　"value":"SSL",
　　　　"path":"/",
　　　　"httpOnly":false,
　　　　"name":"cross_origin_proto"
　　},
　　{
　　　　"domain":".weibo.com",
　　　　"secure":false,
　　　　"value":"715037198114.4742.1523256662497",
　　　　"expiry":1838616662,
　　　　"path":"/",
　　　　"httpOnly":false,
　　　　"name":"SINAGLOBAL"
　　}
]
```

