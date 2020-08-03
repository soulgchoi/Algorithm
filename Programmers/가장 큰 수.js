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

// 시간 초과로 실패