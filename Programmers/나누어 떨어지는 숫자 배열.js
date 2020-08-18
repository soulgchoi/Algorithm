function solution(arr, divisor) {
    const answer = []
    for (let element of arr) {
        if ((element % divisor) === 0) answer.push(element)
    }
    // 이거랑
    answer.sort((a, b) => a - b)
    return answer.length < 1 ? [-1] : answer
    // 이거랑 실행 속도는 별 차이 없음
    // return answer.length < 1 ? [-1] : answer.sort((a, b) => a - b)
}