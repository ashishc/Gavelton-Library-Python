#!/usr/bin/python
from Book       import Book
from Media      import Media
from Film       import Film
from Video      import Video
from Periodic   import Periodic
from PersistSQL import PersistSQL

class SearchEngine(object):
	def __init__(self):
		self.results = []
		self.db = PersistSQL()
		cart_catalog = []
			
	def contains_call_no(self,searchItem):
		books = self.db.searchRecord('Books','CALL_NO',searchItem)
		self.db.displayBook(books)
		films = self.db.searchRecord('Film','CALL_NO',searchItem)	
		self.db.displayFilm(films)
		periodics = self.db.searchRecord('Periodical','CALL_NO',searchItem) 
		self.db.displayPeriodical(periodics)
		videos = self.db.searchRecord('Videos','CALL_NO',searchItem)
		self.db.displayVideo(videos)

	def contains_other(self,other_item):
		for item in self.cart_catalog:
			if item.contains_other(other_item):
				self.results.append(item)
	
	def contains_subject(self,subject):
	   	for item in self.cart_catalog:
			if item.contains_subject(subject):
				self.results.append(item)
	
	def contains_title(self,title):
		for item in self.cart_catalog:
			if item.contains_title(title):
				self.results.append(item)
	
	def display_results(self):
	   	for item in self.results:
			item.display()
	
	def empty_results(self):
		del self.results[:]
	
	def result_found(self):
		if not self.results:
			return False
		return True

	def parse_video(self):
		self.db.createVideo()
		fvideo = open("video.txt")
		item_list = []
		for line in fvideo:
			line = line.strip()
			item_list = line.split("|")
			vi = Video(item_list[0],item_list[1],item_list[2],item_list[3],item_list[4],item_list[5],item_list[6],item_list[7])
			self.db.insertVideo(vi)
		fvideo.close()

	def parse_film(self):
#		self.db.dropRecord("Films")
		self.db.createFilm()
		ffilm = open("film.txt")
		item_list = []
		for line in ffilm:
			line = line.strip()
			item_list = line.split("|")
			fl = Film(item_list[0],item_list[1],item_list[2],item_list[3],item_list[4],item_list[5])
			self.db.insertFilm(fl)
		ffilm.close()

	def parse_periodic(self):
#		self.db.dropRecord("Periodics")
		self.db.createPeriodical()
		fperiodic = open("periodic.txt")
		item_list = []
		for line in fperiodic:
			line = line.strip()
			item_list = line.split("|")
			pr=Periodic(item_list[0],item_list[1],item_list[2],item_list[3],item_list[4],item_list[5],item_list[6],item_list[7],item_list[8],item_list[9],item_list[10],item_list[11])
			self.db.insertPeriodical(pr)
		fperiodic.close()

	def parse_book(self):
		self.db.dropRecord("Books")
		self.db.createBook()
		fbook = open("book.txt")
		item_list = []
		for line in fbook:
			line = line.strip()
			item_list = line.split("|")
			bk = Book(item_list[0],item_list[1],item_list[2],item_list[3],item_list[4],item_list[5],item_list[6],item_list[7],item_list[8],item_list[9])	
			self.db.insertBook(bk)
		fbook.close()

