function solution(a, b) {
    if (a > b) [a, b] = [b, a]  // 아래에서 따로 조건문 쓰지 않도록 값 교환
    let answer = 0
    for (let i=a; i<b+1; i++) {
        answer += i
    }
    return answer
}