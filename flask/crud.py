import sqlite3

class Crud():
	def __init__(self):
			self.filepath = "schema.db"
			self.conn = sqlite3.connect(self.filepath)
			#self.conn.text_factory = str
			self.c = self.conn.cursor()
			print "init"

	def execute(self, command):
		print "im in execute"
		print command
		try:
			#self.c.execute(command)
			self.c.execute("SELECT * FROM passes;")
		except:
			print "i failed"
			print e
			return ""
		try:
			fetch = self.c.fetchall()
			return fetch
		except:
			print "failed here"
			return ""
