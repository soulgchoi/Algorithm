const getAlphabet = (str) => {
    let result = 0
    let alphabet = [...Array(26).keys()].map(i => String.fromCharCode(i + 65))
    result = alphabet.indexOf(str)
    if (result > 13) {
        result = 26 - result
    }
    return result
}

function solution(name) {
    name = name.split('')
    let answer = 0
    let idx = 0
    let right = 1
    let left = 1
    while (true) {
        answer += getAlphabet(name[idx])
        name[idx] = 'A'
        if (name.filter((a) => a === 'A').length === name.length) break
        for (let i=1; i<name.length-1; i++) {
            let temp = idx + i
            if (temp > name.length - 1) temp = temp - name.length
            if (name[temp] === 'A') right += 1
            else break
        }
        for (let j=1; j<name.length-1; j++) {
            let temp = idx - j
            if (temp < 0) temp = name.length + temp
            if (name[temp] === 'A') left += 1
            else break
        }
        if (right > left) {
            answer += left
            if (idx - left < 0) idx = name.length + (idx - left)
            else idx -= left
        } else {
            answer += right
            if (idx + right > name.length-1) idx = (idx + right) - name.length
            else idx += right
        }
    }
    return answer
}


///////////////////////////////////
const getAlphabet = (str) => {
    let result = 0
    let alphabet = [...Array(26).keys()].map(i => String.fromCharCode(i + 65))
    result = alphabet.indexOf(str)
    if (result > 13) {
        result = 26 - result
    }
    return result
}

function solution(name) {
    let count = Array(name.length).fill(0)
    for (let i=0; i<name.length; i++) {
        count[i] = getAlphabet(name[i])
    }
    let countZero = count.filter((a) => a === 0).length
    if (count.reduce((a, b) => a + b) === 0) return 0
    else {
        let answer = 0
        let cnt = 0
        let idx = 0
        let flag = false
        let temp = 0
        let tempidx = 0
        while (cnt < count.length) {
            answer += count[idx]
            cnt += 1

            if (idx < count.length -2 && count[idx+1] === 0) {
                temp = 0
                tempidx = idx + 1
                while (count[tempidx] === 0) {
                    temp += 1
                    tempidx += 1
                }
                tempidx -= 1
                if (idx+1 < temp || temp === countZero) {
                    flag = true
                    answer += idx
                    idx = count.length
                }
            }
            flag ? idx -= 1 : idx += 1

            if (flag && temp > 0) {
                if (idx - temp <= tempidx - temp) {
                    return answer
                }
            } else if (temp > 0) {
                if (idx + temp === count.length-1) {
                    return answer
                }
            }
            answer += 1
        }
        return answer - 1
    }
}

/////////////////////////////////
const getAlphabet = (str) => {
    let result = 0
    let alphabet = [...Array(26).keys()].map(i => String.fromCharCode(i + 65))
    result = alphabet.indexOf(str)
    if (result > 13) {
        result = 26 - result
    }
    return result
}

function solution(name) {
    let answer = 0
    let idx = 0
    let flag = 'right'
    let check = Array(name.length).fill(-1)
    let count = 0
    while (count < name.length) {
        if (check[idx] >= 0) {
            flag === 'right' ? idx += 1 : (idx === 0 ? idx = name.length-1 : idx -= 1)
            answer += 1
        } else {
            answer += getAlphabet(name[idx])
            check[idx] = getAlphabet(name[idx])
            count += 1
            if (name[idx] === 'A') {
                let temp = 0
                while (name[idx+1] === 'A' && idx < name.length) {
                    temp += 1
                    idx += 1
                }
                let right = temp
                let left = idx - temp
                if (left < right) flag = 'left'
                idx = idx - temp
            }
            flag === 'right' ? idx += 1 : (idx === 0 ? idx = name.length-1 : idx -= 1)
            answer += 1
        }
    }
    console.log(answer, check)
    return answer
}

////////////////////////////////
function solution(name) {
    let alphabet = [...Array(26).keys()].map(i => String.fromCharCode(i + 65))
    alphabet.splice(0, 0,"0")

    let answer = alphabet.indexOf(name[0]) - 1
    answer > 13 ? answer = 26 - answer : answer
    let count = [answer]
    let idx = 0
    let temp1 = alphabet.indexOf(name[1]) - 1
    let temp2 = alphabet.indexOf(name[name.length-1]) - 1
    temp1 > 13 ? temp1 = 26 - temp1 : temp1
    temp2 > 13 ? temp2 = 26 - temp2 : temp2

    if (temp1 < temp2) {
        idx = name.length - 2
        answer += temp2
        count.push(temp2)
        while (count.length < name.length) {
            let stick = alphabet.indexOf(name[idx]) - 1
            if (stick > 13) {
                stick = 26 - stick
            }
            answer += stick
            idx -= 1
            count.push(stick)
        }
    } else {
        idx = 2
        count.push(temp1)
        answer += temp1
        while (count.length < name.length) {
            let stick = alphabet.indexOf(name[idx]) - 1
            if (stick > 13) {
                stick = 26 - stick
            }
            answer += stick
            idx += 1
            count.push(stick)
        }
    }
    let i = count.length - 1
    while (count[i] === 0) {
        count.pop()
        i -= 1
    }
    answer += count.length - 1
    return count.length < 1 ? 0 : answer
}