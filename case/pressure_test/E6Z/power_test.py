# coding = "utf-8"

import time
import pytest
from common.common import E6Z
from selenium.webdriver.common.by import By


class Test_one(E6Z):

    def power_test(self):
        if self.is_element_exist_text("点击下载", 3):
            self.find_element_text("取消").click()
            time.sleep(2)

        if self.is_element_exist_by(By.ID, "com.jd.smart:id/tv_device_name", 3):
            self.to_find_element(By.ID, "com.jd.smart:id/tv_device_name").click()
            time.sleep(5)
            c = self.driver.contexts
            print(self.driver.context)
            print(c)
            # self.driver.switch_to.context(c[1])
            print(self.driver.context)
            power_on = self.is_element_exist_by(By.XPATH, '//*[text="照明"]', 3)
            print("111")
            if power_on:
                print("haha")
                for i in range(5):
                    time.sleep(3)
                    if self.is_element_exist_text("集成灶(已开启)", 3):
                        print("关机")
                        self.to_find_element(By.XPATH,
                                             '//*[@text="集成灶(已开启)"]/following-sibling::android.view.View').click()
                        if self.is_element_exist_text("确认要关闭集成灶吗？", 3):
                            self.find_element_text("确定").click()
                    else:
                        print("开机")
                        self.to_find_element(By.XPATH,
                                             '//*[@text="集成灶(已关闭)"]/following-sibling::android.view.View').click()
        time.sleep(3)
        self.quit()


if __name__ == "__main__":
    a = Test_one()
    a.power_test()
