function solution(n, m) {
    function greatestCommonDivisor(a, b) {
       return b === 0 ? a : greatestCommonDivisor(b, a % b)
    }
    const commonDivisor = greatestCommonDivisor(n, m)
    const commonMultiple = (n * m) / commonDivisor
    return [commonDivisor, commonMultiple]
}