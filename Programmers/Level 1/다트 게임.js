const pow = (n, p) => {
    if (p === 'S') return Math.pow(n, 1)
    if (p === 'D') return Math.pow(n, 2)
    if (p === 'T') return Math.pow(n, 3)
}

function solution(dartResult) {
    let answer = 0
    let prev = 'p'
    let cur = 0
    for (let i=0; i<dartResult.length; i++) {
        if (dartResult[i] == parseInt(dartResult[i])) {
            if (prev !== 'p') { answer += prev }
            if (i > 0) { prev = cur }
            cur = dartResult[i]
            if (cur === '1' && dartResult[i+1] === '0') {
                cur = 10
                i += 2
            }
        }
        if (['S', 'D', 'T'].includes(dartResult[i])) {
            cur = pow(cur, dartResult[i])
        }
        if (dartResult[i] === '*') {
            if (prev !== 'p') prev *= 2
            cur *= 2
        }
        if (dartResult[i] === '#') {
            cur *= -1
        }
        if (i === dartResult.length - 1) {
            answer += cur
            answer += prev
        }
    }
    return answer;
}

// 90점짜리 코드
function solution(dartResult) {
    let answer = [0, 0, 0, 0]
    dartResult = dartResult.replace(/10/gi, 'k') + 's'
    dartResult = dartResult.split('')
    const numbers = dartResult.filter((dart) => (dart == parseInt(dart)) || (dart === 'k'))
    for (let i=1; i<4; i++) {
        const temp = dartResult.slice(dartResult.indexOf(numbers[i-1]), dartResult.indexOf(numbers[i]))
        let score = 0
        for (let t of temp) {
            if (t == parseInt(t)) {
                score = parseInt(t)
            } else if (t === 'k') {
                score = 10
            } else if (t === 'D') {
                score = Math.pow(score, 2)
            } else if (t === 'T') {
                score = Math.pow(score, 3)
            } else if (t === '*') {
                score *= 2
                answer[i-1] *= 2
            } else if (t === '#') {
                score *= -1
            }
        }
        answer[i] = score
    }
    return answer.reduce((a, b) => a + b);
}