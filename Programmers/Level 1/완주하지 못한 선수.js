// 해시 문제라고 해서 값을 저장하는 방식으로 풀었는데,
// 별로 좋은 코드는 아닌 것 같다..
function solution(participant, completion) {
    const answer = {};
    participant.forEach((par) => {
        answer[par] ? answer[par] += 1 : answer[par] = 1
    })
    completion.forEach((com) => {
        answer[com] -= 1
    })
    return Object.keys(answer).find(key => answer[key] === 1);
}