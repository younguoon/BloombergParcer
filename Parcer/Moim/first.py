# -*- coding: utf-8 -*-
from selenium import selenium
import unittest, time, re

class first(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*chrome", "http://www.moim.me/")
        self.selenium.start()
    
    def test_qeqeqeqeqqe(self):
        sel = self.selenium
        sel.open("/fnara_admin_new/default.asp")
        sel.select_frame("mainFrame")
        sel.click(u"link=스토어 등록관리")
        sel.click(u"link=스토어 등록관리")
        sel.wait_for_page_to_load("30000")
        sel.click("css=td.list_teb_on")
        sel.click("css=td.list_teb_on")
        sel.wait_for_page_to_load("30000")
        sel.click(u"link=스토어등록")
        sel.click("id=str")
        sel.click("id=str")
        sel.select_frame("relative=up")
        sel.select_frame("mainFrame")
        sel.click_at("id=str", "74,13")
        sel.type("id=str", u"약국")
        sel.send_keys("id=str", "${KEY_ENTER}")
        sel.select_frame("relative=up")
        sel.select_frame("mainFrame")
        sel.click_at("css=a > p", "68,19")
        sel.click(u"link=선택")
    
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
