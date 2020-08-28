function solution(d, budget) {
  if (d.reduce((a, b) => a + b) <= budget) return d.length
  if (Math.min(...d) > budget) return 0  // 이 부분 추가 안하면 틀림
  while (d.reduce((a, b) => a + b) > budget) {
    d.splice(d.indexOf(Math.max(...d)), 1)
  }
  return d.length
}

// 이 코드는 26점
// 덕분에 powerset 알고리즘을 이것저것 찾아보았다.
const PowerSet = (array, budget) => {
  const result = [[]]
  for (let value of array) {
    const length = result.length
    for (let i=0; i<length; i++){
      let temp = result[i].slice(0)
      temp.push(value)
      if (temp.reduce((a, b) => a + b) <= budget) {
        result.push(temp)
      }
    }
  }
  return result;
}

function solution2(d, budget) {
  const powersets = PowerSet(d, budget)
  return Math.max.apply(Math, powersets.map((powerset) => powerset.length ))
}