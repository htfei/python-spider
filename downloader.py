#-*- coding: UTF-8 -*-
import requests  
from contextlib import closing

if __name__ == '__main__':
	#url = 'http://www.demongan.com/source/game/二十四点.zip'
	print('*' * 100) 											# 字符串乘法
	url  = input('请输入需要下载的文件链接:\n')					  # 输入字符串
	filename = url.split('/')[-1]   							# 字符串分割
	with closing(requests.get(url, stream=True)) as response:	# contextlib.closing()函数是实现在一个block之后自动关闭			
		if response.status_code == 200:
			content_size = int(response.headers['content-length'])	# content-length 为数据内容总长度
			with open(filename, "wb") as file:  
				down_data = 0
				for data in response.iter_content(1024):  	# response.iter_content()函数 流下载时的推荐方法
					file.write(data)
					down_data += len(data)
					str = "[%s下载进度] 正在下载 %.2f%% "  % (filename, down_data/content_size * 100 ) # %%表示打印符号‘%’
					print(str,end='\r')
		else:
			print('链接异常')