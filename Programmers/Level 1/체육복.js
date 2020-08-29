// 맞았지만 찝찝하다.
// 더 좋은 방법을 찾기
function solution(n, lost, reserve) {
    const clothes = [...new Set(lost.concat(reserve))]
    const copyLost = lost.slice()
    const copyReserve = reserve.slice()
    let answer = n - clothes.length
    lost.forEach((l) => {
        reserve.forEach((r) => {
            if (l > 0 && r > 0) {
                if (!copyReserve.includes(l) && !copyLost.includes(r)) {
                    if (Math.abs(l - r) === 1) {
                        reserve[reserve.indexOf(r)] = -1
                        lost[lost.indexOf(l)] = -1
                        l = -1
                    }
                } else {
                    if (!copyReserve.includes(l)) reserve[reserve.indexOf(r)] = -1
                }
            }
        })
    })
    const countLost = lost.filter(val => val === -1).length
    return answer + countLost + reserve.length;
}