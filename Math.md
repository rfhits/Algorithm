# Math

## 分解质因数

利用递归

```python
def get_min_factor(num):
    sq = int(num**0.5) + 1
    for i in range(2, sq):
        if num % i == 0:
            return i
        else :
            pass
    return num

def get_factors(num):
    """return a list"""
    factors = []
    min_factor = get_min_factor(num)
    factors.append(min_factor)
    if min_factor == num:
        return factors
    else:
        factors.extend(get_factors(num // min_factor))
        return factors
      

print(get_factors(123124324324134334))
```
