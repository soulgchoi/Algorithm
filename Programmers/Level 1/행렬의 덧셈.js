function solution(arr1, arr2) {
    const answer = new Array(arr1.length)
    for (let a=0; a<answer.length; a++) {
        answer[a] = new Array(arr1[0].length)
    }
    for (let i=0; i<arr1.length; i++) {
        for (let j=0; j<arr1[0].length; j++) {
            answer[i][j] = arr1[i][j] + arr2[i][j]
        }
    }
    return answer
}