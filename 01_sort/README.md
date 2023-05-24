# 1. 정렬

배열의 원소를 정렬하는 방법에는 여러 가지가 있다.

대표적으로 시간복잡도 O(n^2)을 가지는 정렬인 삽입 정렬, 선택 정렬, 버블 정렬이 있다.

또한 시간복잡도 O(nlogn)을 가지는 퀵 정렬, 합병 정렬, 힙 정렬이 있다.

버블 정렬은 인접한 두 원소를 비교해서 왼쪽 원소가 오른쪽 원소보다 크면 바꾸는 형식으로, 가장 큰 원소가 오른쪽에 정렬되는 형식이다.

### 삽입 정렬

- 자료 배열의 모든 요소를 앞에서부터 차례대로 이미 정렬된 배열 부분과 비교해서 자신의 위치를 찾아 삽입하는 정렬.
- 최악, 평균 시간복잡도는 n제곱이며, 최선은 n이다.
- 공간 복잡도는 n이다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c8347d15-2fd4-4d51-97b8-63693d2f5593/Untitled.png)

```python
def insert_sort(x):
	for i in range(1, len(x)):
		j = i - 1
		key = x[i]
		while x[j] > key and j >= 0:
			x[j+1] = x[j]
			j = j - 1
		x[j+1] = key
	return x
```

### 선택 정렬

- 주어진 리스트 중에서 최소 값을 찾는다.
- 그 값을 맨 앞에 위치한 값과 교체한다.
- 맨 처음 위치를 뺀 나머지 리스트를 같은 방법으로 교체한다.
- 최악, 최선, 평균 시간복잡도는 모두 n제곱이며, 공간복잡도는 1이다.
    
    ![Selection-Sort-Animation.gif](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ba2be34c-06e2-44d5-b45d-7b258208db7e/Selection-Sort-Animation.gif)
    

```python
def selection_sort(x):
	length = len(x)
	for i in range(length-1):
	    indexMin = i
		for j in range(i+1, length):
			if x[indexMin] > x[j]:
				indexMin = j
		x[i], x[indexMin] = x[indexMin], x[i]
	return x
```

### 퀵 정렬

- 리스트 가운데서 하나의 원소를 고른다. 이 원소를 피봇이라고 한다.
- 피봇 앞에는 피봇보다 작은 원소들이 오고, 피봇 뒤에는 큰 원소들이 오도록 리스트를 둘로 나눈다.
- 분할된 두 개의 작은 리스트에 대해서 재귀적으로 이 과정을 반복한다.
- 최선과 평균 시간 복잡도는 nlogn,  최악은 n제곱이다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ef795999-e47e-44e3-ac3a-eb28458e8a87/Untitled.png)

```python
def quick_sort(x):
    if len(x) <= 1:
        return x

    pivot = x[len(x) // 2]
    less = []
    more = []
    equal = []
    for a in x:
        if a < pivot:
            less.append(a)
        elif a > pivot:
            more.append(a)
        else:
            equal.append(a)

    return quicksort(less) + equal + quicksort(more)
```

### 합병 정렬

- 리스트의 길이가 1 이하이면 이미 정렬된 것으로 본다.
- 정렬되지 않은 리스트를 절반으로 잘라서 비슷한 크기의 리스트로 나눈다.
- 각 부분의 리스트를 재귀적으로 합병 정렬을 이용해 정렬한다.
- 두 부분 리스트를 다시 하나의 정렬된 리스트로 합병한다.
- 최악과 최선, 평균 모두 다 nlogn이다.
- 공간 복잡도는 n이다.

![Merge-sort-example-300px.gif](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ebe072c2-509b-41ea-b401-afd81f0bb9ee/Merge-sort-example-300px.gif)

```python
def merge_sort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])

    merged_arr = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    return merged_arr
```

### 힙 정렬

- n개의 노드에 대한 완전 이진 트리를 구성한다.
- 최대 힙을 구성한다. 최대 힙이란, 부모 노드가 자식 노드보다 큰 트리를 의미한다.
- 가장 큰 수를 가장 작은 수와 교환한다.
- 2와 3을 반복한다.
- 최악, 최선, 평균 시간 복잡도 모두 nlogn이다.
- 공간복잡도는 1이다.

![Heapsort-example.gif](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/86c2be1e-69d9-49cd-8a1c-e1533f1d4d43/Heapsort-example.gif)

```python
def heapify(unsorted, index, heap_size):
  largest = index
  left = 2 * index + 1
  right = 2 * index + 2
  
  if left < heap_size and unsorted[right] > unsorted[largest]:
    largest = left
    
  if right < heap_size and unsorted[right] > unsorted[largest]:
    largest = right
    
  if largest != index:
    unsorted[largest], unsorted[index] = unsorted[index], unsorted[largest]
    heapify(unsorted, largest, heap_size)

def heap_sort(unsorted):
  n = len(unsorted)
  
  for i in range(n // 2 - 1, -1, -1):
    heapify(unsorted, i, n)
    
  for i in range(n - 1, 0, -1):
    unsorted[0], unsorted[i] = unsorted[i], unsorted[0]
    heapify(unsorted, 0, i)

  return unsorted
```

- 힙정렬은 우선순위큐로도 구현이 가능하다.

### 퀵 vs 합병 vs 힙? 누가 더 뛰어난가?

- 우선 최선의 경우 시간복잡도가 n, 최악의 경우에는 nlogn에다가 추가 메모리도 들지 않는 힙 정렬이 가장 성능이 좋지 않을까라고 생각할 수도 있다.
- 그러나 평균 시간 복잡도가 nlogn이라는 의미를 좀 더 자세히 살펴볼 필요가 있다.
- 시간복잡도가 nlogn이라는 말은 실제 동작시간은 다음과 같다는 의미이다.
    
    $$
    C × nlogn + a
    $$
    
    - 상대적으로 무시할 수 있는 알파 부분을 제외하면 앞에 C라는 상수가 곱해져 있기 대문에 이 값에 따라 **실제 동작시간에 큰 차이**가 생긴다.
    - C라는 값에 큰 영향을 끼치는 요소는 알고리즘이 **참조 지역성 원리를 얼마나 잘 만족하는지**가 있다.
- 참조 지역성 원리 : CPU가 미래에 원하는 데이터를 예측하여 속도가 빠른 장치인 캐시 메모리에 담아 놓는데 이때의 예측률을 높이기 위해 사용하는 원리이다. **최근에 참조한 메모리나 그 메모리와 인접한 메모리를 다시 참조할 확률이 높다**는 이론을 기반으로 하고 있다.
- **힙 정렬**의 경우는 대표적으로 참조 지역성이 좋지 않은 정렬이다. 한 위치에 있는 요소를 해당 요소의 인덱스 두 배 또는 절반인 요소와 반복적으로 비교하기 때문에 캐시 메모리에서는 예측하기가 매우 어렵다.
- **합병 정렬**은 인접한 덩어리를 병합하기 때문에 참조 지역성의 원리를 어느 정도는 잘 만족한다. 그러나 입력 배열의 크기 만큼의 메모리를 추가로 사용한다는 단점이 있다.
- **퀵 정렬**은 피봇 주변에서 데이터의 위치 이동이 빈번하게 발생하기 때문에 참조 지역성이 좋고, 메모리를 추가로 사용하지 않는다. 그러나 피봇을 선정하는 방법에 따라 최악의 경우 시간 복잡도가 n^2이 되는 단점이 있다.
- 위와 같이 모든 정렬 알고리즘에는 장단점이 있기 때문에 한 정렬을 선택할 수 없었고 추가 메모리를 사용하지 않으면서 최악의 경우에도 속도가 빠른 [Tim sort](https://www.notion.so/dd7e4457570547e68b10cf397a80ebf2)가 등장하게 되었다.

### Python의 sort()함수?

- default값은 오름차순 정렬이다.
- key값에 람다 함수를 보내주면 원하는 조건대로 정렬이 가능
    - list.sort(key = lambda x: (x[0], -x[1]))
    - 리스트의 0번째 값은 오름차순, 1번째 값은 내림차순으로 정렬하라는 뜻.
- 내림차순 정렬은 reverse=True를 사용하면 정렬할 수 있다.
- sort()함수는 **Timsort** 알고리즘을 사용한다.

### Timsort?

- 최선은 n, 평균과 최악의 시간 복잡도는 nlogn인 정렬방법.
- 삽입 정렬과 합병 정렬을 결합했기에 안정적이며, 추가 메모리는 사용하지만 기존 합병 정렬보다는 적은 메모리를 사용하므로, nlogn의 정렬 알고리즘 단점을 최대한 극복한 알고리즘이다.
- 왜 삽입 정렬과 합병 정렬을 합쳤을까?
    - 삽입 정렬은 인접한 메모리와의 비교를 반복하기에 참조 지역성의 원리를 잘 만족하고 있다.
    - 또한 작은 n에 대하여 삽입 정렬이 퀵 정렬보다 더 빠르다.
- 이것을 이용하여 전체를 작은 덩어리로 잘라서 각 덩어리는 삽입정렬로 하되, 병합하는 것은 합병정렬을 사용하는 것이다.

### 마무리!

- 정렬 알고리즘은 종류가 많지만, 궁극적으로 활용하는 것은 sort함수이다.
- 정렬 알고리즘은 그리디 문제에서 사용될 수 있다.

---


## 참고 문헌

1. [https://ko.wikipedia.org/wiki/삽입_정렬](https://ko.wikipedia.org/wiki/%EC%82%BD%EC%9E%85_%EC%A0%95%EB%A0%AC)
2. [https://ko.wikipedia.org/wiki/선택_정렬](https://ko.wikipedia.org/wiki/%EC%84%A0%ED%83%9D_%EC%A0%95%EB%A0%AC)
3. [https://ko.wikipedia.org/wiki/퀵_정렬](https://ko.wikipedia.org/wiki/%ED%80%B5_%EC%A0%95%EB%A0%AC)
4. [https://ko.wikipedia.org/wiki/합병_정렬](https://ko.wikipedia.org/wiki/%ED%95%A9%EB%B3%91_%EC%A0%95%EB%A0%AC)
5. [https://ko.wikipedia.org/wiki/힙_정렬](https://ko.wikipedia.org/wiki/%ED%9E%99_%EC%A0%95%EB%A0%AC)
6. [https://www.daleseo.com/sort-insertion/](https://www.daleseo.com/sort-insertion/)
7. [https://good-potato.tistory.com/m/50](https://good-potato.tistory.com/m/50)
8. [https://d2.naver.com/helloworld/0315536](https://d2.naver.com/helloworld/0315536)
9. [https://realpython.com/sorting-algorithms-python/#the-timsort-algorithm-in-python](https://realpython.com/sorting-algorithms-python/#the-timsort-algorithm-in-python)
10. [https://velog.io/@piopiop/백준-13334-철로파이썬](https://velog.io/@piopiop/%EB%B0%B1%EC%A4%80-13334-%EC%B2%A0%EB%A1%9C%ED%8C%8C%EC%9D%B4%EC%8D%AC)
