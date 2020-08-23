function solution(n) {
    let answer = 0;
    for (let m of n.toString()) {
        answer += parseInt(m)
    }
    return answer;
}