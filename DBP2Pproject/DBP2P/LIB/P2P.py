from selenium.webdriver.common.by import By
from LIB.BasePage import BasePage
# from selenium.webdriver.support.ui import Select

class BookPage(BasePage):
    # 元素定位，
    P2P_ZC = (By.CSS_SELECTOR, 'body > header > div > div > div.info.span6 > a:nth-child(2)')
    # Index = (By.CSS_SELECTOR, 'body > header > div > div > div.info.span6 > a:nth-child(2)')
    P2P_DL =(By.CSS_SELECTOR, 'body > header > div > div > div.info.span6 > a:nth-child(1)')
    P2P_tcdl =(By.CSS_SELECTOR, 'body > header > div > div > div.info.span6 > a:nth-child(2)')

    P2Pzc_username = (By.CSS_SELECTOR, '#myform > div > div:nth-child(1) > div > input')
    P2Pzc_userpassword=(By.CSS_SELECTOR, '#myform > div > div:nth-child(2) > div > input')
    P2Pzc_CFuserpassword = (By.CSS_SELECTOR, '#myform > div > div:nth-child(3) > div > input.span12')
    YZM = (By.CSS_SELECTOR, '#CaptchaInputText')
    P2Pzc_submit_loc = (By.CSS_SELECTOR, '#myform > div > button')

    P2Pdl_username = (By.XPATH, '/html/body/div[1]/div[2]/div/div/form/div/div[1]/div/input')
    P2Pdl_userpassword = (By.XPATH, '/html/body/div[1]/div[2]/div/div/form/div/div[2]/div/input')
    P2Pdl_submit_loc = (By.CSS_SELECTOR, 'body > div.layout > div.container > div > div > form > div > button')
    # 点击安全中心

    P2P_aqzx= (By.XPATH, '/html/body/div[1]/div[1]/div/div/div/div/ul/li[6]/a')
    P2P_ysmm= (By.XPATH, '//*[@id="content"]/form/table/tbody/tr[1]/td[2]/input')
    P2P_xmm= (By.XPATH, '//*[@id="content"]/form/table/tbody/tr[2]/td[2]/input')
    P2P_qrxmm= (By.XPATH, '//*[@id="content"]/form/table/tbody/tr[3]/td[2]/input')
    P2Paqzx_submit_loc= (By.XPATH, '//*[@id="content"]/form/table/tbody/tr[4]/td[2]/button')
    # 点击修改交易密码
    P2P_xgjymm = (By.CSS_SELECTOR, 'ul.center_secondary > li:nth-child(2) > a')

    # 点击我要融资
    P2P_wyrz = (By.XPATH, '/html/body/header/div/nav/div/div/ul[1]/li[3]/a')
    # 查看抵押标详情
    P2P_wyrz_dybckxq = (By.CSS_SELECTOR, 'body > div.layout > div.row-fluid > div > div:nth-child(1) > dl > dd > p.view > a:nth-child(1)')
    # 查看质押标详情
    P2P_wyrz_zybckxq = (By.CSS_SELECTOR, 'body > div.layout > div.row-fluid > div > div:nth-child(2) > dl > dd > p.view > a:nth-child(1)')
    # 点击发布1
    P2P_wyrz_fb1 = (By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/dl/dd/p[2]/a[2]')
    # 点击发布2
    P2P_wyrz_fb2 = (By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/dl/dd/p[2]/a[2]')

    # 查看关于我们
    P2P_wyrz_gywm = (By.CSS_SELECTOR, 'body > div.layout > div.sub-nav > div > div > div > div > ul > li:nth-child(1) > a')
    # 查看新闻中心
    P2P_wyrz_xwzx = (By.CSS_SELECTOR, 'body > div.layout > div.sub-nav > div > div > div > div > ul > li:nth-child(2) > a')
    # 查看联系我们
    P2P_wyrz_lxwm = (By.CSS_SELECTOR, 'body > div.layout > div.sub-nav > div > div > div > div > ul > li:nth-child(3) > a')
    # 查看名词解释
    P2P_wyrz_mcjs = (By.CSS_SELECTOR, 'body > div.layout > div.sub-nav > div > div > div > div > ul > li:nth-child(4) > a')
    # 查看收费规则
    P2P_wyrz_sfgz = (By.CSS_SELECTOR, 'body > div.layout > div.sub-nav > div > div > div > div > ul > li:nth-child(5) > a')
    # 查看帮助中心
    P2P_wyrz_bzzx = (By.CSS_SELECTOR, 'body > div.layout > div.sub-nav > div > div > div > div > ul > li:nth-child(6) > a')
    # 查看平台公告
    P2P_wyrz_ptgg = (By.CSS_SELECTOR, 'body > div.layout > div.sub-nav > div > div > div > div > ul > li:nth-child(7) > a')
    # 查看安全保障
    P2P_wyrz_aqbz = (By.CSS_SELECTOR, 'body > div.layout > div.sub-nav > div > div > div > div > ul > li:nth-child(8) > a')

    # 抵押标表单

    # 标题body > div.layout > div.row-fluid > div > form > table > tbody:nth-child(2) > tr > td:nth-child(2) > input
    P2P_wyrz_bt =(By.CSS_SELECTOR,'body > div.layout > div.row-fluid > div > form > table > tbody:nth-child(2) > tr > td:nth-child(2) > input')
    # *年利率:
    P2P_wyrz_nll = (By.XPATH, '/html/body/div[1]/div[2]/div/form/table/tbody[2]/tr/td[2]/div/input')
    # 借款用途
    P2P_wyrz_jkyt = (By.XPATH, '/html/body/div[1]/div[2]/div/form/table/tbody[3]/tr/td[2]/select')


    # 统计单位 按月
    P2P_wyrz_tjdwy = (By.XPATH, '/html/body/div[1]/div[2]/div/form/table/tbody[4]/tr/td[2]/label[1]')
    # 统计单位 按天
    P2P_wyrz_tjdwt= (By.XPATH, '/html/body/div[1]/div[2]/div/form/table/tbody[4]/tr/td[2]/label[2]')
    # 借款期限
    P2P_wyrz_jkqx = (By.XPATH, '//*[@id="deadline1"]')
    # 还款方式:
    P2P_wyrz_hkfx = (By.XPATH, '/html/body/div[1]/div[2]/div/form/table/tbody[6]/tr/td[2]/select')
    # 有效时间:
    P2P_wyrz_yssj = (By.XPATH, '/html/body/div[1]/div[2]/div/form/table/tbody[7]/tr/td[2]/select')

    # 开密码
    P2P_wyrz_kmm = (By.XPATH, '/html/body/div[1]/div[2]/div/form/table/tbody[8]/tr/td[2]/label[2]')
    # 输入密码
    P2P_wyrz_srmm = (By.XPATH, '//*[@id="pass1"]')
    # 最低投标金额:
    P2P_wyrz_zdtbje = (By.XPATH, '/html/body/div[1]/div[2]/div/form/table/tbody[10]/tr/td[2]/select')
    # 最高投标金额:
    P2P_wyrz_zgtbje = (By.XPATH, '/html/body/div[1]/div[2]/div/form/table/tbody[11]/tr/td[2]/select')
    # *借款金额
    P2P_wyrz_jkje = (By.XPATH, '/html/body/div[1]/div[2]/div/form/table/tbody[12]/tr/td[2]/div/input[1]')
    # 投标奖励按金额奖励
    P2P_wyrz_tbjl1 = (By.CSS_SELECTOR, 'body > div.layout > div.row-fluid > div > form > table > tbody:nth-child(14) > tr > td:nth-child(2) > div:nth-child(3)>label>div>span')
    P2P_wyrz_tbjl1input = (By.CSS_SELECTOR, '#reward_1')

    # 投标奖励按比例奖励
    P2P_wyrz_tbjl2 = (By.XPATH, 'body > div.layout > div.row-fluid > div > form > table > tbody:nth-child(14) > tr > td:nth-child(2) > div:nth-child(4)>label>div>span')
    P2P_wyrz_tbjl2input = (By.CSS_SELECTOR, '#reward_2')
    # 详细说明:
    P2P_wyrz_xssm = (By.CSS_SELECTOR, 'body > div.layout > div.row-fluid > div > form > table > tbody:nth-child(16)>tr>td>div>div>iframe')

    # 输入验证码
    P2P_wyrz_yzm = (By.CSS_SELECTOR, 'body > div.layout > div.row-fluid > div > form > div:nth-child(3) > input')

    # 确认提交
    P2P_wyrz_qrtj = (By.CSS_SELECTOR, 'body > div.layout > div.row-fluid > div > form > div:nth-child(4) > button')

    # 投资
    P2P_wytz_tz = (By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/div[2]/div[1]/div/div[1]/div[2]/div/div[1]/a')
    # 立即投资
    P2P_wytz_ljtz = (By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[1]/div/div[2]/div[3]/div/a')

    # 点击我要投资
    P2P_wytz = (By.XPATH, '/html/body/header/div/nav/div/div/ul[1]/li[2]/a')
    # 投标金额
    P2P_wytz_tbje = (By.CSS_SELECTOR, '#tEnder > div.modal-body > div:nth-child(2)>form>dl>dd>span>input')
    # 支付密码
    P2P_wytz_zfmm = (By.XPATH, '//*[@id="tEnder"]/div[2]/div[2]/form/dl/dd[2]/input')
    # 验证码
    P2P_wytz_yzm = (By.XPATH, '//*[@id="CaptchaInputText"]')
    # 我要投资确认提交
    P2P_wytz_qrtj = (By.XPATH, '//*[@id="tEnder"]/div[2]/div[2]/form/dl/dd[5]/button')
    # 点击注册
    def ZC(self):
        self.find_ele(*self.P2P_ZC).click()
    # 点击登录
    def DL(self):
        self.find_ele(*self.P2P_DL).click()
    # 退出登录
    def TCDL(self):
        self.find_ele(*self.P2P_tcdl).click()
    # 注册账户
    def userinput(self,keyword):
        self.find_ele(*self.P2Pzc_username).send_keys(keyword)
    # 注册密码
    def passwordinput(self,keyword):
        self.find_ele(*self.P2Pzc_userpassword).send_keys(keyword)

    # 注册重复密码
    def cfpasswordinput(self, keyword):
        self.find_ele(*self.P2Pzc_CFuserpassword).send_keys(keyword)
    #验证码
    def zym(self, keyword):
        self.find_ele(*self.YZM).send_keys(keyword)
    # 注册提交操作
    def zcsubmitclick(self):
        self.find_ele(*self.P2Pzc_submit_loc).click()

 # ------------------------------------------------------
    # 登录账户
    def dluserinput(self,keyword):
        self.find_ele(*self.P2Pdl_username).send_keys(keyword)
    # 登录密码
    def dlpasswordinput(self,keyword):
        self.find_ele(*self.P2Pdl_userpassword).send_keys(keyword)
    # 登录提交
    def dlsubmitclick(self):
        self.find_ele(*self.P2Pdl_submit_loc).click()
# ---------------------------------


    # 点击安全中心
    def aqzx(self):
        self.find_ele(*self.P2P_aqzx).click()
    # 修改登录密码
    # 输入原始密码
    def ysmm(self,keyword):
        self.find_ele(*self.P2P_ysmm).send_keys(keyword)

    # 输入新的密码
    def xmm(self, keyword):
        self.find_ele(*self.P2P_xmm).send_keys(keyword)
    # 输入确认的密码
    def qrxmm(self,keyword):
        self.find_ele(*self.P2P_qrxmm).send_keys(keyword)
    # 点击提交
    def submit(self):
        self.find_ele(*self.P2Paqzx_submit_loc).click()
    # 点击修改交易密码
    def xgjymm(self):
        self.find_ele(*self.P2P_xgjymm).click()
    # --------------------------------------------------------------------
    # 我要投资
    def wytz(self):
        self.find_ele(*self.P2P_wytz).click()
    # 我要融资
    def wyrz(self):
        self.find_ele(*self.P2P_wyrz).click()
    # 点击抵押标查看详情
    def dybckxq(self):
        self.find_ele(*self.P2P_wyrz_dybckxq).click()

    # 点击质押标查看详情
    def zybckxq(self):
        self.find_ele(*self.P2P_wyrz_zybckxq).click()

    # 点击发布

    def fb1(self):
        self.find_ele(*self.P2P_wyrz_fb1).click()

    def fb2(self):
        self.find_ele(*self.P2P_wyrz_fb2).click()
    # 关于我们
    def gywm(self):
        self.find_ele(*self.P2P_wyrz_gywm).click()

    # 新闻中心
    def xwzx(self):
        self.find_ele(*self.P2P_wyrz_xwzx).click()
    # 联系我们
    def lxwm(self):
        self.find_ele(*self.P2P_wyrz_lxwm).click()
    # 名词解释
    def mcjs(self):
        self.find_ele(*self.P2P_wyrz_mcjs).click()
    # 收费规则
    def sfgz(self):
        self.find_ele(*self.P2P_wyrz_sfgz).click()
    # 帮助中心
    def bzzx(self):
        self.find_ele(*self.P2P_wyrz_bzzx).click()
    # 平台公告
    def ptgg(self):
        self.find_ele(*self.P2P_wyrz_ptgg).click()

    # 安全保障
    def aqbz(self,):
        self.find_ele(*self.P2P_wyrz_aqbz).click()

# 我要融资发布内容
#     *标题
    def wyrz_bt(self,keyword):
        self.find_ele(*self.P2P_wyrz_bt).send_keys(keyword)

    # *年利率:
    def wyrz_nll(self,keyword):
        self.find_ele(*self.P2P_wyrz_nll).send_keys(keyword)

    # 借款用途
    def wyrz_jkyt(self,keyword):
        # self.Select(*self.P2P_wyrz_jkyt).select_by_visible_text(keyword)
        self.Select(*self.P2P_wyrz_jkyt).select_by_value(keyword)
        # a.Select_by_visible_text(keyword)
        # return a

    # 统计单位:月
    def wyrz_tjdwy(self):
        self.find_ele(*self.P2P_wyrz_tjdwy).click()

    # 统计单位: 天
    def wyrz_tjdwt(self):
        self.find_ele(*self.P2P_wyrz_tjdwt).click()

    # 借款期限
    def wyrz_jkqs(self,keyword):
        self.Select(*self.P2P_wyrz_jkqx).select_by_value(keyword)

    # 还款方式
    def wyrz_hkfs(self,keyword):
        self.Select(*self.P2P_wyrz_hkfx).select_by_value(keyword)

    # 有效时间
    def wyrz_yssj(self,keyword):
        self.Select(*self.P2P_wyrz_yssj).select_by_value(keyword)

    # 密码标状态:
    def wyrz_kmm(self):
        self.find_ele(*self.P2P_wyrz_kmm).click()

    # 输入密码:
    def wyrz_srmm(self,keyword):
        self.find_ele(*self.P2P_wyrz_srmm).send_keys(keyword)

    # 最低投标金额:
    def wyrz_zdtbje(self,keyword):
        self.Select(*self.P2P_wyrz_zdtbje).select_by_value(keyword)

    # 最高投标金额:
    def wyrz_zgtbje(self,keyword):
        self.Select(*self.P2P_wyrz_zgtbje).select_by_value(keyword)

    # *借款金额:
    def wyrz_jkje(self,keyword):
        self.find_ele(*self.P2P_wyrz_jkje).send_keys(keyword)

    # 投标奖励:
    def wyrz_tbjl1(self):
        self.find_ele(*self.P2P_wyrz_tbjl1).click()

    def wyrz_tbjl1input(self,keyword):
        self.find_ele(*self.P2P_wyrz_tbjl1input).send_keys(keyword)


    def wyrz_tbjl2(self):
        self.find_ele(*self.P2P_wyrz_tbjl2).click()

    def wyrz_tbjl2input(self,keyword):
        self.find_ele(*self.P2P_wyrz_tbjl2input).send_keys(keyword)

    # 详细说明
    def wyrz_xssm(self,keyword):
        self.find_ele(*self.P2P_wyrz_xssm).send_keys(keyword)
    # 验证码
    def wyrz_yzm(self,keyword):
        self.find_ele(*self.P2P_wyrz_yzm).send_keys(keyword)
# 点击确认提交
    def wyrz_qrtj(self):
        self.find_ele(*self.P2P_wyrz_qrtj).click()

    # 我要投资
    def wytz_tz(self):
        self.find_ele(*self.P2P_wytz_tz).click()
    def wytz_ljtz(self):
        self.find_ele(*self.P2P_wytz_ljtz).click()
    def wytz_tbje(self,keyword):
        self.find_ele(*self.P2P_wytz_tbje).clear()
        self.find_ele(*self.P2P_wytz_tbje).send_keys(keyword)

    def wytz_zfmm(self,keyword):
        self.find_ele(*self.P2P_wytz_zfmm).send_keys(keyword)

    def wytz_yzm(self,keyword):
        self.find_ele(*self.P2P_wytz_yzm).send_keys(keyword)

    def wytz_qrtj(self):
        self.find_ele(*self.P2P_wytz_qrtj).click()