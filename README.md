# README



[TOC]



---
---
---



## CheckiO Game


>   [CheckiO Game](https://py.checkio.org/)
>
>   [Code by ZpRoc in GitHub](https://github.com/ZpRoc/checkio)



## Elementary


### p03_acceptable_password_i

#### if 条件语句的简洁写法

```python
>>> flg = True if len(password) > 6 else False
```


### p13_nearest_value

#### 多重排序

```python
### 使用 key 进行控制，先选择最接近的，再选择数值小的
### sorted() 也有相同的 key 参数
>>> index = min(values, key=lambda n: (abs(one - n), n))
```



## Home


### p04_right_to_left

#### list.join()

```python
### list 的 join() 方法
>>> val = ['a', 'b', 'c']
>>> print(','.join(val))
a,b,c
```


### p06_days_between

#### datetime

```python
>>> from datetime import datetime
```


### p07_count_digits

#### for 循环语句的简洁写法

```python
>>> sum([ch.isdigit() for ch in text])
```


### p14_sort_array_by_element_frequency

#### 多重排序 sorted()

```python
### 先按照出现的次数的降序排列，再按照出现的位置的升序排列
>>> sorted(items, key = lambda x: (-items.count(x), items.index(x)))
```


### p16_sun_angle

#### datetime.strptime()

```python
>>> from datetime import datetime
>>> times = datetime.strptime(time, '%H:%M')
>>> h     = times.hour
>>> m     = times.minute
```

```python
>>> from datetime import datetime
>>> cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
>>> print(cday)
2015-06-01 18:19:59
```


### p19_date_and_time_converter

#### datetime.strftime()

```python
>>> from datetime import datetime
>>> now = datetime.now()
>>> print(now.strftime('%a, %b %d %H:%M'))
Mon, May 05 16:28
```


### p20_morse_decoder

#### str.capitalize()

```python
### 将字符串的第一个字母变成大写,其他字母变小写
>>> str.capitalize()
```



## Electronic Station


### p02_sort_by_extension

#### str.lsplit() & str.rsplit()

```python
### 同 str.split()
### 类似: str.strip(), str.lstrip(), str.rstrip()
```














