// 쉽게 생각하면 풀린다!
const findPos = (obj, num) => {
    return Object.keys(obj).find((key) => obj[key].includes(num))
}

function solution(numbers, hand) {
    let answer = ''
    let keypad = { 0: [1, 2, 3], 1: [4, 5, 6], 2: [7, 8, 9], 3: [10, 0, 12]}
    let left = 10
    let right = 12
    numbers.forEach((number) => {
        if ([1, 4, 7].includes(number)) {
            answer += 'L'
            left = number
        }
        if ([3, 6, 9].includes(number)) {
            answer += 'R'
            right = number
        }
        if ([2, 5, 8, 0].includes(number)) {
            const posX = findPos(keypad, number)
            const posY = keypad[posX].indexOf(number)

            const leftX = findPos(keypad, left)
            const leftY = keypad[leftX].indexOf(left)

            const rightX = findPos(keypad, right)
            const rightY = keypad[rightX].indexOf(right)

            const disL = Math.abs(posX - leftX) + Math.abs(posY - leftY)
            const disR = Math.abs(posX - rightX) + Math.abs(posY - rightY)

            if (disL === disR) {
                if (hand === 'left') {
                    answer += 'L'
                    left = number
                } else {
                    answer += 'R'
                    right = number
                }
            } else if (disL < disR) {
                answer += 'L'
                left = number
            } else {
                answer += 'R'
                right = number
            }
        }
    })
    return answer
}

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