function solution(s) {
    let answer = []
    for (let i=Math.floor((s.length-1) / 2)+1; i>=0; i--) {
        let j = 0
        let string = []
        while (j < s.length) {
          string.push(s.substring(j, j+i+1))
          j += i + 1
        }
        let count = 0
        let newString = []
        let temp = string.shift()
        while (string.length) {
          if (temp === string[0]) {
            count >= 2 ? count += 1 : count += 2
            if (count > 2) {
              string.shift()
              newString.pop()
              newString.push(count + temp)
            } else if (count > 0) {
              string.shift()
              newString.push(count + temp)
            }
          } else {
            if (count < 1) newString.push(temp)
            count = 0
            if (string.length === 1) newString.push(string[0])
            temp = string.shift()
          }
        }
        if (newString.length < 1) newString = [temp]
        answer.push(newString.join('').length)
    }
    return answer.reduce((a, b) => a < b ? a : b)
}
