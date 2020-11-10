def replace_melody(string):
	return string.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#','g').replace('A#', 'a')

def solution(m, musicinfos):
	answer = (0, 0)
	m = replace_melody(m)
	musics = {}

	for musicinfo in musicinfos:
		musicinfo = musicinfo.split(',')

		time = 0
		t1, t2 = musicinfo[0], musicinfo[1]
		time += (int(t2[:2]) - int(t1[:2])) * 60
		time += int(t2[3:]) - int(t1[3:])

		akbo = replace_melody(musicinfo[3])
		n_akbo = akbo
		while len(n_akbo) < time:
			n_akbo += akbo
		n_akbo = n_akbo[:time]

		musics[musicinfo[2]] = n_akbo

	for key, val in musics.items():
		j = 0
		while j < len(val):
			if m[0] == val[j]:
				for k in range(len(m)):
					if j + k < len(val):
						if m[k] != val[j+k]:
							break
					else:
						break
				else:
					if len(val) > answer[1]:
						answer = (key, len(val))
			j += 1

	return answer[0] if answer[0] else '(None)'

print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print(solution('CDEFGAC', ['12:00,12:06,HELLO,CDEFGA'])) # none
print(solution("ABC", ["00:00,00:05,HI,ABC#ABC"]))  # none
print(solution("ABC", ["00:00,00:06,HI,ABC#ABC"]))  # hi

# 참고 list in list 체크하는 방법
# all(item in List1 for item in List2)
# 없는지 체크는
# any(~~)
