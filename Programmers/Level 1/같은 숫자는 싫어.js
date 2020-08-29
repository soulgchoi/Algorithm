// 시간초과;
function solution(arr) {
    arr = arr.reduce((acc, cur, idx) =>
        arr[idx-1] === cur ? acc : [...acc, cur]
          , [])
    return arr;
}

// 통과
// 다른 메서드를 쓰는 게 더 오래걸리는 모양이다.
function solution2(arr) {
    const answer = []
    for (let i=0; i<arr.length; i++) {
        if (arr[i-1] !== arr[i]) answer.push(arr[i])
    }
    return answer;
}