import heapq

def solution(scoville, K):
	answer = 0
	return answer

# def solution(scoville, K):
# 	answer = 0
# 	l = len([x for x in scoville if x >= K])
# 	j = len([y for y in scoville if y < K])
# 	while j > 0:
# 		if len(scoville) < 2:
# 			return -1
# 		scoville.sort()
# 		min_sc = scoville[0]
# 		if min_sc >= K:
# 			l -= 1
# 		else:
# 			j -= 1
# 		scoville.remove(min_sc)
# 		snd_sc = scoville[0]
# 		if snd_sc >= K:
# 			l -= 1
# 		else:
# 			j -= 1
# 		scoville.remove(snd_sc)
# 		n_sc = min_sc + (snd_sc*2)
# 		if n_sc >= K:
# 			l += 1
# 		else:
# 			j += 1
# 		scoville += [n_sc]
# 		answer += 1
# 	return answer


solution([1, 2, 3, 9, 10, 12], 7)
