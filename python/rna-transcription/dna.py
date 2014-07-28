class dna:
		def to_rna(self,s):
			
			for i in range(0,len(s)):
				#G->c
				if i == 'G':
					i = 'C'
				#c->G
				if i == 'C':
					i = 'G'
				#T->A
				if i == 'T':
					i = 'A'
				#A->U
				if i == 'A':
					i = 'U'
				print i
			
		
		