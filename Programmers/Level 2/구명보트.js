function solution(people, limit) {
    var answer = 0
    people = people.sort((a, b) => b - a)
    let [left, right] = [0, people.length-1]
    while (left < right) {
        if (people[left] + people[right] > limit) {
            left += 1
        } else {
            left += 1
            right -= 1
        }
        answer += 1
    }
    if (left === right) answer += 1
    return answer
}