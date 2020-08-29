function solution(phone_number) {
    let answer = ''
    const phoneNumber = phone_number.split('')
    const hidden = phoneNumber.splice(0, phoneNumber.length-4)
    answer += '*'.repeat(hidden.length)
    answer += phoneNumber.join('')
    return answer
}