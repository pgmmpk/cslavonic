# Church Slavonic numbers

WORK IN PROGRESS...

Church Slavonic uses lowercase letters for digits:

| number | digit |
|-------:|:-----:|
| 1 | а |
| 2 | в |
| 3 | г |
| 4 | д |
| 5 | е |

Combining these digits allows one to represent any number from 1 to 999, inclusive. The digits should follow
a specific sequence, that is derived from the order in which corresponding words are pronounced in Church Slavonic.

General rule is that higher digits are to the left of the lower digits. But numbers from 11 to 19 (inclusively)
are special and the order of digits there is reversed.

Here is the algorithm:
```python
def format_small_number(value):
    assert 1 <= value <= 999
    
    hundreds = (value // 100) * 100
    value -= hundreds
    tens     = (value // 10) * 10
    value -= tens
    assert 0 <= value <= 9

    if hundreds:
        output.append(CU_DIGIT_BY_NUMBER[hundreds])
        value -= hundreds
  
    assert value < 100
    if tens == 1:  # special order of digits
        if value:
            output.append(CU_DIGIT_BY_NUMBER[value])
        output.append(CU_DIGIT_BY_NUMBER[tens])
    else:
        if tens:
            output.append(CU_DIGIT_BY_NUMBER[tens])
        if value:
            output.append(CU_DIGIT_BY_NUMBER[value])
  
  return ''.join(output)
```

Placing titlo: 
1. place titlo over next to last digit (ignore thousand signs)
2. if next to last happen to be CU_800, place titlo over the last digit
3. if a single-digit number, place titlo over it (even if it is CU_800)
```
def place_titlo(numstring):
  assert len(numstring) > 0
   if len(numstring) > 1:
      if numstring[-2] != CU_THOUSAND:
         if numstring[-2] != CU_800:
            return numstring[:-1] + CU_TITLO + numstring[-1:]
      else:
         if len(numstring) > 2:
             if numstring[-3] != CU_THOUSAND:  # e.g. not "##a"
                 if numstring[-3] != CU_800:
                     return numstring[:-2] + CU_TITLO + numstring[-2:]
   return numstring + CU_TITLO
```

For numbers greater than 999 

Числа больше 999 записываются с помощью использования тех же цифр с добавлением тысящного знака:

| number | digit |
|-------:|:-----:|
| 1000   | #а |
| 2000   | #в |
| 3000   | #г |
| 4000   | #д |
| 5000   | #е |

При этом непонятно как записывать числа выше 10 000 так как примеров в существующих церковнославянских
текстах нет.

Мы сформулируем два немного различных подхода к представлению больших чисел: "стандартный" диалект и "старый" диалект.

## Старый диалект
Числа до 1 000 000 записываются с помощью цифр из таблиц A и B, без разделителя тысящных групп.

| decimal | Church Slavonic |
|--------:|:---------------:|
| 1001    | #аа             |
| 10232   | #iргв           |
...

Алгоритм `old_dialect`:
```python
Input: value

if value< 1000:
     return small_number(value)

if value >= 1000000:
     raise ValueError('not supported')

value1 = value // 1000
value0 = value % 1000

group1 = small_number(value1)
group0 = small_number(value0)

# insert thousand symbol before every digit in group1
group1 = CU_THOUSAND + CU_THOUSAND.join(group1)

return group1 + group0
```
