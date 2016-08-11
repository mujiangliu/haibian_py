# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
from Tkinter import Button
from time import sleep
import new
from selenium.webdriver import chrome

courseId = "2515"
mainTeacher = u"李阳"

#打开浏览器
driver = webdriver.Chrome()

#登录后台模块
driver.get("http://test2.admin.haibian.com")
driver.find_element_by_id("uname").clear()
driver.find_element_by_id("uname").send_keys("mujiangliu@163.com")
driver.find_element_by_id("pwd").clear()
driver.find_element_by_id("pwd").send_keys("111111")
driver.find_element_by_name("login_sub").click()
time.sleep(2)

#打开创建直播讲页
driver.get("http://test2.admin.haibian.com/chapter/add_live")

#计算当前日期
n = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
num = 20
nameNew = n[0:num]

#输入直播名称
driver.find_element_by_id("liveVideoName").send_keys(u"李阳测试"+nameNew)

#选择年级
selectGrade = Select(driver.find_element_by_id("gradeId"))
selectGrade.select_by_visible_text("初一")

#选择学科
selectSubject = Select(driver.find_element_by_id("subjectId"))
selectSubject.select_by_value("2")

#输入主讲老师
driver.find_element_by_id("publicTeacherId_sele").send_keys(mainTeacher)
time.sleep(1)

#选择直播类型：选修课-阶梯教室
driver.find_element_by_css_selector("html.no-js body.page-header-fixed div#publicTeacherId_editable-select-options.editable-select-options ul li.selected").click()
driver.find_element_by_css_selector("label.checkbox-inline.n1").click()
time.sleep(1)

#选择试卷:ytxu随堂作业组卷
driver.find_element_by_css_selector("button.btn.btn_getExam").click()
time.sleep(1)
driver.find_element_by_id("paper_key").send_keys(u"ytxu随堂作业组卷")
time.sleep(1)
driver.find_element_by_name('getPaperList').click()
time.sleep(1)
driver.find_element_by_xpath("//div[@id='dialog_paper_list']/label[1]").click()
driver.find_element_by_link_text(u"确定").click()

#去掉首页推荐的勾选
driver.find_element_by_id("show_index").click()

#单击保存
driver.find_element_by_name("saveLive").click()

#确认弹框提示1
a = driver.switch_to_alert()
print a.text
a.accept()
time.sleep(1)

#确认弹框提示2
b = driver.switch_to_alert()
print b.text
assert u"保存成功" in b.text
b.accept()
time.sleep(2)

#关联课程

driver.get("http://test2.admin.haibian.com/course/coursedate?course_id=%s"%courseId)
time.sleep(2)
driver.find_element_by_css_selector("#quanbu").click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="addchapters"]').click()
time.sleep(1)

n = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
num = 10
nameNew = n[5:num]
print nameNew
startTime= n[11:13]

selectGrade = Select(driver.find_element_by_name("grades"))
selectGrade.select_by_visible_text(u"初一")

selectSubject = Select(driver.find_element_by_name("subjects"))
selectSubject.select_by_visible_text(u"数学")

driver.find_element_by_id("wk").send_keys(nameNew)
driver.find_element_by_css_selector("form div button").click()
time.sleep(1)

driver.find_element_by_css_selector("#uniform-pid span").click()
time.sleep(1)

driver.find_element_by_id("baocun").click()

a = driver.switch_to_alert()
print a.text
a.accept()
time.sleep(1)
 
b = driver.switch_to_alert()
print b.text
b.accept()
time.sleep(1)
print "直播讲关联成功"

#关闭浏览器
driver.close()