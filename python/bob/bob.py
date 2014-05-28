class bob(object):
	def __int__(self,quest):
		self.quest = quest
	
	if quest[:1]=='?':
		print('Sure')
	elif quest.upper():
		print('Whoa, chill out!')
	elif quest.islower():
		print('Whatever.')
