from LIB.P2P import BookPage
from selenium import webdriver
from hytest import *
import time

from cases.ddt import C00003x

force_tags = ['login_test']
class UI_0101:
    name = '检查操作菜单 UI_0101'

    # C00003x.ddt_cases()

    # 初始化方法
    def setup(self):
        self.driver=webdriver.Chrome(r'C:\Users\86150\Desktop\chromedriver.exe')
        self.driver.get("http://localhost/")
        mainWindow = self.driver.current_window_handle
        GSTORE['mainWindow'] = mainWindow
        INFO('进入首页')
        self.driver.implicitly_wait(10)
        self.P2P=BookPage(self.driver)


    # 清除方法
    def teardown(self):
       self.driver.quit()

    def teststeps(self):
        STEP(1, '注册图书馆')
        # self.P2P.ZC()
        # username, password, cfpassword ,yzm, info = self.para
        #
        # if username is not None:
        #     self.P2P.userinput(username)
        #
        # if password is not None:
        #     self.P2P.passwordinput(password)
        #
        # if cfpassword is not None:
        #     self.P2P.passwordinput(cfpassword)
        #
        # if yzm is not None:
        #     self.P2P.passwordinput(yzm)
        #
        # notify = self.P2P.switch_to.alert.text
        #
        # CHECK_POINT('弹出提示', notify == info)
        #
        #
        #
        # self.P2P.zcsubmitclick()
        # self.P2P.TCDL()


        self.P2P.ZC()
        self.P2P.userinput("2005050206")
        self.P2P.passwordinput("123456")
        self.P2P.cfpasswordinput("123456")
        self.P2P.zym("1234")
        self.P2P.zcsubmitclick()
        SELENIUM_LOG_SCREEN(self.driver, width='100%')
        self.P2P.TCDL()


        # -------------
        self.P2P.ZC()
        self.P2P.userinput("2005050202")
        self.P2P.passwordinput("123456")
        self.P2P.cfpasswordinput("123456")
        self.P2P.zym("1234")
        self.P2P.zcsubmitclick()
        self.P2P.TCDL()
        # --------------------

        self.P2P.ZC()
        self.P2P.userinput("2003030208")
        self.P2P.passwordinput("123456")
        self.P2P.cfpasswordinput("123456")
        self.P2P.zym("1234")
        self.P2P.zcsubmitclick()
        self.P2P.TCDL()

        # ----------------------
        self.P2P.ZC()
        self.P2P.userinput("2005050203")
        self.P2P.passwordinput("123456")
        self.P2P.cfpasswordinput("123456")
        self.P2P.zym("1234")
        self.P2P.zcsubmitclick()
        self.P2P.TCDL()

        STEP(2,'登录密码为空')
        time.sleep(1)
        self.P2P.DL()
        self.P2P.dluserinput("2005050206")
        self.P2P.dlpasswordinput("")
        self.P2P.zym("1234")
        self.P2P.dlsubmitclick()
        SELENIUM_LOG_SCREEN(self.driver, width='100%')

        STEP(3, '账户为空')
        time.sleep(1)
        self.P2P.DL()
        self.P2P.dluserinput("")
        self.P2P.dlpasswordinput("123456")
        self.P2P.zym("1234")
        self.P2P.dlsubmitclick()
        SELENIUM_LOG_SCREEN(self.driver, width='100%')

        STEP(4, '验证码为空')
        time.sleep(1)
        self.P2P.DL()
        self.P2P.dluserinput("2005050206")
        self.P2P.dlpasswordinput("123456")
        self.P2P.zym("")
        self.P2P.dlsubmitclick()
        SELENIUM_LOG_SCREEN(self.driver, width='100%')

        STEP(5, '正常输入登录')
        time.sleep(1)
        self.P2P.DL()
        self.P2P.dluserinput("2005050206")
        self.P2P.dlpasswordinput("123456")
        self.P2P.zym("1234")
        self.P2P.dlsubmitclick()
        SELENIUM_LOG_SCREEN(self.driver, width='100%')

        # STEP(3,'修改密码')
        # time.sleep(1)
        # self.P2P.aqzx()
        # self.P2P.ysmm("123456")
        # self.P2P.xmm("123456")
        # self.P2P.qrxmm("123456")
        # self.P2P.submit()

        STEP(6,'查看我要融资抵押标详情')
        mainWindow= GSTORE['mainWindow']
        self.P2P.switch_to(mainWindow)
        time.sleep(1)
        self.P2P.wyrz()
        self.P2P.dybckxq()
        self.P2P.gywm()
        self.P2P.xwzx()
        self.P2P.lxwm()
        self.P2P.mcjs()
        self.P2P.sfgz()
        self.P2P.bzzx()
        self.P2P.ptgg()
        self.P2P.aqzx()
        self.P2P.switch_to(mainWindow)
        STEP(7, '发布抵押标')
        time.sleep(1)
        self.P2P.wyrz()
        self.P2P.fb1()
        self.P2P.wyrz_bt('asdasd')#标题:
        self.P2P.wyrz_nll('1111')#年利率:
        self.P2P.wyrz_jkyt('3')#借款用途
        self.P2P.wyrz_tjdwt()#统计单位 天
        self.P2P.wyrz_jkqs('11')#借款期限: 1或者12
        self.P2P.wyrz_hkfs('1')#还款方式0或者1
        self.P2P.wyrz_yssj('3')#有效时间
        self.P2P.wyrz_kmm()#密码标状态:
        self.P2P.wyrz_srmm('123456')#密码
        self.P2P.wyrz_zdtbje('100')#最低投标金额
        self.P2P.wyrz_zgtbje('1000')#最高投标金额
        self.P2P.wyrz_jkje('11111111')#借款金额:
        self.P2P.wyrz_tbjl1()#投标奖励
        self.P2P.wyrz_tbjl1input('1234441123')#按金额奖励
        self.P2P.wyrz_xssm('asjfjbsfbasjbfk')#详细说明
        self.P2P.wyrz_yzm('1234')#验证码
        SELENIUM_LOG_SCREEN(self.driver, width='100%')#截图
        self.P2P.wyrz_qrtj()#确认提交





        STEP(8,'查看我要融资质押标详情')
        time.sleep(1)
        self.P2P.wyrz()
        self.P2P.zybckxq()
        self.P2P.gywm()
        self.P2P.xwzx()
        self.P2P.lxwm()
        self.P2P.mcjs()
        self.P2P.sfgz()
        self.P2P.bzzx()
        self.P2P.ptgg()
        self.P2P.aqzx()

        STEP(9, '发布质押标')
        time.sleep(1)
        self.P2P.wyrz()
        self.P2P.fb2()
        self.P2P.wyrz_bt('asdasd')#标题
        self.P2P.wyrz_nll('1111')#年利率
        self.P2P.wyrz_jkyt('3')#借款用途
        self.P2P.wyrz_tjdwt()#统计单位
        self.P2P.wyrz_jkqs('9')#借款期限
        self.P2P.wyrz_hkfs('1')#还款方式
        self.P2P.wyrz_yssj('20')#有效时间
        self.P2P.wyrz_kmm()#密码标状态:
        self.P2P.wyrz_srmm('123456')#密码
        self.P2P.wyrz_zdtbje('50')#最低投标金额:
        self.P2P.wyrz_zgtbje('500')#最高投标金额:
        self.P2P.wyrz_jkje('11111111')#借款金额
        self.P2P.wyrz_tbjl1()#投标奖励:
        self.P2P.wyrz_tbjl1input('1234441123')#按金额奖励
        self.P2P.wyrz_xssm('asjfjbsfbasjbfk')#详细说明
        self.P2P.wyrz_yzm('1234')#验证码

        self.P2P.wyrz_qrtj()#确认提交
        SELENIUM_LOG_SCREEN(self.driver, width='10%')#


        STEP(9, '我要投资')
        self.P2P.wytz()
        self.P2P.wytz_tz()
        self.P2P.wytz_ljtz()#立即投资
        self.P2P.wytz_tbje('30')#投资金额
        self.P2P.wytz_zfmm('123456')#支付密码
        self.P2P.wytz_yzm('1234')#验证码
        self.P2P.wytz_qrtj()#确认提交








