# Первая задача
```python
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr = sorted(arr)
        if len(arr) <= 2:
            return True
        diff = arr[1] - arr[0]
        for i in range(2, len(arr)):
            if arr[i] - arr[i-1] != diff:
                return False
        return True
```


# Вторая задача
```python
import math

class Solution:
    def pivotInteger(self, n: int) -> int:
        S = n * (n + 1) // 2
        sqrt_S = math.isqrt(S)
        if sqrt_S * sqrt_S == S:
            return sqrt_S
        else:
            return -1
```
