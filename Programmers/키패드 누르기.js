// 40점짜리 코드
function solution(numbers, hand) {
    let answer = ''
    let left = 10
    let right = 12

    function dis(num) {
        if ([1, 3].includes(num)) {
            return 1
        } else if ([2, 4, 6].includes(num)) {
            return 2
        } else if ([5, 7, 9].includes(num)) {
            return 3
        } else if ([8, 10].includes(num)) {
            return 4
        }
    }

    for (let number of numbers) {
        if (number === 0) number = 11
        if (number % 3 === 1) {
            answer += 'L'
            left = number
        } else if (number % 3 === 0) {
            answer += 'R'
            right = number
        } else if (number % 3 === 2) {
            let cLeft =  dis(Math.abs(number - left))
            let cRight = dis(Math.abs(number - right))
            if (cLeft === cRight) {
                if (hand === 'left') {
                    answer += 'L'
                    left = number
                } else {
                    answer += 'R'
                    right = number
                }
            } else {
                if (cLeft > cRight) {
                    answer += 'R'
                    right = number
                } else {
                    answer += 'L'
                    left = number
                }
            }
        }
    }
    return answer;
}