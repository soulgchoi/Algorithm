function solution(board, moves) {
  const size = board.length
  // 배열을 회전시킨다.
  const newBoard = board[0].map(function(col, i) {
    return board.slice(0).reverse().map(function(row) {
      return row[i]
    })
  });
  const basket = Array()
  let answer = 0
  moves.forEach(move => {
    for (let b=size-1; b>-1; b--) {
      if (newBoard[move-1][b] !== 0) {
        // 자바스크립트 Array 의 [-1] 은 파이썬처럼 동작하지 않는다.
        // length -1 로 할 것..
        if (basket.length > 0 && basket[basket.length-1] === newBoard[move-1][b]) {
          basket.pop()
          answer += 2
        } else {
          basket.push(newBoard[move-1][b])
        }
        newBoard[move-1][b] = 0
        break
      }
    }
  })
  return answer;
}