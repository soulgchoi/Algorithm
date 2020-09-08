const powerset = (array) => {
  const result = [[]]
  for (let value of array) {
    const length = result.length
    for (let i=0; i<length; i++){
      let temp = result[i].slice(0)
      temp.push(value)
      result.push(temp)
    }
  }
  return result;
}

const permutation = (array) => {
    return array.reduce((arr, ele) => {
        const result = []
        arr.forEach((a) => {
            for (let i=a.length; i>=0; i--) {
                const newa = [].concat(a)
                newa.splice(i, 0, ele)
                result.push(newa)
            }
        })
        return result
    }, [[]]
    )
}

function solution(numbers) {
    let newNumbers = powerset(numbers).splice(1).map((a) => a.join('')).reduce((a, b) =>
        a.includes(b) ? a : [...a, b]
    , [])
    let answer = []
    for (let number of newNumbers) {
        const num = permutation(number.split(''))
        for (let n of num) {
            n = parseInt(n.join(''))
            let flag = true
            for (let i=2; i<n; i++) {
                if ((n % i) === 0) {
                    flag = false
                    break
                }
            }
            if (n > 1 && flag) answer.push(n)
        }
    }
    answer = [...new Set(answer)]
    return answer.length
}