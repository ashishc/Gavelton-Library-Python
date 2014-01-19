from __future__ import print_function
from Media import Media

class Video(Media):
	def __init__(self,call_no,title,subjects,description,distribution,notes,series,label):
		super(Video,self).__init__(call_no,title,subjects,notes)
		self.description  = description
		self.distribution = distribution
		self.label        = label
		self.series       = series
	
	def display(self):
		print("_____________________________Video_____________________________")
		super(Video,self).display()
		print('Description    		  :',self.description)
		print('Distribution    		  :',self.distribution)
		print('Label          	 	  :',self.label)
		print('Series         		  :',self.series)
		print("_______________________________________________________________")
	
	def contains_other(self,item):
	 	if self.description.__contains__(item) or self.notes.__contains__(item) or self.distribution.__contains__(item):
			return True
		return False
