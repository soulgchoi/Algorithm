function solution(strings, n) {
    strings.sort((a, b) => {
        if (a[n] > b[n]) {  // 인덱스(n) 기준으로 정렬
            return 1
        } else if (a[n] === b[n]) {  // 같으면,
            return (a > b) ? 1 : -1  // 전체를 비교해서 정렬
        } else {
            return -1
        }
    })
    return strings;
}