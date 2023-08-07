class removeDupes:
	def __init__(self):
		self.filename = input('File Name:  ')
		mm = self.filelines(self.filename)
		self.writes(self.ReadFile())
		print('Lines Removed: '+str(mm-self.filelines(self.filename)))

	def filelines(self, file):
		with open(file, 'rb') as f:
			for i, null in enumerate(f):
				pass
		return i
	def ReadFile(self):
		with open(self.filename, 'rb') as f:
			return f.read().decode('ISO-8859-1').replace("\r", '').split('\n')
	def writes(self, data):
		data = set(data)
		with open(self.filename, 'wb') as f:
			for x in data:
				if x == '' or x == b'':
					continue
				f.write(x.encode() + b'\n')
removeDupes()