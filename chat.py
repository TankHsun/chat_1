import os  #operating system

#讀取檔案
def read_file(filename):
	lines = []
	if os.path.isfile(filename):#尋找當下路徑是否有這個檔案，若為其他路徑則須提供完整路徑
		with open(filename, 'r',encoding='utf-8-sig') as f:
			for line in f:
				lines.append(line.strip())
	return lines
#對話分類
def convert(lines):
	new = []
	person = None
	for line in lines:
		if line == 'Allen':
			person = 'Allen'
			continue
		elif line == 'Tom':
			person = 'Tom'
			continue
		if person:	
			new.append(person + ':' + line)
	return new

#寫入檔案
def write_file(filename, new):

	with open(filename, 'w') as f:
	#encoding='utf-8'，為了修正亂碼問題，用utf-8通用的編碼
	#with open(filename, 'w', encoding='utf-8') as f:
		for p in new:
			f.write(p + '\n')
	
def main():
	lines = read_file('input.txt')
	new = convert(lines)
	write_file('output.txt', new)

main()