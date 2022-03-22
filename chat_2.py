import os  #operating system

#讀取檔案
def read_file(filename):
	lines = []
	if os.path.isfile(filename):#尋找當下路徑是否有這個檔案，若為其他路徑則須提供完整路徑
		with open(filename, 'r',encoding='utf-8-sig') as f:
			for line in f:
				lines.append(line.split())
	print(lines)
	return lines
#統計
def stats(lines):
	A_w, A_t, A_p, V_w, V_t, V_p=0, 0, 0, 0, 0, 0
	for a in range(len(lines)):
		if lines[a][1] == 'Allen':
			if lines[a][2] == '貼圖':
				A_t += 1
			if lines[a][2] == '圖片':
				A_p += 1
			else:
				for sum_ in lines[a][2:]:
					A_w += len(sum_)
	
		elif lines[a][1] == 'Viki':
			if lines[a][2] == '貼圖':
				V_t += 1
			if lines[a][2] == '圖片':
				V_p += 1
			else:
				for sum_ in lines[a][2:]:
					V_w += len(sum_)	
		else:
			continue	
	print('Allen說了',A_w,'個字，傳了',A_t,'個貼圖，傳了',A_p,'張圖片')
	print('Viki說了',V_w,'個字，傳了',V_t,'個貼圖，傳了',V_p,'張圖片')	
	
def main():
	lines = read_file('LINE-Viki.txt')
	stats(lines)

main()