// 마지막을 다르게 처리할 수 없을까? 심란하다.
function solution(s) {
    let answer = ''
    const sentence = s.split(' ')
    for (let char of sentence) {
        for (let i=0; i<char.length; i++) {
            if (i % 2) {
                answer += char[i].toLowerCase()
            } else answer += char[i].toUpperCase()
        }
        answer += ' '
    }
    return answer.slice(0, -1);
}