#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#crc32加密
#author: bp404

import binascii

def crc32(v):  
    """ 
    Generates the crc32 hash of the v. 
    @return: str, the str value for the crc32 of the v 
    """  
    return '0x%x' % (binascii.crc32(v) & 0xffffffff)  #取crc32的八位数据 %x返回16进制

if __name__ == '__main__':
	for i in range(1900,2100):
		for j in range(01,12):
			for k in range(1,30):
				year = str(i)
				month = str(j)
				day = str(k)
				if j < 10:
					month = "0" + month
				if k < 10:
					day = "0" + day

				str_date = year + month + day

				str1 = crc32(str_date)
				#0x4d1fae0b
				if str1 == "0x4d1fae0b":
					print "Key =>" + str_date
					break


