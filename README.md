# MCSManager Auto-Restarter
这个项目是针对[MCSManager自动重启失效的Bug](https://github.com/MCSManager/MCSManager/issues/932)而制作的临时解决方案。它将会定期检测实例是否崩溃关闭，并自动重启。

# 注意事项
1. 这只是一个*临时的*解决方案，这意味着当MCSM修复了这个Bug之后，此程序将会毫无用处；
2. 使用此程序之前，您必须思考您是否经常手动停止实例。一旦您需要手动停止实例，必须提前暂停此程序；
3. 如果您的示例崩溃频率在1次/天以下的，不建议使用此程序；
4. 代码全是屎山，毕竟是临时的，能跑就行（bushi）

# 使用方式
1. 克隆本项目
   `git clone https://github.com/Zhou-Shilin/MCSMAR`
2. 打开`main.py`，填写配置。
3. 使用运行`main.py`
  
注：您不需要安装任何的第三方库，程序使用的都是Python3内置库。

# 附加功能
你可以通过修改代码来获得个性化的体验，如通知提醒功能：
![通知提醒截图](https://cdn.staticaly.com/gh/Zhou-Shilin/picx-images-hosting@master/20230719/D1A3A92E-21DF-4C6D-840B-8F0A18EECBC0.s3xiuhd8v28.webp)
![代码截图/notice.py](https://cdn.staticaly.com/gh/Zhou-Shilin/picx-images-hosting@master/20230719/A4BF41C5-ABA8-42A1-A297-0F1BEADB2F52.59lfy21cr6kg.webp)
![代码截图/main.py](https://cdn.staticaly.com/gh/Zhou-Shilin/picx-images-hosting@master/20230719/F30B99A4-C1E7-4573-8181-2F8B5E98C23F.3s8b81fbo5og.webp)
