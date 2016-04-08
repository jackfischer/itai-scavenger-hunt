import sqlite3

class Crud():
	def __init__(self):
			self.filepath = "schema.db"
			self.conn = sqlite3.connect(self.filepath)
			self.conn.text_factory = str
			self.c = self.conn.cursor()

	def execute(command):
		print "im in execute"
		try:
			self.c.execute(execute)
		except:
			print "i failed"
