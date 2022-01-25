# 데이터 구조(Data Structure)

[문자열(String)](#문자열string)

[리스트(List)](#리스트list)

[튜플(Tuple)](#튜플tuple)

[셋(Set)](#셋set)

[딕셔너리(Dictionary)](#딕셔너리dictionary)

[얕은 복사와 깊은 복사](#얕은-복사와-깊은-복사)

## 순서가 있는 데이터 구조

### 문자열(String)

- immutable: 변경 불가능이므로, 변경된 값을 따로 반환한다.

- 문자열 조회/탐색

  ```python
  s.find(x)		# x의 첫 번째 위치 반환, 없으면 -1 반환
  s.index(x)		# x의 첫 번째 위치 반환, 없으면 오류 발생
  				# 만약 모든 위치를 알고 싶다면 반복문 써야함
  ```

- 문자열 검증 메서드

  ```python
  s.isalpha()		# 숫자가 아닌 글자인가?
  s.isspace()		# 공백으로 이루어져 있는가?
  s.isupper()		# 대문자 여부
  s.islower()		# 소문자 여부
  s.istitle()		# 타이틀 형식 여부 (모든 단어 앞글자가 대문자)
  s.startwith(x)	# 문자열이 x로 시작하면 True 아니면 False
  s.endswith(x)	# 문자열이 x로 끝나면 True 아니면 False
  ```

- 숫자 관련 검증 메서드

  ```python
  .isdecimal() ⊆ .isdigit() ⊆ .isnumeric()
  
  s.isdecimal()	# 0~9까지 수인가?
  s.isdigit()		# 문자열이 숫자로 이루어져 있는가?
  s.isnumeric()	# 문자열을 수로 볼 수 있는가?
  ```

- 문자열 변경 메서드

  ```python
  s.replace(old, new[, count])	# 바꿀 대상 글자를 새로운 글자로 바꿔서 반환
  s.replace(old, new, count=1)	# count는 해당 개수만큼 시행 (선택)
  
  s.strip([chars])				# 공백이나 특정 문자 제거
  s.lstrip() / s.rstrip()			# 왼쪽 / 오른쪽 공백 제거
  
  s.split(sep=None, maxsplit=-1)	# 공백이나 특정 문자기준으로 분리
  								# sep = None인 경우 연속된 공백을 단일 공백으로 간주
      							# maxsplit = -1인 경우 제한 없음
          
  'seperator'.join([iterable])	# 구분자'seperator'로 iterable 합침
  								# 문자열만 가능. int는 불가능하다.
  
  s.capitalize()					# 첫글자를 대문자로, 나머지는 소문자로
  s.title							# ' 혹은 공백 이후를 대문자로
  s.upper()						# 모두 대문자로
  s.lower()						# 모두 소문자로
  s.swapcase						# 대소문자 변경
  ```

  

### 리스트(List)

- mutable: 리스트 자체가 바뀌는 경우가 많다.

- 리스트 메소드

  ```python
  L.append(x)					# 마지막에 x 추가
  L.insert(i, x)				# 인덱스 i에 x 추가, i가 길이보다 크면 맨 뒤에 추가
  							# i = -1이면 맨 끝이 아니라 맨 끝 바로 앞에 추가
      						# 인덱스 앞에 추가하는 구조인듯 하다.
  L.extend(iterable)			# iterable의 각 항목을 추가
  
  L.remove(x)					# 첫 번째 x 제거. 항목이 없으면 ValueError
  L.pop()						# 가장 오른쪽 반환 후 제거
  L.pop(i)					# 인덱스 i 항목 반환 후 제거
  L.clear()					# 모두 제거
  
  L.index(x, start, end)		# 항목 중 가장 처음 x 인덱스 반환
  							# 값이 없으면 ValueError
  L.reverse()					# 원본을 거꾸로 뒤집기
  L.sort(...)					# 리스트를 정렬. list 원본을 바꿈. a.sort()
  							# sorted(list): 원본은 그대로. 반환값이 정렬. a = sorted(a)
  L.count(x)					# x가 리스트에 몇 개인지 반환
  ```
  
  

### 튜플(Tuple)

- immutable: 리스트 메소드 중 항목을 변경하는 메소드를 제외하고 사용 가능

- 튜플 메서드

  ```python
  (1, 2) + (3, 4) = (1, 2, 3, 4)	# 튜플끼리 더하기 가능
  								# 튜플 내부끼리 더해지지는 않는다.
  ```

  

## 순서가 없는 데이터 구조

### 셋(Set)

- mutable

- 셋 메서드

  ```python
  s.copy()				# 셋의 얕은 복사본 반환
  s.update(iterable)		# iterable에 있는 모든 항목 중 s에 없는 항목 추가
  
  s.add(x)				# x가 s에 없다면 추가
  
  s.pop()					# s에서 랜덤하게 항목 반환하고 제거
  						# s가 비어있을 경우 KeyError
  s.remove(x)				# x를 s에서 제거
  						# x가 s에 없으면 KeyError
  s.discard(x)			# x가 s에 있으면 제거
  						# x가 s에 없어도 에러 발생 없음
  s.clear()				# 모두 삭제
  
  s.isdisjoint(t)			# s와 t의 교집합이 없으면 True
  s.issubset(t)			# s가 t의 하위 집합이면 True
  s.issuperset(t)			# s가 t의 상위 집합이면 True
  ```

  

### 딕셔너리(Dictionary)

- mutable

- 딕셔너리 메서드

  ```python
  d.copy()				# 얕은 복사본 반환
  d.update(...)			# ...이 d에 없거나 수정되면 업데이트
  d.update(a = 'b')		# d = {'a': 'a'} -> {'a': 'b'}
  						# keyword 인자처럼 ''안써도 됨
  
  d.keys()				# 모든 키를 담은 뷰를 반환
  d.values()				# 모든 값을 담은 뷰를 반환
  d.items()				# 모든 키-값 쌍을 반환
  
  d.get(k)				# 키 k의 값을 반환, 없으면 None반환
  d.get(k, v)				# 키 k의 값을 반환, 없으면 v 반환
  d.setdefault(k,v)		# 키 k의 값을 반환, 없으면 v 반환, k-v를 d에 추가
  
  d.pop(k)				# 키 k의 값을 반환, 키 k의 항목 삭제, k가 없으면 KeyError
  d.pop(k, v)				# 키 k의 값을 반환, 키 k의 항목 삭제, k가 없으면 v 반환
  d.clear()				# 모두 삭제
  ```



## 얕은 복사와 깊은 복사

### 복사방법

- 할당 (Assignment)
- 얕은 복사 (Shallow copy)
- 깊은 복사 (Deep copy)

### 할당

- `=`을 사용하면 mutable 객체의 경우 주소를 참조한다.

  ```python
  original_list = [1, 2, 3]
  copy_list = original_list
  copy_list[0] = 4
  
  print(original_list)
  # [4, 2, 3]
  ```

### 얕은 복사(Shallow Copy)

- `[:]` 슬라이싱을 통해 복사하고 다른 주소를 얻음

- `list(original_list)`: list 함수의 반환값

- original_list 내부에 또 다른 주소를 참조하는 객체가 포함되는 경우 오리지널이 바뀔 수 있음

  ```python
  a = [1, 2, ['a', 'b']]
  b = a[:]
  b[2][0] = 0
  print(a)
  # [1, 2, [0, 'b']]
  ```

  

### 깊은 복사(Deep Copy)

```python
import copy
b = copy.deepcopy(a)
```