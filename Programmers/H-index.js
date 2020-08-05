function solution(citations) {
    var answer = 0;
    for (let i=0; i<citations.length+1; i++) {
        let cttArray = [];
        for (var idx in citations) {
            if (Math.floor(citations[idx] / i) >= 1) {
                cttArray[idx] = 1
            } else cttArray[idx] = 0
        }
        const maxH = cttArray.reduce((acc, car) => acc + car)
        if (i <= maxH && i > answer) {
            answer = i
        }
    }
    return answer;
}

// 다른 풀이
function solution2(citations) {
  const citation = citations.sort((a, b) => b - a)
  let i = 0
  while (i+1 <= citation[i]) {
    i++
  }
  return i
}