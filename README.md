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


### p04_acceptable_password_2

#### any() & all()

```python
### any(): 如果不都为空、0、false，则返回 True
###        如果  都为空、0、false，则返回 False

>>>any(['a', 'b', 'c', 'd'])   # 列表list，元素都不为空或0
True
 
>>> any(['a', 'b', '', 'd'])   # 列表list，存在一个为空的元素
True
 
>>> any([0, '', False])        # 列表list,元素全为0,'',false
False
 
>>> any(('a', 'b', 'c', 'd'))  # 元组tuple，元素都不为空或0
True
 
>>> any(('a', 'b', '', 'd'))   # 元组tuple，存在一个为空的元素
True
 
>>> any((0, '', False))        # 元组tuple，元素全为0,'',false
False
  
>>> any([]) # 空列表
False
 
>>> any(()) # 空元组
False
```

```python
### all(): 所有 iterable 的元素不为 0、''、False 或者 iterable 为空
###        则 all(iterable) 返回 True，否则返回 False

>>> all(['a', 'b', 'c', 'd'])  # 列表list，元素都不为空或0
True
>>> all(['a', 'b', '', 'd'])   # 列表list，存在一个为空的元素
False
>>> all([0, 1，2, 3])          # 列表list，存在一个为0的元素
False
   
>>> all(('a', 'b', 'c', 'd'))  # 元组tuple，元素都不为空或0
True
>>> all(('a', 'b', '', 'd'))   # 元组tuple，存在一个为空的元素
False
>>> all((0, 1, 2, 3))          # 元组tuple，存在一个为0的元素
False
   
>>> all([])             # 空列表
True
>>> all(())             # 空元组
True
```


### p07_acceptable_password_5

#### in & not in

```python
### in, not in

# 以下两句等价
>>> str.count(ch) == 0
>>> ch not in str
```


### p09_all_upper_2

#### str.isupper() & str.islower()

```python
### str.isupper(): 判断字符串是否都是大写
### str.islower(): 判断字符串是否都是小写
```



## Mine


### p07_caesar_cipher_decryptor

#### ord() & chr()

```python
### ord(): char 转 byte
### chr(): byte 转 char
```



## Polygon









## Incinerator


### p01_the_warriors

#### @property 装饰器

```python
### 通过 @property 装饰器，可以直接通过方法名来访问方法
### 不需要在方法名后添加一对“（）”小括号。
>>> @property
>>> def 方法名(self)
>>>     代码块

### Example
@property
def health(self):
    return self._health

@health.setter
def health(self, value):
    self._health = value
```




