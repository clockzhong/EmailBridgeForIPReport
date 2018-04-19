# EmailBridgeForIPReport
项目目标：
1. 该项目主要目标是为了替换dynamic dns服务，因为作者在使用dynamic dns的过程中，经常发现那些免费的dynamic dns服务会停止工作或者工作不正常，而最终导致自己无法知道重新启动的设备的新的IP地址。
2. 该项目的唯一功能是通过设置一个中间email地址，作为互联网上的一个设备向email用户通知自己IP地址的手段。其作用和dynamic dns几乎一样，但dynamic dns有如下缺点：

    a. dynamic dns工作不稳定，有时候设备或者机器重新启动，其并不更新IP DNS。并且地球上某一小撮反文明的组织会对这种互联网上的公共DNS服务进行了干扰攻击。这样就导致了我们在设备重新启动后无法通过DNS域名找到设备新的IP
    
    b. dynamic dns的更新频率并不能任意设置，很多设备的配置只允许最快在十分钟内才更新新的IP给DNS记录，而最终全互联网有效，则需要等待超过15分钟。太慢。

系统设计实现:
1. 系统每过一段时间，访问互联网上的某些IP报告网站，https://www.iplocation.net/, http://www.infosniper.net/, http://ip138.com/;
2. 解析上一步获得的网站html内容,获得其回报的IP地址;
3. 把上一步骤获得的IP地址，和自己存储的老地址相比较，如果已经发生了变化，则加密或明文地通过SMTP服务，传送到系统设置的email地址里面。
4. 每次系统重新启动的时候，自动执行第一到第三步。这样做可以克服上述的dynamic dns的第二个缺点：重新启动后，更新IP地址过慢。

使用方法：
1. 准备工作：

   a. 一个email帐号地址

   b. 上面那个email帐号地址对应的SMTP密码，多数情况下，等同于email帐号的Pop3密码

   c. email帐号对应的的SMTP的服务器IP地址或者域名，比如mail.163.com对应的SMTP服务器是：smtp.163.com

   d. email帐号对应的的SMTP的服务端口，多数情况下都是25

2. 执行如下命令：
   notifyIP.py YouEmailAddress YouPasswordForYourEmailAccount YouSMTPServer YouSMTPPort

如果需要在服务器设备上每次启动时都自动运行notifyIP.py，则可以参考stackoverflow站点上这个session的第二个方案。

https://stackoverflow.com/questions/24518522/run-python-script-at-startup-in-ubuntu

我总结为如下两步：

1. sudo crontab -e

2. 在最后，增加一行如下命令：

   @reboot python /your_path_to_notifyIP/notifyIP.py YouEmailAddress YouPasswordForYourEmailAccount YouSMTPServer YouSMTPPort &

上述步骤在Ubuntu16.04 LTS环境中验证工作正常。

2017.12.12

钟钟
