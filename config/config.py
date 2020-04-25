import os
import logging

project_file=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
report_file=os.path.join(project_file,"report","report.html")
log_file=os.path.join(project_file,'log','log.txt')

test_path=os.path.join(project_file,"sound") #遍历sound包下面的所有单元测试用例

#日志配置文件
logging.basicConfig(level=logging.DEBUG,
                    format="[%(asctime)s %(levelname)s] %(filename)s %(levelno)d %(message)s",
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename=log_file,
                    filemode='a')
#邮箱配置
smtp_server='smtp.163.com'
sender='18986032799@163.com'
receiver='18986032799@163.com'

user=sender
password='PCOFXVQNFUFROEWZ'
port=465
subject='unittest test'