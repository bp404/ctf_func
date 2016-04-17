#!/usr/Bin/env python
# -*- coding: utf-8 -*-

#smtp邮件发送
#author: bp404

import smtplib
from email.message import Message
def email_bp404():
	m = Message
	m = Message()
	m['Subject'] = '陈炫慧'
	m['From'] = 'honkerxin@163.com'
	m['To'] = '1223522476@qq.com'
	m.set_payload('臭傻逼')
	m = m.as_string()
	smtp = 'smtp.163.com'
	sm = smtplib.SMTP_SSL(smtp,port=465,timeout=20)
	sm.login('honkerxin@163.com','1314bpbp')
	sm.sendmail('honkerxin@163.com','1223522476@qq.com',m)

n = 100
while n > 0:
	email_bp404()
	n = n - 1