// 소수는 나의 적;

// 시간 초과
function solution(n) {
  const answer = [];
  for (let i = 2; i < n + 1; i++) {
      let flag = true
      for (let j = 0; j < answer.length; j++) {
          if ((i % answer[j]) === 0) {
              flag = false
              break
          }
      }
      if (flag) answer.push(i)
  }
  return answer.length;
}

// 효율성 테스트 시간 초과
function solution(n) {
    const answer = []
    for (let i=2; i<n+1; i++) {
        let flag = true
        for (let j=0; j<answer.length; j++){
            if (answer[j] < Math.sqrt(n)) {
                if ((i % answer[j]) === 0) {
                    flag = false
                    break
                }
            } else break
        }
        if (flag) answer.push(i)
    }
    return answer.length
}

// n 이 아니라 i 여야 했던 것
function solution(n) {
    const answer = []
    for (let i=2; i<n+1; i++) {
        let flag = true
        for (let j=0; j<answer.length; j++){
            if (answer[j] <= Math.sqrt(i)) {  // 여기!
                if ((i % answer[j]) === 0) {
                    flag = false
                    break
                }
            } else break
        }
        if (flag) answer.push(i)
    }
    return answer.length
}