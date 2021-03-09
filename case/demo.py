# coding = utf-8

import time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

desired_caps = {
    'platformName': 'Android',
    'platformVersion': '8.1.0',
    'deviceName': 'e80c140b',
    'appPackage': 'com.jd.smart',
    'appActivity': 'com.jd.smart.activity.LoadingActivity'
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
action = TouchAction(driver)


def get_size():

    # 获取窗口尺寸
    size = driver.get_window_size()
    x = size['width']
    y = size['height']
    return x, y


def swipe_up():
    # 向上滑动
    size = get_size()
    x1 = int(size[0] * 0.5)
    y1 = int(size[1] * 0.9)
    y2 = int(size[1] * 0.1)
    driver.swipe(x1, y1, x1, y2, 500)


def swipe_down():
    # 向下滑动
    size = get_size()
    x1 = int(size[0] * 0.5)
    y1 = int(size[1] * 0.1)
    y2 = int(size[1] * 0.9)
    driver.swipe(x1, y1, x1, y2, 500)


def swipe_left():
    # 向左滑动
    size = get_size()
    x1 = int(size[0] * 0.9)
    x2 = int(size[0] * 0.1)
    y1 = int(size[1] * 0.5)
    driver.swipe(x1, y1, x2, y1, 500)


def swipe_right():
    # 向右滑动
    size = get_size()
    x1 = int(size[0] * 0.1)
    x2 = int(size[0] * 0.9)
    y1 = int(size[1] * 0.5)
    driver.swipe(x1, y1, x2, y1, 500)


time.sleep(5)


def is_elment_exist(element):
    source = driver.page_source
    print(source)
    if element in source:
        return True
    else:
        return False


if is_elment_exist("登陆"):
    a = driver.find_element_by_xpath(
        "//*[@resource-id='com.aliyun.iot.ilop.demo:id/login_id']/android.widget.LinearLayout/android.widget.EditText")
    a.clear()
    a.send_keys("15397010160")
    time.sleep(2)
    driver.find_element_by_xpath(
        "//*[@resource-id='com.aliyun.iot.ilop.demo:id/password']/android.widget.LinearLayout/android.widget.EditText").send_keys(
        "Hxraxw#1234")
    time.sleep(2)
    # driver.find_element_by_name("登录").click()
    # driver.find_element_by_android_uiautomator('text("登录")').click()
    driver.find_element_by_id("com.aliyun.iot.ilop.demo:id/next").click()
    time.sleep(3)
driver.find_element_by_id("com.aliyun.iot.ilop.demo:id/device_panel_name").click()
time.sleep(2)
light = driver.find_element_by_id("com.aliyun.iot.ilop.demo:id/e5z_light_tv")
light.click()
print(light.get_attribute("text"))
# print(light.get_attribute("drawableTop"))
swipe_down()
time.sleep(2)
driver.find_element_by_android_uiautomator('.text("蒸箱功能")').click()
time.sleep(2)
driver.find_element_by_id("com.aliyun.iot.ilop.demo:id/steam_book_func_ll").click()
time.sleep(2)
c = driver.find_element_by_id("com.aliyun.iot.ilop.demo:id/hour24")


time.sleep(5)
driver.quit()
