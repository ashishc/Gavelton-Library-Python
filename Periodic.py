from __future__ import print_function
from Media import Media

class Periodic(Media):
	def __init__(self,call_no,title,subjects,author,description,publisher,pub_history,series,notes,related_title,other_titles,gov_doc_no):
		super(Periodic,self).__init__(call_no,title,subjects,notes)
		self.author         	   = author
		self.title		   = title
		self.description 	   = description
		self.publisher   	   = publisher
		self.publisher_history     = pub_history
		self.related_titles        = related_title
		self.other_titles	   = other_titles
		self.series 	 	   = series
		self.gov_doc_no        	   = gov_doc_no
	def display(self):
		print("__________________________Periodic_____________________________")
		super(Periodic,self).display()
		print('Author        		:',self.author)
		print('Title			:',self.title)
		print('Description   		:',self.description)
		print('Publisher     		:',self.publisher)
		print('Publisher History        :',self.publisher_history)
		print('Related Titles        	:',self.related_titles)
		print('Other Titles         	:',self.other_titles)
		print('Series         		:',self.series)
		print('Government Doc No        :',self.gov_doc_no)
		print("_______________________________________________________________")
	def contains_other(self,item):
	 	if self.description.__contains__(item) or self.notes.__contains__(item) or self.series.__contains__(item):
			return True
		return False
