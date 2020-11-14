def solution(files):
	files_dict = {}

	for file in files:
		head, number, tail = '', '', ''

		for f in range(len(file)):
			if len(head) > 0 and len(tail) > 0:
				try:
					tail += str(int(file[f]))
				except:
					tail += file[f]
			else:
				try:
					number += str(int(file[f]))
				except:
					if len(number) > 0:
						tail += file[f]
					else:
						head += file[f]

		files_dict[file] = head.lower(), int(number)

	answer = sorted(files_dict.items(), key=lambda x: (x[1][0], x[1][1]))
	return list(y[0] for y in answer)


print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))
