function solution(progresses, speeds) {
    let answer = []
    let done = []
    let flag = true
    while (progresses.length) {
        done = []
        for (let i=0; i<progresses.length; i++) {
            flag = true
            progresses[i] += speeds[i]
            if (progresses[i] >= 100) {
                for (let j=0; j<i; j++) {
                    if (progresses[j] < 100) {
                        flag = false
                    }
                }
                if (flag) done.push(i)
            }
        }
        if (done.length) {
            answer.push(done.length)
            while (done.length) {
                progresses.shift()
                speeds.shift()  // 이 부분 빼먹어서 오래걸림
                done.shift()
            }
        }
    }
    return answer
}