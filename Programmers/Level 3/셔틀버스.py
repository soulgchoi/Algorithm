def solution(n, t, m, timetable):
    timetable = [int(time[:2]) * 60 + int(time[3:5]) for time in timetable]
    timetable.sort()
    last_time = (60 * 9) + (n - 1) * t

    for i in range(n):
        if len(timetable) < m:
            return '%02d:%02d' % (last_time // 60, last_time % 60)
        if i == n - 1:
            if timetable[0] <= last_time:
                last_time = timetable[m - 1] - 1
            return '%02d:%02d' % (last_time // 60, last_time % 60)
        for j in range(m - 1, -1, -1):
            bus_arrive = (60 * 9) + i * t
            if timetable[j] <= bus_arrive:
                del timetable[j]


print(1, 1, 5, ["08:00", "08:01", "08:02", "08:03"])
print(2, 10, 2, ["09:10", "09:09", "08:00"])
print(2, 1, 2, ["09:00", "09:00", "09:00", "09:00"])
print(1, 1, 5, ["00:01", "00:01", "00:01", "00:01", "00:01"])
print(1, 1, 1, ["23:59"])
print(10, 60, 45,
      ["23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59",
       "23:59", "23:59", "23:59", "23:59"])
