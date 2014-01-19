from __future__ import print_function
from Media import Media

class Book(Media):
	def __init__(self,call_no,title,subjects,author,description,publisher,city,year,series,notes):
		super(Book,self).__init__(call_no,title,subjects,notes)
		self.author      = author
		self.description = description
		self.publisher   = publisher
		self.city        = city
		self.series 	 = series
		self.year        = year
	def display(self):
		print("______________________________BOOK_____________________________")
		super(Book,self).display()
		print('Author        :',self.author)
		print('Description   :',self.description)
		print('Publisher     :',self.publisher)
		print('City          :',self.city)
		print('Series        :',self.series)
		print('Years         :',self.year)
		print("_______________________________________________________________")
	def contains_other(self,item):
	 	if self.description.__contains__(item) or self.notes.__contains__(item) or self.year.__contains__(item):
			return True
		return False
