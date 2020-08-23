// 이 문제를 푸는 의미가 뭘까?
function solution(n) {
    return parseInt(n.toString().split('').sort((a, b) => b > a).join(''))
}