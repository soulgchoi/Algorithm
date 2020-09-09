function solution(number, k) {
    let n = number.length - k
    const answer = []
    for (let i=0; i<number.length; i++) {
        let temp = number[i]
        while (k > 0 && answer[answer.length -1] < temp) {
            answer.pop()
            k -= 1
        }
        answer.push(temp)
    }
    return answer.length > n ? answer.slice(0, n).join('') : answer.join('')
}

// 하나 시간초과 (최대 자릿수인듯)
function solution(number, k) {
    k = number.length - k
    let i = 0
    while (i < k + 1 && number.length > k) {
        if (number[i] < number[i+1]) {
            number = number.substring(0, i) + number.substring(i+1)
            i = 0
        } else {
            i += 1
        }
    }
    return number.length > k ? number.substring(0, k) : number
}
