import re

texto = """b7 (ab) b52s [^ab] (x b2s (pe bas? (( xxx"""

print(re.findall(r'\([^ab)]',texto)) # Toma (x, pero toma otros?
print(re.findall(r'b[3-72]s',texto)) # Toma b2s?
print(re.findall(r'(([^a][^b])*)+',texto))
print(re.findall(r'b[^0-59]s\?',texto)) # Toma bas?