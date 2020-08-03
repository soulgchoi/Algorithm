// const quickSort = array => {
//     if (array.length < 2) return array;
//
//     const pivot = array[array.length - 1].toString();
//     const left = [], right = [];
//
//     for (let i = 0; i < array.length - 1 ; i++) {
//         let stringifiedNum = array[i].toString()
//         if (stringifiedNum[0] > pivot[0]) {
//             left.push(stringifiedNum)
//         } else if (stringifiedNum[0] === pivot[0]) {
//
//             if (stringifiedNum.length > pivot.length) {
//                 for (let j=0; j<pivot.length; j++) {
//                     if (stringifiedNum[j+1] > pivot[j]) {
//                         left.push(stringifiedNum)
//                     } else right.push(stringifiedNum);
//                 }
//             } else if (stringifiedNum.length < pivot.length) {
//                 for (let k=0; k<stringifiedNum.length; k++) {
//                     if (stringifiedNum[k] > pivot[k+1]) {
//                         left.push(stringifiedNum)
//                     } else right.push(stringifiedNum)
//                 }
//             } else if (stringifiedNum.length === pivot.length) {
//                 for (let l=1; l<stringifiedNum.length; l++) {
//                     if (stringifiedNum[l] > pivot[l]) {
//                         left.push(stringifiedNum)
//                     } else right.push(stringifiedNum)
//                 }
//             }
//         }
//         else right.push(stringifiedNum);
//     }
//     return [...quickSort(left), pivot, ...quickSort(right)];
// };
//
// function solution(numbers) {
//     var sortedArr = quickSort(numbers)
//     var answer = sortedArr.join("")
//     return answer
// }

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