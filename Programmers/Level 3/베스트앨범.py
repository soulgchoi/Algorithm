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


def solution2(genres, plays):
	answer = []
	hash_map = {}
	for i in range(len(genres)):
		if genres[i] in hash_map.keys():
			hash_map[genres[i]] += [plays[i]]
		else:
			hash_map[genres[i]] = [plays[i]]

	for key, val in hash_map.items():
		hash_map[key] = sorted(val, reverse=True)

	plays_rank = sorted(hash_map.keys(), key=lambda x: sum(hash_map[x]), reverse=True)

	for r in range(len(plays_rank)):
		for i in range(2):
			if i == 1 and len(hash_map[plays_rank[r]]) < 2:
				continue
			temp = plays.index(hash_map[plays_rank[r]][i])
			plays[temp] = 0
			answer += [temp]

	return answer


# print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
# print(solution(["classic", "classic", "classic", "classic", "pop"], [500, 150, 800, 800, 2500]))
