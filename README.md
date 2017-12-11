# EmailBridgeForIPReport
项目目标：
1. 该项目主要目标是为了替换dynamic dns服务，因为作者在使用dynamic dns的过程中，经常发现那些免费的dynamic dns服务经常会停止工作，而最终导致自己无法知道重新启动的设备的新的IP地址。
2. 唯一功能是通过设置一个中间email地址，作为互联网上的一个设备向email用户通知自己IP地址的手段。其作用和dynamic dns几乎一样，但dynamic dns有如下缺点：
    a. dynamic dns工作不稳定，有时候设备或者机器重新启动，其并不更新IP DNS。并且某一小撮国家对这种DNS服务进行了干扰攻击。这样就导致了我们在设备重新启动后无法通过DNS服务找到新的设备新的IP
    b. dynamic dns的更新频率并不能任意设置，很多设备的配置只允许最快在十分钟内才更新新的IP给DNS记录，而最终全互联网有效，则需要等待超过15分钟。太慢。

系统设计实现:
1. 系统每过一段时间，访问互联网上的某些IP报告网站，https://www.iplocation.net/, http://www.infosniper.net/;
2. 解析上一步获得的网站html内容,获得其回报的IP地址;
3. 把上一步骤获得的IP地址，和自己存储的老地址想比较，如果已经发生了变化，则加密或这明文的通过SMTP服务，传送到系统设置的email地址里面。
4. 每次系统重新启动的时候，自动执行第一到第三步。这样做可以克服上述的dynamic dns的第二个缺点：重新启动后，更新IP地址过慢。

2017.12.11

Clock ZHONG
