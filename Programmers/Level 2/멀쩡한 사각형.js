// 최대 공약수 문제;;
const greatestCommonDivisor = (a, b) => {
       return b === 0 ? a : greatestCommonDivisor(b, a % b)
    }

function solution(w, h) {
    const gcd = greatestCommonDivisor(w, h)
    return (w * h) - ((w / gcd) + (h / gcd) - 1) * gcd
}