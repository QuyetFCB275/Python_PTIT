from datetime import time, timedelta

class address:
    def __init__(self, id, name, rain, time) -> None:
        self.id = id
        self.name = name
        self.rain = rain
        self.time = time
        self.avg = 0
    
    def update_rain(self, k):
        self.rain += k
    def update_time(self, k):
        self.time += k
    def update(self):
        self.avg = self.rain / self.time
    def __str__(self) -> str:
        return f'{self.id} {self.name} {self.avg:.2f}'
    
if __name__ == "__main__":
    dt = {}
    dem = 0
    for i in range(int(input())):
        add = input()
        x1, x2 = input(), input()
        count = float(input())
        time1 = time(int(x1[0:2]), int(x1[3:]))
        time2 = time(int(x2[0:2]), int(x2[3:]))
        dt1 = timedelta(hours=time1.hour, minutes=time1.minute, seconds=time1.second)
        dt2 = timedelta(hours=time2.hour, minutes=time2.minute, seconds=time2.second)
        delta = dt2 - dt1
        if add not in dt:
            dem += 1
            id = "T" + format(dem, "02d")
            a = address(id, add, count, delta.total_seconds()/3600)
            dt[add] = a
        else:
            a = dt[add]
            a.update_rain(count)
            a.update_time(delta.total_seconds()/3600)
            a.update()
    for x in dt:
        print(dt[x])