def solution(genres, plays):
	answer = []
	music = {}
	for i in range(len(genres)):
		if genres[i] in music.keys():
			music[genres[i]].append(plays[i])
		else:
			music[genres[i]] = [plays[i]]

	for key, val in music.items():
		music[key] = sorted(val, reverse=True)

	rank = sorted(music.items(), key=lambda x: sum(x[1]), reverse=True)

	for r in range(len(rank)):
		cnt = 0
		j = 0
		while cnt < 2 and len(rank[r][1]) > 0:
			if genres[j] == rank[r][0]:
				if plays[j] == rank[r][1][0]:
					answer += [j]
					rank[r][1].pop(0)
					cnt += 1
			if j == len(genres)-1:
				j = 0
			else:
				j += 1

	return answer


# print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
