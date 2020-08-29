// 정렬 > K번째 수
function solution(array, commands) {
    var answer = [];
    for (const command of commands) {
        let [i, j, k] = command
        let sortedArray = array.slice(i-1, j).sort((a, b) => a - b)
        answer.push(sortedArray[k-1])
    }
    return answer;
}

// for 루프 대신 map 을 사용
function solution2(array, commands) {
    var answer = [];
    commands.map((command) => {
            let [i, j, k] = command
            let sortedArray = array.slice(i-1, j).sort((a, b) => a - b)
            answer.push(sortedArray[k-1])
        }
    )
    return answer;
}