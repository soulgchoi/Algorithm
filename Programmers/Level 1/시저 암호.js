function solution(s, n) {
    const upper = [...Array(26).keys()].map(i => String.fromCharCode(i + 65))
    const lower = [...Array(26).keys()].map(i => String.fromCharCode(i + 97))
    const answer = []
    for (let val of s) {
        if (val === ' ') {
            answer.push(' ')
        } else if (val === val.toLowerCase()) {
            answer.push(lower[(lower.indexOf(val) + n) % lower.length])
        } else {
            answer.push(upper[(upper.indexOf(val) + n) % upper.length])
        }
    }
    return answer.join('');
}