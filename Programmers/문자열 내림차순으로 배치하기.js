// for loop 와 split 때문에 실행속도가 크게 차이나지는 않았다.
function solution(s) {
    const answer = []
    for (let char of s) {
        answer.push(char)
    }
    answer.sort().reverse()
    return answer.join('')
}

function solution(s) {
    return s.split('').sort().reverse().join('')
}

// 처음에 대소문자를 구분해야 하는줄 알았는데,
// 아스키코드 기반으로 정렬해줘서 상관없었다.
function solution(s) {
    const lower = []
    const upper = []
    for (let char of s) {
        // 대신 대문자인지 소문자인지 이렇게 체크할 수 있음
        if (char === char.toLowerCase()) {
            lower.push(char)
        } else {
            upper.push(char)
        }
    }
    lower.sort().reverse()
    upper.sort().reverse()
    const answer = lower.concat(upper)
    return answer.join('')
}
