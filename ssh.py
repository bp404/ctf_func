#!/usr/bin/python
# -*- coding: utf-8 -*-

#ssh 连接
#author: bp404

import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("218.7.221.122",22,"root", "hrbnu88060100()100")
stdin, stdout, stderr = ssh.exec_command("top")
rtn = stdout.readlines()
print rtn
ssh.close()