# coding: utf-8

# use pandas taframe to store weather_info.txt as csv format

from datetime import *
import time
import pandas as pd

weather_df = pd.read_csv('weather_info.txt',header=None)
weather_df.columns = ['City','Weather']

''' 
 除了直接操作Pandas，自己尝试三种方法转成 Dict
 change pandas dataframe to dict 
 Method 1: Pandas to_dict, BE CAREFUL cannot have duplicated index
weather_dict = weather_df.set_index('city')['weather'].to_dict()

 Method 2:Pandas zip, BE CAREFUL cannot have duplicated index
weather_dict = dict(zip(weather_df.city, weather_df.weather))

 Standard method:  can have duplicate value
 weather_dict = {}
 for i in range(len(weather_df)):
	currentcity = weather_df.iloc[i,0]
	currentweather = weather_df.iloc[i,1]
	weather_dict.setdefault(currentcity,[])
	weather_dict[currentcity].append(currentweather) 
'''


# start receiving user input
history = []
usr_input=''

while usr_input != 'quit':
	usr_input = input('请输入指令或您要查询的城市名：')

	# accumulate user input into history list
	history.append([datetime.now().strftime('%c'),usr_input])

	if usr_input == 'help':
		print('输入城市名，查询该城市的天气；')
		print('输入 help，获取帮助文档；')
		print('输入 history, 获取查询历史；')
		print('输入 quit，退出天气查询系统。')

	elif usr_input == 'history':
		for i in range(len(history)):
			print(history[i])

	elif usr_input == 'quit':
		break
	
	else :
		# search the dataframe
		result_df = weather_df[weather_df.City==usr_input]
		if len(result_df) == 0 :
			print('您输入的指令不正确，或者没有您输入的城市的天气信息')
			print('您可以输入 help 获取帮助。')
		else :
		# 只取出搜索到的第一条信息，万一文件里有重复
			print(usr_input,' 的天气是',result_df.iat[0,1])



	
