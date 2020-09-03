function solution(skill, skill_trees) {
    let answer = 0
    let preSkill = Array(skill.length)
    let flag = true
    for (let skill_tree of skill_trees) {
        flag = true
        preSkill.fill(0)
        for (let i=0; i<skill_tree.length; i++) {
            if (preSkill[skill.indexOf(skill_tree[i]) - 1] === 0) {
                flag = false
                break
            }
            else preSkill[skill.indexOf(skill_tree[i])] = 1
        }
        if (flag) answer += 1
    }
    return answer
}