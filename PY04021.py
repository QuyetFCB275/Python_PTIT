from datetime import time, timedelta


class person:
    def __init__(self, id, name, hour, minute):
        self.id = id
        self.name = name
        self.hour = hour
        self.minute = minute

    def __str__(self):
        return f'{self.id} {self.name} {self.hour} gio {self.minute} phut'

if __name__ == "__main__":
    lit = []
    for i in range(int(input())):
        id = input()
        name = input()

        t1 = input()
        t2 = input()
        time1 = time(int (t1[0:2]),int (t1[3:]))
        time2 = time(int(t2[0:2]), int(t2[3:]))
        dt1 = timedelta(hours=time1.hour, minutes=time1.minute)
        dt2 = timedelta(hours=time2.hour, minutes=time2.minute)
        delta = dt2 - dt1

        hour = int (delta.total_seconds() // 3600)
        minute = int ((delta.total_seconds() // 60) % 60)
        lit.append(person(id, name, hour, minute))
    lit.sort(key=lambda x : (-x.hour, -x.minute))
    for x in lit:
        print(x)