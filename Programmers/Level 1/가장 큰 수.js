// 틀림
function solution(numbers) {
    var strArr = numbers.map(number => number.toString())
    var maxLeng = strArr.map(char => char.length).reduce((a, b) => Math.max(a, b))
    var sortedArr = strArr.map(function(number) {
        var idx = strArr.indexOf(number)
        if (number.length < maxLeng) {
            for (let i=0; i<maxLeng-number.length+1; i++) {
                number += number[0];
            }
        }
        return [number, idx]
    })
    sortedArr = sortedArr.sort((a, b) => b[0] - a[0])
    var answer = [];
    for (let j=0; j<sortedArr.length; j++) {
        answer.push(strArr[sortedArr[j][1]])
    }
    if (answer[0] == 0) {
        return '0'
    } else return answer.join('')
}


// 조건 하나 빼먹은듯..
function solution2(numbers) {
    const maxLeng = 4
    const unsortedObj = {};
    for (let i=0; i<numbers.length; i++) {
        let stringifiedNum = numbers[i].toString()
        stringifiedNum += stringifiedNum[0].repeat(maxLeng-stringifiedNum.length+1)
        unsortedObj[stringifiedNum] = numbers[i]
    }
    const sortedObj = Object.values(unsortedObj).reverse()
    return sortedObj.join('')
}


const sortFunc = array => {
    if (array.length < 2) return array;

    const pivot = array[array.length - 1];
    const left = [], right = [];

    for (let i = 0; i < array.length - 1 ; i++) {
        let compare = array[i]
        if (compare[0] > pivot[0]) {
            left.push(compare)
        } else if (compare[0] === pivot[0]) {
            if (compare.length == pivot.length) {
                if (compare > pivot) {
                    left.push(compare)
                } else right.push(compare);
            } else {
                const cLength = compare.length
                const pLength = pivot.length
                if (cLength > pLength) {
                    const pivot2 = pivot + pivot[0].repeat(cLength - pLength)
                    if (compare > pivot2) {
                    left.push(compare)
                    } else if (compare == pivot2) {
                        if (compare + pivot > pivot + compare) {
                            left.push(compare)
                        } else right.push(compare)
                    } else right.push(compare);
                } else if (cLength < pLength) {
                    const compare2 = compare + compare[0].repeat(pLength - cLength)
                    if (compare2 > pivot) {
                        left.push(compare)
                    } else if (compare2 === pivot) {
                        if (compare + pivot > pivot + compare) {
                            left.push(compare)
                        } else right.push(compare)
                    } else right.push(compare);
                }
            }
        }
        else right.push(compare);
    }
    return [...sortFunc(left), pivot, ...sortFunc(right)];
};

function solution3(numbers) {
    var strArr = numbers.map(number => number.toString())
    var answer = sortFunc(strArr)
    if (answer[0] == 0) {
        return '0'
    } else return answer.join('')
}

// 이게 찐 정답이었다..
function solution4(numbers) {
    const strArr = numbers.map((number) => number.toString())
    const sortedNumbers = strArr.sort((a, b) => (b + a) - (a + b))
    return sortedNumbers[0] === '0' ? '0' : sortedNumbers.join('')
}
