import pyttsx3


def speakOffline(msg):
    engine = pyttsx3.init()
    engine.setProperty('voice', 'zh')  # 开启支持中文
    engine.setProperty('rate',130)
    pyttsx3.speak(msg)



speakOffline("就算你是金城武，也不能使用")