# -*- coding:utf-8  -*-
# @Time     :2018/9/16 20:20
# @Author   :Hawley
def make_pizza(size,*toppings):
	print('\n making a' + str(size) + '-inch pizza with the following toppings:')
	for topping in toppings:
		print('-' + topping)