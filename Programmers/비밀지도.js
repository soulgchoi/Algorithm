function solution(n, arr1, arr2) {
    const answer = []
    for (let i=0; i<n; i++) {
        let binArr1 = arr1[i].toString(2)
        binArr1 = binArr1.length < n ? '0'.repeat(n - binArr1.length) + binArr1 : binArr1
        let binArr2 = arr2[i].toString(2)
        binArr2 = binArr2.length < n ? '0'.repeat(n - binArr2.length) + binArr2 : binArr2
        const temp = []
        for (let j=0; j<n; j++) {
            temp.push(binArr1[j] | binArr2[j] ? '#' : ' ')
        }
        answer.push(temp.join(''))
    }
    return answer
}