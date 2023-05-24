하나의 그래프에서 트리를 만들 수 있는 방법은 다양하다. 그 중에서 간선의 가중치 합이 가장 작은 트리는 어떻게 구할 수 있을까?

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/433b3982-ebd3-4a12-9b1f-d7dd32ced82a/Untitled.png)

다음과 같은 그래프에서 트리를 만들 수 있는 방법으로는 두 가지가 있다.

## Minimum Spanning Tree

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a56d1a22-653b-416b-850e-cd6f4f44cdf5/Untitled.png)

- 하나의 그래프에서 만들 수 있는 트리들을 신장트리라고 함.
- 신장 트리 중 간선의 가중치 합이 가장 작은 트리를 **최소신장트리**라고 함.
- MST를 구하는 알고리즘으로 **크루스칼, 프림 알고리즘**이 있다.

### Kruskal 알고리즘

- 유니온 파인드 알고리즘을 이용해 MST를 구한다.
- 유니온 파인드에서 같은 집합은 사이클이 발생한다는 점을 이용한다.
- 가중치가 가장 작은 간선부터 선택하며, 사이클이 발생하지 않는다면 트리에 포함한다.
- 유니온 파인드의 시간 복잡도가 O(1)에 가깝기 때문에 간선을 정렬하는 시간 복잡도만 고려한다.
- 간선이 많지 않을 때 주로 사용되며 간선의 수를 E라고 할 때 시간 복잡도는 O(ElogE)이다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/3bb8fcf1-c038-4902-8f5e-a6ef4af85987/Untitled.png)

1. 가장 가중치가 낮은 3-5부터 선택 후 진행.

|  | 3-5 | 6-8 | 5-7 | 3-4 | 1-2 | 6-7 | 7-8 | 2-3 | 2-4 | 4-6 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Weight | 1 | 3 | 3 | 4 | 4 | 5 | 7 | 9 | 9 | 14 |
|  |  |  |  |  |  |  |  |  |  |  |
|  | 1번 | 2번 | 3번 | 4번 | 5번 | 6번 | 7번 | 8번 |  |  |
| Parent | -1 | -1 | -2 | -1 | 3 | -1 | -1 | -1 |  |  |
1. 다음으로 가중치가 낮은 6-8 선택 후 진행.

|  | 3-5 | 6-8 | 5-7 | 3-4 | 1-2 | 6-7 | 7-8 | 2-3 | 2-4 | 4-6 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Weight | 1 | 3 | 3 | 4 | 4 | 5 | 7 | 9 | 9 | 14 |
|  |  |  |  |  |  |  |  |  |  |  |
|  | 1번 | 2번 | 3번 | 4번 | 5번 | 6번 | 7번 | 8번 |  |  |
| Parent | -1 | -1 | -2 | -1 | 3 | -2 | -1 | 6 |  |  |
1. 이런식으로 반복해서 진행하다가 7-8간선을 선택할 때 같은 parent를 가지고 있는 노드끼리 연결하게 되는데, 이 때 break를 해준다.

|  | 3-5 | 6-8 | 5-7 | 3-4 | 1-2 | 6-7 | 7-8 | 2-3 | 2-4 | 4-6 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Weight | 1 | 3 | 3 | 4 | 4 | 5 | 7 | 9 | 9 | 14 |
|  |  |  |  |  |  |  |  |  |  |  |
|  | 1번 | 2번 | 3번 | 4번 | 5번 | 6번 | 7번 | 8번 |  |  |
| Parent | -2 | 1 | -6 | 3 | 3 | 3 | 3 | 3 |  |  |

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/0d60c09f-a7b1-4a02-be71-a951d18b7c79/Untitled.png)

최종 모형은 다음과 같이 완성된다.

### Kruskal 알고리즘 예제 / 1197번 : 최소 스패닝 트리 - Gold 4

그래프가 주어졌을 때, 그 그래프의 최소 스패닝 트리를 구하는 프로그램을 작성하시오.

**입력**

첫째 줄에 정점의 개수 V(1 ≤ V ≤ 10,000)와 간선의 개수 E(1 ≤ E ≤ 100,000)가 주어진다. 다음 E개의 줄에는 각 간선에 대한 정보를 나타내는 세 정수 A, B, C가 주어진다. 이는 A번 정점과 B번 정점이 가중치 C인 간선으로 연결되어 있다는 의미이다. C는 음수일 수도 있으며, 절댓값이 1,000,000을 넘지 않는다.

그래프의 정점은 1번부터 V번까지 번호가 매겨져 있고, 임의의 두 정점 사이에 경로가 있다. 최소 스패닝 트리의 가중치가 -2,147,483,648보다 크거나 같고, 2,147,483,647보다 작거나 같은 데이터만 입력으로 주어진다.

**출력**

첫째 줄에 최소 스패닝 트리의 가중치를 출력한다.

**예제 입력 1**

```
3 3
1 2 1
2 3 2
1 3 3

```

**예제 출력 1**

```
3
```

### 해결 코드

```python
#1197번 : 최소 스패닝 트리 - Gold 4
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
"""

"""

def find_parent(x):
    if parent[x] < 0:
        return x
    parent[x] = find_parent(parent[x])
    return parent[x]

def union(x,y):
    px = find_parent(x)
    py = find_parent(y)

    if px == py:
        return True

    if parent[px] < parent[py]:
        parent[px] += parent[py]
        parent[py] = px
    else:
        parent[py] += parent[px]
        parent[px] = py
    return False

v,e = map(int, input().split())
parent = [-1] * (v+1)
n_list = []
for _ in range(e):
    n_list.append(list(map(int, input().split())))

n_list.sort(key = lambda x : x[2])
count = 0
for s,e,weight in n_list:
    if union(s,e):
        continue
    count += weight
print(count)
```

말 그대로 유니온 파인드를 사용해서 푸는 문제였다. 다만, 가중치가 뒤에 나오기 때문에 람다식을 이용해서 정렬하는 것이 좋다. x[2]만 정렬할 수 있도록 지정하고, 나머지는 상관없이 정렬한다. 그래야 시간 절약할 수 있음.

---

### Prim 알고리즘

- 특정 정점에서 시작하여 접근할 수 있는 정점 중 가중치가 가장 작은 정점을 우선으로 접근한다.
- 시작점으로부터의 누적 거리를 고려한 다익스트라와는 달리 간선 자체의 가중치만 고려한다.
- 시작점이 특별하게 주어진 경우에 주로 사용한다.
- 시간 복잡도는 O(VlogV + ElogV)이다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/e249640c-32ca-41b2-9b24-b50b00edbf6e/Untitled.png)

1. 1번부터 시작한다고 고려. 

| 1번 | 2번 | 3번 | 4번 | 5번 | 6번 | 7번 | 8번 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | INF | INF | INF | INF | INF | INF | INF |
1. 1번에서 가장 짧은 간선은 2번 노드로 가는 간선이므로 이를 선택.

| 1번 | 2번 | 3번 | 4번 | 5번 | 6번 | 7번 | 8번 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 4 | INF | INF | INF | INF | INF | INF |
1. 2번에서 갈 수 있는 간선은 3과 4로 가는 간선이고, 둘 다 갱신.

| 1번 | 2번 | 3번 | 4번 | 5번 | 6번 | 7번 | 8번 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 4 | 9 | 9 | INF | INF | INF | INF |
1. 3번에서 가장 짧은 간선인 5로 가는 것 선택 후 4로 가는 것도 선택. 왜냐면 기존에 있는 9보다 4가 더 작기 때문에.

| 1번 | 2번 | 3번 | 4번 | 5번 | 6번 | 7번 | 8번 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 4 | 9 | 4 | 1 | INF | INF | INF |
1. 5번에서 갈 수 있는 간선이 7로 가는 것 하나 뿐이므로 갱신 후 선택

| 1번 | 2번 | 3번 | 4번 | 5번 | 6번 | 7번 | 8번 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 4 | 9 | 4 | 1 | INF | 3 | INF |
1. 7번에서 갈 수 있는 간선이 6,8 두 개 있으므로 갱신 후 가장 짧은 4번 선택.

| 1번 | 2번 | 3번 | 4번 | 5번 | 6번 | 7번 | 8번 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 4 | 9 | 4 | 1 | 5 | 3 | 7 |
1. 6번에서 갈 수 있는 간선이 4,8 두 개 있으므로 갱신 후 가장 짧은 6번 선택.

| 1번 | 2번 | 3번 | 4번 | 5번 | 6번 | 7번 | 8번 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 4 | 9 | 4 | 1 | 5 | 3 | 7 |

8, 마지막으로 남아있는 8번 선택하고 난 결과물은 다음과 같다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/9c45e61f-f476-49d6-b4fe-281a5511267f/Untitled.png)

### 프림 알고리즘과 다익스트라 알고리즘의 차이점은?

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/165ae87f-b70f-4970-b0a3-1f7943f0bf00/Untitled.png)

1,2,3번 노드가 다음과 같이 이어져 있다면 각 알고리즘의 DIST 배열은 다음과 같다.

- 프림 알고리즘의 DIST 배열
    
    
    | 1번 | 2번 | 3번 |
    | --- | --- | --- |
    | 0 | 9 | 4 |
- 다익스트라 알고리즘의 DIST 배열
    
    
    | 1번 | 2번 | 3번 |
    | --- | --- | --- |
    | 0 | 9 | 13 |

다익스트라는 시작점부터의 거리를 기록하기 때문에 거리가 누적되지만, 프림은 선택된 간선의 거리만 사용한다. 

이 때문에 다익스트라는 DIST 배열에 저장된 값과의 비교를 통해서 재방문을 방지하지만, 프림은 visited배열을 사용하여 재방문을 방지해야 한다.

## 그래서 어떤 알고리즘을 사용해야 하는 거지?

- 크루스칼 시간 복잡도 = O(ElogE)
- 프림 시간 복잡도 = O(VlogV + ElogV)
- 크루스칼 알고리즘의 연산 횟수에 영향을 주는 요소는 오직 간선의 수이며, 프림 알고리즘 연산에 영향을 주는 요소는 정점의 수이다.
- 때문에 간선이 많거나 특정 시작 정점이 주어진다면 = 프림
- 간선이 적거나 특정 시작 정점이 없다면 = 크루스칼 사용한다.
- 다만…. 개인 취향의 영역에 가깝다..

---

## 최종 정리!

- 그래프에서 만들 수 있는 모든 트리를 신장 트리라고 한다.
- 그 중 간선의 가중치 총 합이 가장 작은 트리를 최소 신장 트리(MST)라고 한다.
- MST를 구하는 알고리즘으로는 크루스칼, 프림이 있다.
- 크루스칼은 유니온 파인드 알고리즘을 활용하고, 프림은 다익스트라와 유사하다.
- 간선이 적다면 크루스칼, 간선이 많거나 시작점이 주어지면 프림으로 풀기!
## 최소신장트리 예제

### 4386번 : 별자리 만들기 - Gold 3(크루스칼 방식으로 해결)

도현이는 우주의 신이다. 이제 도현이는 아무렇게나 널브러져 있는 n개의 별들을 이어서 별자리를 하나 만들 것이다. 별자리의 조건은 다음과 같다.

- 별자리를 이루는 선은 서로 다른 두 별을 일직선으로 이은 형태이다.
- 모든 별들은 별자리 위의 선을 통해 서로 직/간접적으로 이어져 있어야 한다.

별들이 2차원 평면 위에 놓여 있다. 선을 하나 이을 때마다 두 별 사이의 거리만큼의 비용이 든다고 할 때, 별자리를 만드는 최소 비용을 구하시오.

**입력**

첫째 줄에 별의 개수 n이 주어진다. (1 ≤ n ≤ 100)

둘째 줄부터 n개의 줄에 걸쳐 각 별의 x, y좌표가 실수 형태로 주어지며, 최대 소수점 둘째자리까지 주어진다. 좌표는 1000을 넘지 않는 양의 실수이다.

**출력**

첫째 줄에 정답을 출력한다. 절대/상대 오차는 10-2까지 허용한다.

**예제 입력 1**

```
3
1.0 1.0
2.0 2.0
2.0 4.0

```

**예제 출력 1**

```
3.41
```

### 해결 코드

```python
#4386번 : 별자리 만들기 - Gold 3
import math
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
"""

"""

def find_parent(x):
    if parent[x] < 0:
        return x
    parent[x] = find_parent(parent[x])
    return parent[x]

def union(x,y):
    px = find_parent(x)
    py = find_parent(y)

    if px == py:
        return True

    if parent[px] < parent[py]:
        parent[px] += parent[py]
        parent[py] = px
    else:
        parent[py] += parent[px]
        parent[px] = py
    return False

n = int(input())
n_list = []
answer = []
parent = [-1] * (n)

for _ in range(n):
    x, y = map(float, input().split())
    n_list.append([x,y])

for i in range(n):
    for j in range(n):
        if i==j:
            continue
        x1, y1 = n_list[i]
				x2, y2 = n_list[j]
        weight = math.sqrt((x1 - x2)**2 + (y1-y2)**2)
        answer.append([i,j,weight])

answer.sort(key=lambda x : x[2])

count = 0
for s,e,weight in answer:
    if union(s,e):
        continue
    count += weight

print(round(count,2))
```

---

### 10423번 : 전기가 부족해 – Gold 2

 N개의 도시가 있고 M개의 두 도시를 연결하는 케이블의 정보와 K개의 YNY발전소가 설치된 도시가 주어지면 케이블 설치 비용을 최소로 사용하여 모든 도시에 전기가 공급할 수 있도록 해결해야 한다. 중요한 점은 어느 한 도시가 두 개의 발전소에서 전기를 공급받으면 낭비가 되므로 케이블이 연결되어있는 도시에는 발전소가 반드시 하나만 존재해야 한다. 아래 Figure 1를 보자. 9개의 도시와 3 개의 YNY발전소(A,B,I)가 있고, 각각의 도시들을 연결할 때 드는 비용이 주어진다.

!https://www.acmicpc.net/upload/images2/E1.png

Figure 1

!https://www.acmicpc.net/upload/images2/E2.png

Figure 2

이 예제에서 모든 도시에 전기를 공급하기 위하여 설치할 케이블의 최소 비용은 22이고, Figure 2의 굵은 간선이 연결한 케이블이다. B 도시는 연결된 도시가 하나도 없지만, 발전소가 설치된 도시는 전기가 공급될 수 있기 때문에 상관없다.

**입력**

첫째 줄에는 도시의 개수 N(1 ≤ N ≤ 1,000)과 설치 가능한 케이블의 수 M(1 ≤ M ≤ 100,000)개, 발전소의 개수 K(1 ≤ K ≤ N)개가 주어진다. 둘째 줄에는 발전소가 설치된 도시의 번호가 주어진다. 셋째 줄부터 M개의 두 도시를 연결하는 케이블의 정보가 u, v, w로 주어진다. 이는 u도시와 v도시를 연결하는 케이블을 설치할 때 w의 비용이 드는 것을 의미한다. w는 10,000보다 작거나 같은 양의 정수이다.

**출력**

모든 도시에 전기를 공급할 수 있도록 케이블을 설치하는 데 드는 최소비용을 출력한다.

**예제 입력 1**

```
9 14 3
1 2 9
1 3 3
1 4 8
2 4 10
3 4 11
3 5 6
4 5 4
4 6 10
5 6 5
5 7 4
6 7 7
6 8 4
7 8 5
7 9 2
8 9 5

```

**예제 출력 1**

```
22

```

**예제 입력 2**

```
4 5 1
1
1 2 5
1 3 5
1 4 5
2 3 10
3 4 10

```

**예제 출력 2**

```
15

```

**예제 입력 3**

```
10 9 5
1 4 6 9 10
1 2 3
2 3 8
3 4 5
4 5 1
5 6 2
6 7 6
7 8 3
8 9 4
9 10 1

```

**예제 출력 3**

```
16
```

### 해결 코드

기존에 했었던 최소신장트리에서 달라진 것은 루트 노드의 개수가 따로 주어진다는 것이다. 즉, 지금까지는 하나의 집합으로 진행했지만, 이번 문제는 K개의 집합으로 유니온-파인드를 진행해야 하는 것이다. 이러한 경우에는 k개의 집합으로 나누면 어렵기 때문에 임의의 0번 노드를 생성하여 발전소(루트)를 모두 0번에 연결시켜 버리는 것이다. 그러면 손쉽게 해결할 수 있다.

```python
#10423번 : 전기가 부족해 – Gold 2
import math
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
"""

"""

def find_parent(x):
    if parent[x] < 0:
        return x
    parent[x] = find_parent(parent[x])
    return parent[x]

def union(x,y):
    px = find_parent(x)
    py = find_parent(y)

    if px == py:
        return True

    if parent[px] < parent[py]:
        parent[px] += parent[py]
        parent[py] = px
    else:
        parent[py] += parent[px]
        parent[px] = py
    return False

def kruskal(n, edge):
    cost = 0
    cnt = 0
    for u, v, w in edge:
        if union(u, v):
            continue
        cost += w
        cnt += 1

        if cnt == n - 1:
            return cost

    return 0

n, m, k = map(int, input().split())
k_list = list(map(int, input().split()))
parent = [-1] * (n+1)
parent[0] = -k

for i in k_list:
    parent[i] = 0

n_list = [list(map(int, input().split())) for _ in range(m)]
n_list.sort(key=lambda x : x[2])
print(kruskal(n - k + 1, n_list))
```

---

### 1774번 : 우주신과의 교감 – Gold 3

황선자씨는 우주신과 교감을 할수 있는 채널러 이다. 하지만 우주신은 하나만 있는 것이 아니기때문에 황선자 씨는 매번 여럿의 우주신과 교감하느라 힘이 든다. 이러던 와중에 새로운 우주신들이 황선자씨를 이용하게 되었다.

하지만 위대한 우주신들은 바로 황선자씨와 연결될 필요가 없다. 이미 황선자씨와 혹은 이미 우주신끼리 교감할 수 있는 우주신들이 있기 때문에 새로운 우주신들은 그 우주신들을 거쳐서 황선자 씨와 교감을 할 수 있다.

우주신들과의 교감은 우주신들과 황선자씨 혹은 우주신들 끼리 이어진 정신적인 통로를 통해 이루어 진다. 하지만 우주신들과 교감하는 것은 힘든 일이기 때문에 황선자씨는 이런 통로들이 긴 것을 좋아하지 않는다. 왜냐하면 통로들이 길 수록 더 힘이 들기 때문이다.

또한 우리들은 3차원 좌표계로 나타낼 수 있는 세상에 살고 있지만 우주신들과 황선자씨는 2차원 좌표계로 나타낼 수 있는 세상에 살고 있다. 통로들의 길이는 2차원 좌표계상의 거리와 같다.

이미 황선자씨와 연결된, 혹은 우주신들과 연결된 통로들이 존재한다. 우리는 황선자 씨를 도와 아직 연결이 되지 않은 우주신들을 연결해 드려야 한다. 새로 만들어야 할 정신적인 통로의 길이들이 합이 최소가 되게 통로를 만들어 “빵상”을 외칠수 있게 도와주자.

**입력**

첫째 줄에 우주신들의 개수(N<=1,000) 이미 연결된 신들과의 통로의 개수(M<=1,000)가 주어진다.

두 번째 줄부터 N개의 줄에는 황선자를 포함하여 우주신들의 좌표가 (0<= X<=1,000,000), (0<=Y<=1,000,000)가 주어진다. 그 밑으로 M개의 줄에는 이미 연결된 통로가 주어진다. 번호는 위의 입력받은 좌표들의 순서라고 생각하면 된다. 좌표는 정수이다.

**출력**

첫째 줄에 만들어야 할 최소의 통로 길이를 출력하라. 출력은 소수점 둘째짜리까지 출력하여라.

**예제 입력 1**

```
4 1
1 1
3 1
2 3
4 3
1 4

```

**예제 출력 1**

```
4.00
```

### 해결 코드

```python
import sys
input = sys.stdin.readline

"""
[우주신과의 교감]

4386번 : 별자리 만들기의 응용 문제
 이미 연결된 정점들이 존재한다는 것을 제외하고는 4386번과 동일

 1. 임의의 두 별에 대한 거리(간선) 모두 구하기
 2. 이미 존재하는 통로들 표시
    !주의! 통로의 개수가 m개라면 v-m-1개의 간선만 더 추가하면 될까?
          이미 연결된 통로들도 사이클을 이룰 수 있기 때문에 유니온 연산을 하며 사이클 없이 연결된 간선만 세기
 3. 이미 연결된 통로의 수를 k개라고 하면 v-k-1개의 간선을 추가로 선택
"""

# find 연산
def find_parent(x):
    if parent[x] < 0:
        return x
    
    parent[x] = find_parent(parent[x])
    return parent[x]

# union 연산
def union(x, y):
    px = find_parent(x)
    py = find_parent(y)

    if px == py:
        return False
    
    if parent[px] < parent[py]:
        parent[px] += parent[py]
        parent[py] = px
    else:
        parent[py] += parent[px]
        parent[px] = py

    return True

def kruskal(n, edge):
    cost = 0
    cnt = 0
    for u, v, w in edge:
        if not union(u, v):
            continue
        
        cost += w
        cnt += 1

        if cnt == n-1:
            return cost

    return 0

# 입력
n, m = map(int, input().split())
position = [tuple(map(int, input().split())) for _ in range(n)]
edge = []

for i in range(n):
    for j in range(i):
        dx = position[i][0] - position[j][0]
        dy = position[i][1] - position[j][1]

        edge.append((i, j, (dx**2 + dy**2)**(1/2)))

# 초기화
parent = [-1]*(n)

cnt = 0

for _ in range(m):
    u, v = map(int, input().split())
    # 이미 연결한 통로
    if union(u-1, v-1):
        cnt += 1

edge.sort(key=lambda x:x[2])  # 정렬

# 연산 & 출력
print("%.2f" %(kruskal(n - cnt, edge)))
```

---

### 1368번 : 물대기 – Gold 2 *** 다시 풀어보기!

선주는 자신이 운영하는 N개의 논에 물을 대려고 한다. 물을 대는 방법은 두 가지가 있는데 하나는 직접 논에 우물을 파는 것이고 다른 하나는 이미 물을 대고 있는 다른 논으로부터 물을 끌어오는 법이다.

각각의 논에 대해 우물을 파는 비용과 논들 사이에 물을 끌어오는 비용들이 주어졌을 때 최소의 비용으로 모든 논에 물을 대는 것이 문제이다.

**입력**

첫 줄에는 논의 수 N(1 ≤ N ≤ 300)이 주어진다. 다음 N개의 줄에는 i번째 논에 우물을 팔 때 드는 비용 Wi(1 ≤ Wi ≤ 100,000)가 순서대로 들어온다. 다음 N개의 줄에 대해서는 각 줄에 N개의 수가 들어오는데 이는 i번째 논과 j번째 논을 연결하는데 드는 비용 Pi,j(1 ≤ Pi,j ≤ 100,000, Pi,j = Pj,i, Pi,i = 0)를 의미한다.

**출력**

첫 줄에 모든 논에 물을 대는데 필요한 최소비용을 출력한다.

**예제 입력 1**

```
4
5
4
4
3
0 2 2 2
2 0 3 3
2 3 0 4
2 3 4 0

```

**예제 출력 1**

```
9
```

### 해결코드

우물을 파는 경우를 고려하면서 간선도 고려하는 것은 굉장히 복잡하기 때문에 논 배열에 추가로 모든 우물과 연결되는 수원이 있다고 가정한다! 

0 2 2 2 5
2 0 3 3 4
2 3 0 4 4
2 3 4 0 3
5 4 4 3 0

즉 이러한 배열이 만들어지는 것이고, 인덱스 0부터 n-1까지는 논이고, 인덱스 n은 수원이라고 보면 된다. 결국 수원에서부터 시작하는 최소 신장트리를 찾는 알고리즘이므로, 프림 알고리즘을 사용하면 적절하다고 판단된다.

```python
#1368번 : 물대기 - Gold 2
import sys
import heapq as hq
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
INF = 10**5 + 1
"""

"""
def prim(size, start, graph):
    total = 0
    pq = []
    visited = [False] * size
    dist = [INF] * size

    dist[start] = 0
    hq.heappush(pq, (0,start))

    while pq:
        cost, curr = hq.heappop(pq)

        if visited[curr]:
            continue

        visited[curr] = True
        total += cost

        for i in range(size):
            if not visited[i] and graph[curr][i] < dist[i]:
                dist[i] = graph[curr][i]
                hq.heappush(pq, (graph[curr][i], i))
    return total

n = int(input())
cost = [int(input()) for _ in range(n)]

# 논들 사이에서 물을 끌어오는 비용
graph = [list(map(int, input().split())) for _ in range(n)]

# 수원지로부터 물을 끌어오는 비용
graph.append(cost + [0])
for i in range(n):
    graph[i].append(cost[i])

# 연산 & 출력
print(prim(n+1, n, graph))
```

---

### 1647번 : 도시 분할 계획 – Gold 4

동물원에서 막 탈출한 원숭이 한 마리가 세상구경을 하고 있다. 그러다가 평화로운 마을에 가게 되었는데, 그곳에서는 알 수 없는 일이 벌어지고 있었다.

마을은 N개의 집과 그 집들을 연결하는 M개의 길로 이루어져 있다. 길은 어느 방향으로든지 다닐 수 있는 편리한 길이다. 그리고 각 길마다 길을 유지하는데 드는 유지비가 있다.

마을의 이장은 마을을 두 개의 분리된 마을로 분할할 계획을 가지고 있다. 마을이 너무 커서 혼자서는 관리할 수 없기 때문이다. 마을을 분할할 때는 각 분리된 마을 안에 집들이 서로 연결되도록 분할해야 한다. 각 분리된 마을 안에 있는 임의의 두 집 사이에 경로가 항상 존재해야 한다는 뜻이다. 마을에는 집이 하나 이상 있어야 한다.

그렇게 마을의 이장은 계획을 세우다가 마을 안에 길이 너무 많다는 생각을 하게 되었다. 일단 분리된 두 마을 사이에 있는 길들은 필요가 없으므로 없앨 수 있다. 그리고 각 분리된 마을 안에서도 임의의 두 집 사이에 경로가 항상 존재하게 하면서 길을 더 없앨 수 있다. 마을의 이장은 위 조건을 만족하도록 길들을 모두 없애고 나머지 길의 유지비의 합을 최소로 하고 싶다. 이것을 구하는 프로그램을 작성하시오.

**입력**

첫째 줄에 집의 개수 N, 길의 개수 M이 주어진다. N은 2이상 100,000이하인 정수이고, M은 1이상 1,000,000이하인 정수이다. 그 다음 줄부터 M줄에 걸쳐 길의 정보가 A B C 세 개의 정수로 주어지는데 A번 집과 B번 집을 연결하는 길의 유지비가 C (1 ≤ C ≤ 1,000)라는 뜻이다.

**출력**

첫째 줄에 없애고 남은 길 유지비의 합의 최솟값을 출력한다.

**예제 입력 1**

```
7 12
1 2 3
1 3 2
3 2 1
2 5 2
3 4 4
7 3 6
5 1 5
1 6 2
6 4 1
6 5 3
4 5 3
6 7 4

```

**예제 출력 1**

```
8
```

### 해결코드

최소신장트리로 만들어서 n개를 연결한 후, 마지막에 끊게 되면 결국 트리 하나와 노드 하나만 남게 되기 때문에 n-1개만 연결한다고 생각하면 된다.

```python
#1647번 : 도시분할계획 - Gold 4
import sys
import heapq as hq
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
INF = 10**5 + 1
"""

"""
def find_parent(x):
    if parent[x] < 0 :
        return x
    parent[x] = find_parent(parent[x])
    return parent[x]

def union(x,y):
    px = find_parent(x)
    py = find_parent(y)

    if px == py:
        return True
    if parent[px] > parent[py]:
        parent[py] += parent[px]
        parent[px] = py
    else:
        parent[px] += parent[py]
        parent[py] = px
    return False

def kruskal(n,n_list):
    total = 0
    count = 0
    for x,y,weight in n_list:
        if union(x,y):
            continue
        total += weight
        count += 1
        if count == n-1:
            return total
    return 0
n,m = map(int, input().split())
parent = [-1] * (n+1)
n_list = [tuple(map(int, input().split())) for _ in range(m)]
n_list.sort(key = lambda x: x[2])
print(kruskal(n-1,n_list))
```