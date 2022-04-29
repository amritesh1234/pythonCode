from collections import deque
class HitCounter:
    def __init__(self):
        self.q = deque()

    def add(self, timestamp):
        self.q.append(timestamp)
        while self.q:
            if self.q[0] < timestamp - 60:
                self.q.popleft()
            else:
                break

    def count(self, timestamp):
        while self.q:
            if self.q[0] < timestamp - 60:
                self.q.popleft()
            else:
                break
        return len(s)


s = HitCounter()
print(s.add(0))
print(s.add(0))
print(s.count(60))
# print(s.add(70))
# print(s.count(100))
