class DNA:
		def __init__(self, s):
			self.s = s
			
		def to_rna(self):

			if self.s == 'G':
				self.s = 'C'
					#c->G
			if self.s == 'C':
				return'G'
					#T->A
			if self.s == 'T':
				self.s = 'A'
					#A->U
			if self.s == 'A':
				self.s = 'U'
				
			#for i in range(0,len(s)):
					#G->c
			#	if s[i] == 'G':
			#		s[i] = 'C'
					#c->G
			#	if s[i] == 'C':
			#		s[i] = 'G'
					#T->A
			#	if s[i] == 'T':
			#		s[i] = 'A'
					#A->U
			#	if s[i] == 'A':
			#		s[i] = 'U'
			
			return self.s
			
		
		