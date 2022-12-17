import cv2
import base64
import requests
def compareFace(image_path="/home/magicmirror/Desktop/pycharm_project_214/PythonProject/facecompare",
                image_name="compared.png"):
    cap = cv2.VideoCapture(0)
    print("start...")
    while (cap.isOpened()):
        ret, frame = cap.read()
        cv2.imwrite(image_path + "/" + image_name, frame)
        print("保存" + image_name + "成功!")
        break

    # 使用百度API
    ak = "kmM6KARrCmCnSMiPvb55fz8G"
    sk = "MsUqQHbSuBoHYDUyGuGi8TSKRtGiUW6s"
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=%s&client_secret=%s' % (
        ak, sk)
    response = requests.get(host)
    access_token = response.json()['access_token']

    pic1 = open("/home/magicmirror/Desktop/pycharm_project_214/PythonProject/facecompare/compared.png", "rb")
    pic1_base64 = str(base64.b64encode(pic1.read()), 'utf-8')
    pic1.close()
    pic2 = open("/home/magicmirror/Desktop/pycharm_project_214/PythonProject/facecompare/jcw.jpeg", "rb")
    pic2_base64 = str(base64.b64encode(pic2.read()), 'utf-8')
    pic2.close()
    pic3 = open("/home/magicmirror/Desktop/pycharm_project_214/PythonProject/facecompare/xmh.png", "rb")
    pic3_base64 = str(base64.b64encode(pic3.read()), 'utf-8')
    pic3.close()

    request_url = "https://aip.baidubce.com/rest/2.0/face/v3/match"

    # 与xmh比较
    params1 = [{"image": "" + pic1_base64 + "", "image_type": "BASE64", "face_type": "LIVE", " \
             ""quality_control": "LOW"}, {"image": "" + pic3_base64 + "", "image_type": "BASE64", " \
             ""face_type": "IDCARD", "quality_control": "LOW"}]
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/json'}
    response1 = requests.post(request_url, json=params1, headers=headers)
    print(response1.json()['result']['score'])
    if response1:
        score = response1.json()['result']['score']
        if score > 85:
            cap.release()
            return 91

    # 与jcw比较
    params2 = [{"image": "" + pic1_base64 + "", "image_type": "BASE64", "face_type": "LIVE", " \
                     ""quality_control": "LOW"}, {"image": "" + pic2_base64 + "", "image_type": "BASE64", " \
                     ""face_type": "IDCARD", "quality_control": "LOW"}]
    response2 = requests.post(request_url, json=params2, headers=headers)
    if response2:
        score = response2.json()['result']['score']
        if score > 85:
            cap.release()
            return 1000
        else:
            cap.release()
            return 0
compareFace()