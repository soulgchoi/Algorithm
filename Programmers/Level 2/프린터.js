function solution(priorities, location) {
    let answer = 0
    const copyPriorities = priorities.reduce((acc, cur, idx) => {
        acc.push({ [idx] : cur })
        return acc
    }, [])
    while (priorities) {
        const max = priorities.reduce((a, b) => Math.max(a, b))
        const J = copyPriorities.shift()
        const j = priorities.shift()
        if (Object.values(J)[0] === max) {
            answer += 1
            if (Object.keys(J)[0] == location) break
        } else {
            copyPriorities.push(J)
            priorities.push(j)
        }
    }
    return answer
}