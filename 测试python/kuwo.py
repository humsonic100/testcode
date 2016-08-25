import urllib2
import sys
import os
import re

def get_href_music(home_page):
	home_html=urllib2.urlopen(home_page).read()
	href_music_rule='href=".*;"'
	href_music_rule_re=re.compile(href_music_rule)
	href_list=href_music_rule_re.findall(home_html)
	href_music_list=[]

	for href in href_list:
		#print href
		#continue
		#print "href start...."
		music_index=href.find("MUSIC")
		if music_index==-1:
			continue
		#	print href[music_index:]
		#continue
		#print music_index
		music_over_index=href.find("',",music_index)
		#print music_over_index
		#if music_over_index!=-1:
		#	print href[music_index:music_over_index]
		#print "href end...."
		#continue
		if not music_index:
			print "music_index not find.."
		else:
			href_music_list.append(href[music_index:music_over_index])
		#else:
		#	#print "music_index find"
		#	print href[music_index:music_over_index]
		#print href
	return href_music_list

def get_antiserver_url(href_true_list):
	for href in href_true_list:
		#href=href.replace('_','%5F')
		full_anti_url="http://antiserver.kuwo.cn/anti.s?response=url&type=convert%5Furl&rid="+href+"&format=aac%7Cmp3"
		#%sformat=aac%7Cmp3"%href
		true_file_url=urllib2.urlopen(full_anti_url).read()
		print true_file_url

def main():
	#suffix_list.append("zip")
	#suffix_list.append("exe")
	#suffix_list.append("rar")
	home_page="http://www.kuwo.cn/bang/index"
	#static_rule="/soft/"
	href_true_list=get_href_music(home_page)
	#for i in href_true_list:
	#	print i
	get_antiserver_url(href_true_list)
	#for href in href_true_list:
	#	print href
	#get_file_list(href_true_list)
if __name__ == '__main__':
  main()