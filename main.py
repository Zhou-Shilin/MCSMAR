import api
import time
import os
from log_writer import log

# 配置
apikey = "" # 我的信息-API接口秘钥
uuid = "" # 实例-高级设置
remote_uuid = "" # 实例-高级设置
url = "" # 你的面板url 带http(s)://
time_before_restart = 10 # 检测到实例停止之后等待多少秒重启 不建议设置为小于3s
detection_frequecy = 60 # 检测频率

try:
    os.remove("log.txt")
except:
    prin("日志文件不存在！正在创建……")

log("Start, MSCMAR 1.3 / BaimoQilin 2023")
print("Start, MSCMAR 1.3 / BaimoQilin 2023")
print("Ctrl+C 退出程序")

while True:
    status = api.get_status(url, uuid, remote_uuid, apikey)

    if status == 0:
        tempLog = "[" + time.ctime() + "] (main.py) 检测到实例已停止, " + time_before_restart + "s后重启！"
        log(tempLog)
        time.sleep(time_before_restart)
        isStartedSuccessful = api.start_app(url, uuid, remote_uuid, apikey)
        if isStartedSuccessful == True:
            tempLog = "[" + time.ctime() + "] (main.py) 实例启动成功！"
            log()
        else:
            tempLog = "[" + time.ctime() + "] (main.py) 实例启动失败！"
            log(tempLog)
    else:
        pass

    time.sleep(detection_frequecy)
