class DNA:
		def __init__(self, s):
			self.s = s
			print s
		def to_rna(s):

			if s == 'G':
				s = 'C'
					#c->G
			if s == 'C':
				 return'G'
					#T->A
			if s== 'T':
				s = 'A'
					#A->U
			if s == 'A':
				s = 'U'
				
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
			
				return s
			
		
		