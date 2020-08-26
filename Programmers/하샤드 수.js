function solution(x) {
    return x % (x.toString().split('').map(a => parseInt(a)).reduce((a, b) => a + b)) ? false : true
}

// 웹스톰이 고쳐줌;
function solution2(x) {
    return !(x % (x.toString().split('').map(a => parseInt(a)).reduce((a, b) => a + b)))
}