import re

# Encuentra la expresión para que se emita: 
# ['(734) 647-6333', '(734) 647-8044','(734) 763-2285', '(734) 647-3576', '(734) 763-1251', '(734) 764-9376']


texto = """Office of Research Administration: (734) 647-6333 | 4325 North Quad
Office of Budget and Financial Administration: (734) 647-8044 | 309 Maynard, Suite 205
Health Informatics Program: (734) 763-2285 | 333 Maynard, Suite 500
Office of the Dean: (734) 647-3576 | 4322 North Quad
UMSI Engagement Center: (734) 763-1251 | 777 North University
Faculty Adminstrative Support Staff: (734) 764-9376 | 4322 North Quad"""

print(re.findall(r':\D(.+)\D\|',texto))