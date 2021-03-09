# coding = "utf-8"

import json
import time
from appium import webdriver

j_data = open("F:\work\Link\common\configure.json", encoding="utf-8")
data = json.load(j_data)


class E5Z:
    def __init__(self):
        self.desired_caps = {'platformName': data['E5Z']['platformName'],
                             'platformVersion': data['E5Z']['platformVersion'],
                             'deviceName': data['E5Z']['deviceName'],
                             'appPackage': data['E5Z']['appPackage'],
                             'appActivity': data['E5Z']['appActivity']}
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_caps)

    def to_find_element(self, by, value):
        try:
            return self.driver.find_element(by, value)
        except Exception as msg:
            print("元素{}找不到:{}".format(value, msg))
            return False

    def to_find_elements(self, by, value):
        try:
            elements = self.driver.find_elements(by, value)
            if len(elements) < 1:
                return False
            return elements
        except Exception as msg:
            print("元素们{}不存在：{}".format(value, msg))
            return False


class E6Z:
    def __init__(self):
        self.desired_caps = {'platformName': data['E6Z']['platformName'],
                             'platformVersion': data['E6Z']['platformVersion'],
                             'deviceName': data['E6Z']['deviceName'],
                             'appPackage': data['E6Z']['appPackage'],
                             'appActivity': data['E6Z']['appActivity']}
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_caps)

    def to_find_element(self, by, value):
        try:
            element = self.driver.find_element(by, value)
            return element
        except Exception as msg:
            print("元素{}找不到:{}".format(value, msg))
            return False

    def to_find_elements(self, by, value):
        try:
            elements = self.driver.find_elements(by, value)
            if len(elements) < 1:
                return False
            return elements
        except Exception as msg:
            print("元素们{}不存在：{}".format(value, msg))
            return False

    def find_element_text(self, text):
        try:
            return self.driver.find_element_by_android_uiautomator('new UiSelector().text("{}")'.format(text))
        except:
            return False

    def is_element_exist_by(self, by, value, times=1):
        for i in range(times):
            time.sleep(2)
            if self.to_find_element(by, value):
                return True
        return False

    def is_element_exist_text(self, value, times=1):
        for i in range(times):
            time.sleep(2)
            if self.find_element_text(value):
                return True
        return False

    def aa(self):
        pass

    def quit(self):
        self.driver.quit()


if __name__ == "__main__":
    a = E6Z()
    if a.to_find_element("name", "device_card_name_火星人集成灶"):
        print("11111")
    time.sleep(5)
    a.quit()
