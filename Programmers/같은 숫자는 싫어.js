// 시간초과;
function solution(arr) {
    arr = arr.reduce((acc, cur, idx) =>
        arr[idx-1] === cur ? acc : [...acc, cur]
          , [])
    return arr;
}