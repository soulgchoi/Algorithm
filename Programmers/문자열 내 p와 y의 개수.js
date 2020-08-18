function solution(s){
    let answer = true;
    const lower = s.toLowerCase();
    let p = 0
    let y = 0
    for (let str of lower) {
        if (str === 'p') p += 1
        else if (str === 'y') y += 1
    }
    (p === y) ? answer = true : answer = false
    return answer;
}