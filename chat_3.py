import os  #operating system

#讀取檔案
def read_file(filename):
	lines = []
	if os.path.isfile(filename):#尋找當下路徑是否有這個檔案，若為其他路徑則須提供完整路徑
		with open(filename, 'r',encoding='utf-8-sig') as f:
			for line in f:
				lines.append(line.strip())
	return lines

def cut(lines):
	for line in lines:
		s=line.split()
		name = s[0][5:]
		print(name)


def main():
	lines = read_file('3.txt')
	cut(lines)

main()