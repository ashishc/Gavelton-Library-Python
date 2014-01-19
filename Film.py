from __future__ import print_function
from Media import Media

class Film(Media):
	def __init__(self,call_no,title,subjects,director,notes,year):
		super(Film,self).__init__(call_no,title,subjects,notes)
		self.director    = director
		self.year        = year
	
	def display(self):
		print("______________________________FILM_____________________________")
		super(Film,self).display()
		print('Director      :',self.director)
		print('Years         :',self.year)
		print("_______________________________________________________________")
	
	def contains_other(self,item):
	 	if self.director.__contains__(item) or self.notes.__contains__(item) or self.year.__contains__(item):
			return True
		return False
