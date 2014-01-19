from __future__ import print_function
import sqlite3 as lite
import sys
from Film       import Film
from Video      import Video
from Periodic   import Periodic
from Book       import Book

class PersistSQL(object):
	def __init__(self):
		self.dbName     = 'python_library'
		self.connection = None

	def execute_query(self,query):
		self.connect()
		cur   = self.connection.cursor()
		cur.execute(query)
		cur.close()

	def connect(self):
		if self.connection is not None: 
			return self.connection
		self.connection  = lite.connect(self.dbName+".db")
		cur  = self.connection.cursor()
		cur.execute('SELECT SQLITE_VERSION()')
		data = cur.fetchone()
		cur.close()
		return self.connection

	def createBook(self):
		self.connect()
		cur = self.connection.cursor()
		try:
			cur.execute("CREATE TABLE Books(CALL_NO TEXT,TITLE TEXT,SUBJECT TEXT,NOTES TEXT,AUTHOR TEXT,DESCRIPTION TEXT,PUBLISHER TEXT,CITY TEXT,SEIRES TEXT,YEAR TEXT)"+';');
		except sqlite3.IntegrityError:
			print('Table Alread Created')
		finally:
			self.connection.commit()
			cur.close()
			return True

	def createPeriodical(self):
		self.connect()
		cur = self.connection.cursor()
		try:
			cur.execute("CREATE TABLE Periodical(CALL_NO TEXT,TITLE TEXT,SUBJECT TEXT,AUTHOR TEXT,DESCRIPTION TEXT,PUBLISHER TEXT,PUBLISHER_HISTORY TEXT,SERIES TEXT,NOTES TEXT,RELATED_TITLE TEXT,OTHER_TITLES TEXT,GOV_DOC_NO TEXT)"+';');
		except sqlite3.IntegrityError:
			print('Table Alread Created')
		finally:
			self.connection.commit()
			cur.close()
			return True
	
	def createFilm(self):
		self.connect()
		cur = self.connection.cursor()
		try:
			cur.execute("CREATE TABLE Film(CALL_NO TEXT,TITLE TEXT,SUBJECT TEXT,DIRECTOR TEXT,NOTES TEXT,YEAR TEXT)"+';');
		except sqlite3.IntegrityError:
			print('Table Alread Created')
		finally:
			self.connection.commit()
			cur.close()
			return True
	
	def createVideo(self):
		self.connect()
		cur = self.connection.cursor()
		try:
			cur.execute("CREATE TABLE Videos(CALL_NO TEXT,TITLE TEXT,SUBJECT TEXT,DSCRIPTION TEXT,DISTRIBUTION TEXT,NOTES TEXT,SERIES TEXT,LABEL TEXT)"+';');
		except sqlite3.IntegrityError:
			print('Table Alread Created')
		finally:
			self.connection.commit()
			cur.close()
			return True
		
	def insertBook(self,book):
		query = """insert into Books values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"""%(book.call_no,book.title,book.subject,book.notes,book.author,book.description,book.publisher,book.city,book.series,book.year)
		self.execute_query(query)
	
	def insertFilm(self,book):
		query = """insert into Film values('%s','%s','%s','%s','%s','%s')"""%(book.call_no,book.title,book.subject,book.notes,book.director,book.year)
		self.execute_query(query)
	
	def insertVideo(self,book):
		query = """insert into Videos values('%s','%s','%s','%s','%s','%s','%s','%s')"""%(book.call_no,book.title,book.subject,book.description,book.distribution,book.notes,book.series,book.label)
		self.execute_query(query)

	def insertPeriodical(self,book):
		query = """insert into Periodical values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"""%(book.call_no,book.title,book.subject,book.author,book.description,book.publisher,book.publisher_history,book.series,book.notes,book.related_titles,book.other_titles,book.gov_doc_no)
		self.execute_query(query)

	def dropRecord(self,item):
		query = "Drop table "+item
		self.execute_query(query)

	def searchRecord(self,record,entity,entityName):
		self.connect()
		cur   = self.connection.cursor()
#		query = "select * from Film"
		query = "select * from "+record+" where "+entity+" like '%"+entityName+"%';" 
		cur.execute(query)
		result = cur.fetchall()
		return result
	
	def displayBook(self,results):
		for book in results:
			Book(book[0],book[1],book[2],book[3],book[4],book[5],book[6],book[7],book[8],book[9]).display()
	
	def displayFilm(self,results):
		for film in results:
			Film(film[0],film[1],film[2],film[3],film[4],film[5]).display()

	def displayPeriodical(self,results):
		for periodical in results:
			Periodic(periodical[0],periodical[1],periodical[2],periodical[3],periodical[4],periodical[5],periodical[6],periodical[7],periodical[8],periodical[9],periodical[10],periodical[11]).display()

	def displayVideo(self,results):
		for video in results:
			Video(video[0],video[1],video[2],video[3],video[4],video[5],video[6],video[7]).display()
