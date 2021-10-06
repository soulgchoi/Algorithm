def solution(table, languages, preferences):
    works = []
    table = [t.split(' ') for t in table]
    new_table = {}
    for t in table:
        new_table[t[0]] = t[1:]  # score = 5 - idx
        works += [t[0]]
    print(new_table)

    works.sort()

    answer = [0] * len(works)
    for w in range(len(works)):
        score = 0
        for i in range(len(languages)):
            work = new_table.get(works[w])
            temp = work.index(languages[i]) if languages[i] in work else 5
            score += (5 - temp) * preferences[i]
        answer[w] = score
    print(answer)
    return works[answer.index(max(answer))]


print(solution(["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++",
                "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP",
                "GAME C++ C# JAVASCRIPT C JAVA"], ["PYTHON", "C++", "SQL"], [7, 5, 5]))  # HARDWARE
print(solution(["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++",
                "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP",
                "GAME C++ C# JAVASCRIPT C JAVA"], ["JAVA", "JAVASCRIPT"], [7, 5]))  # PORTAL
