// 맘에 안든다..
function solution(answers) {
    const one = [1, 2, 3, 4, 5]
    const two = [2, 1, 2, 3, 2, 4, 2, 5]
    const three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    const grade = [0, 0, 0]

    for (let i=0; i<answers.length; i++) {
        if (answers[i] === one[i % 5]) grade[0] += 1
        if (answers[i] === two[i % 8]) grade[1] += 1
        if (answers[i] === three[i % 10]) grade[2] += 1
    }

    const max = grade.reduce((a, b) => Math.max(a, b))
    const answer = []
    grade.forEach((g, idx) => {
        if (g === max) answer.push(idx+1)
    })
    return answer;
}