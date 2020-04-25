import unittest
from lib import HTMLTestRunner
from config.config import *
from lib.send_email import send_email
logging.info("------teststart--------------")
suitecase=unittest.defaultTestLoader.discover(test_path)

with open(report_file,"wb") as file1:
    runner=HTMLTestRunner.HTMLTestRunner(stream=file1,title='unittest',description='test')
    runner.run(suitecase)


send_email(report_file)
logging.info("--------------testend------------")