from __future__ import print_function

class Media(object):
	def __init__(self,cno,name,sub,note):
		self.call_no  = cno
		self.title    = name
		self.subject  = sub
		self.notes    = note
	
	def display(self):
		print("Call Number   :",self.call_no)
		print("Title         :",self.title)
		print("Subject       :",self.subject)
		print("Notes         :",self.notes)
	
	def contains_title(self,title):
	 	if self.title.__contains__(title):
			return True
		return False
	
	def contains_subject(self,subject):
	  	if self.subject.__contains__(subject):
			return True
		return False
	
	def contains_call_no(self,call_no):
	  	if self.call_no.__contains__(call_no):
			return True
		return False
