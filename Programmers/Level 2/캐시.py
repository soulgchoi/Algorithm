# 0 처리 빼먹지 말기
def solution(cacheSize, cities):
    ans = 0
    cache = {}
    cities = [city.lower() for city in cities]
    if cacheSize == 0:
        return len(cities) * 5
    for c in cities:
        if c in cache.keys():
            ans += 1
            cache[c] = ans
        else:
            if len(cache) == cacheSize:
                cache.pop(min(cache, key=cache.get))
            ans += 5
            cache[c] = ans
    return ans