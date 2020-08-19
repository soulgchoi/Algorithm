// 문자열 'e' 를 포함할 때를 굳이 조건에 넣은 이유는,
// 지수 표현 '1e22' 같은 것은 숫자로 인식되기 때문이다.
function solution(s) {
    if (s.length === 4 || s.length === 6) {
        return !(isNaN(s) || s.includes('e')) ? false : true
    } else return false
}

// 웹스톰이 코드를 줄여줌^^
function solution(s) {
    if (s.length === 4 || s.length === 6) {
        return !(isNaN(s) || s.includes('e'))
    } else return false
}