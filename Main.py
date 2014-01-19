#!/usr/bin/python

from __future__ import print_function
from SearchEngine import SearchEngine
import sys
choice = 0
se = SearchEngine()

if len(sys.argv) is not None:
	argument = str(sys.argv)
	if "book" in argument:
		se.parse_book()			
	if "film" in argument:
		se.parse_film()
	if "period" in argument:
		se.parse_periodic()
	if "video" in argument:
		se.parse_video()


while choice!= 5:
	print("__________________Welcome_________________")
	print("1.Search by Call Number")
	print("2.Search by Title")
	print("3.Search by Subject")
	print("4.Search by Others")
	print("5.Exit")
	print("__________________________________________")
	choice = input("Please enter your choice:")

	if choice == 1:
		search = raw_input("Enter string to search:")
		se.contains_call_no(search)
		if se.result_found():
			se.display_results()
		else:
			print("No match Found")

	elif choice == 2:
		search = raw_input("Enter string to search:")
		se.contains_title(search)

		if se.result_found():
			se.display_results()
		else:
			print("No match Found")
		
	elif choice == 3: 
		search = raw_input("Enter string to search:")
		se.contains_subject(search)
		if se.result_found():
			se.display_results()
		else:
			print("No match found")

	elif choice == 4:
		search = raw_input("Enter string to search:")
		se.contains_other(search)
		if se.result_found():
			se.display_results()
		else:
			print("No match found")

	elif choice == 5:
		exit()

	se.empty_results();
