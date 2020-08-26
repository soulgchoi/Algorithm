// reduce 메서드는 너무너무 좋다.
function solution(arr) {
    const answer = arr.reduce((acc, cur) => {
        return acc + cur
    })
    return answer / arr.length
}