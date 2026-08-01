class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        
        if key not in self.store:
            self.store[key] = []

        self.store[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        
        if key not in self.store:
            return ""
        
        value = self.store[key]
        left = 0
        right = len(value)-1
        answer = ""
        while left <= right:
            mid = (left+right)//2

            time1,value1 = value[mid]

            if time1 <= timestamp:
                answer = value1
                left = mid + 1
            else:
                right = mid - 1

        return answer            


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)