function solution(s) {
    let answer = ''
    if (s.length % 2) {
        answer = s.substr((s.length / 2), 1)
    } else {
        answer = s.substr((s.length / 2) - 1, 2)
    }
    return answer;
}