function solution(arr) {
    const min = arr.reduce((acc, cur) => {
        return acc >= cur ? cur : acc
    })
    arr.splice(arr.indexOf(min), 1)
    return arr.length < 1 ? [-1] : arr;
}