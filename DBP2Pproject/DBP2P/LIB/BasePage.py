from selenium.webdriver.support.ui import Select
class BasePage:
    # 构造方法
    def __init__(self,driver):
        # 打开浏览器
        self.driver = driver  # Alt+Enter
        # 加载百度首页
        # self.driver.get('http://www.baidu.com')

    # 封装定位元素
    def find_ele(self, *args):
        ele = self.driver.find_element(*args)
        return ele
    def switch_to(self, *args):
        ele = self.driver.switch_to.window(*args)
        return ele
    def current_window_handle(self, *args):
        ele = self.driver.current_window_handle(*args)
        return ele
    def window(self, *args):
        ele = self.driver.window(*args)
        return ele
    def Select(self, *args):
        ele = Select(self.driver.find_element(*args))
        # ele.select_by_visible_text(keyword)
        return ele
    def Select_by_visible_text(self, *args):
        ele = self.driver.select_by_visible_text(*args)
        return ele

