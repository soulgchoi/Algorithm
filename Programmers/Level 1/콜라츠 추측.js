function solution(num) {
    function collatz(num) {
        return num % 2 ? (num * 3) + 1 : num / 2
    }
    let answer = 0
    let curNumber = num
    while (curNumber !== 1) {
        if (answer >= 500 ) {
            return -1
        } else {
            curNumber = collatz(curNumber)
            answer += 1
        }
    }
    return answer
}

// 아래는 재귀로 만들고 싶어서 부득불 짠 코드
const getCollatz = function (num) {
    return num % 2 ? (num * 3) + 1 : num / 2
}

const countCollatz = function (num, count) {
    return (num === 1) ? count : (count >= 500 ? -1 : countCollatz(getCollatz(num), count + 1))
}

const solution2 = function(num) {
    return countCollatz(num, 0)
}