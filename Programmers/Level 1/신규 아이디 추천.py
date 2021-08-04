def solution(new_id):
	new_id = new_id.lower()
	char = ['-', '_', '.'] + [chr(i) for i in range(ord('a'), ord('z')+1)] + [str(i) for i in range(10)]
	new_id = list(filter(lambda x: x in char, new_id))
	for i in range(len(new_id)):
		if new_id[i] == '.':
			j = i + 1
			while j < len(new_id):
				if new_id[j] == '.':
					new_id[j] = ''
					j += 1
				else:
					break
	new_id = ''.join(new_id).strip('.')
	if not new_id:
		new_id = 'a'
	if len(new_id) > 15:
		return new_id[:15].strip('.')
	while len(new_id) < 3:
		new_id += new_id[-1]
	return new_id


# print(solution("...!@BaT#*..y.abcdefghijklm"))  # "bat.y.abcdefghi"
# print(solution("z-+.^."	))  # "z--"
# print(solution("=.="))  # "aaa"
# print(solution("123_.def"))  # "123_.def"
# print(solution("abcdefghijklmn.p"))  # "abcdefghijklmn"
# print(solution("................b"))  # "bbb"
# print(solution("~!@#$%&*()=+[{]}:?,<>/"))  # aaa
# print(solution(".1."))  # 111
