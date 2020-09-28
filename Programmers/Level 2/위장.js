function solution(clothes) {
    let answer = 0
    let wardrobe = {}
    clothes.forEach((c) => {
        wardrobe[c[1]] ? wardrobe[c[1]].push(c[0]) : wardrobe[c[1]] = [c[0]]
    })
    for (let val of Object.values(wardrobe)) {
        answer ? answer *= val.length + 1 : answer += val.length + 1
    }
    answer -= 1
    return answer
}