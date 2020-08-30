// 수학을 못해서 망할듯
function solution(n) {
    let answer = ''
    const rule = ['4', '1', '2']
    while (n > 0) {
        answer += rule[n % 3]
        if (n % 3 === 0) n -= 1
        n = parseInt(n / 3)
    }
    return answer.split('').reverse().join('')
}