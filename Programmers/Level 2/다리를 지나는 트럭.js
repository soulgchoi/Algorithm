const arrSum = (arr) => {
    if (arr.length) {
        return arr.reduce((a, b) => a + b)
    } else return 0
}

function solution(bridge_length, weight, truck_weights) {
    let answer = 0
    let bridgeCount = Array(bridge_length).fill(0)
    let bridge = []
    let flag = true
    while (flag) {
        if (bridge.length) {
            for (let b=0; b<bridge.length; b++) {
                bridgeCount[b] += 1
            }
            if (bridgeCount[0] >= bridge_length) {
                bridge.shift()
                bridgeCount.shift()
                bridgeCount.push(0)
            }
        }
        if (truck_weights.length < 1) {
            if (arrSum(bridgeCount) === 0) {
                flag = false
            }
        }
        if (bridge.length < bridge_length) {
            let truck = truck_weights[0]
            if (arrSum(bridge) + truck <= weight) {
                truck = truck_weights.shift()
                bridge.push(truck)
            }
        }
        answer += 1
    }
    return answer
}