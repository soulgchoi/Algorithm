// 삼항연산자에서 조건을 좀 더 유연하게 줄 수 있어야겠다.
function solution(N, stages) {
    const fail = {}
    for (let n=0; n<N; n++) {
        if (stages.filter((stage) => stage === n+1).length) {
            fail[n+1] = stages.filter((stage) => stage === n+1).length / stages.filter((stage) => stage >= n+1).length
        } else fail[n+1] = 0
    }
    const answer = Object.keys(fail).sort((a, b) =>
        fail[a] === fail[b] ? a - b : fail[b] - fail[a]
    ).map((key) => parseInt(key))
    return answer;
}