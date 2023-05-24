## 트리

- 비선형 자료 구조 중 하나.
- 그래프의 부분집합으로 계층 관계를 나타낼 때 주로 사용된다.
- 사이클이 없고, V개의 정점에 대해서 V-1개의 간선이 있다.
- 부모-자식의 계층 구조이다.
- 트리 탐색의 시간 복잡도는 O(h)이다.
- 그래프와 마찬가지로 DFS, BFS 등을 이용하여 탐색한다.

### 트리 용어

- Root : 부모 정점이 없는 정점, 일반적으로 1번 정점을 의미한다.
- Subtree : 트리의 부분 집합
- Leaf node : 자식 정점이 없는 정점
- Level : 트리의 각 계층
- Height : Level 중에서 가장 큰 값

### 트리의 종류

- Binary Tree(이진트리) : 자식 정점의 수가 2개 이하.
- General Tree(일반 트리) : 자식 정점의 수에 제한 없음.

### 트리 구현 의사 코드

```cpp
int main(){
	map<int, pair<int, int>> tree;
	tree[1] = {2,3};
	tree[2] = {-1, -1};
	tree[3] = {-1, -1};
}
```

## 이진 트리 순회

```
			 3
		 /   \
		6	 	  7
	 / \   /
	5	 4	1

다음과 같은 트리가 있다.
```

### 레벨 순회

```python
level(root)
{
	while(!q.empty())
		v = q.front();
		q.pop();
		if (v == null)
			continue;
		q.push(left(v))
		q.push(right(v))
}
```

탐색 순서 : 3→6→7→5→4→1

### 전위 순회

```python
preorder(v)
{
	if (v != null)
		print(v)
		preorder(left(v))
		preorder(right(v))
}
root > left > right
```

탐색 순서 : 3→6→5→4→7→1

### 중위 순회

```python
inorder(v)
{
	if (v != null)
		inorder(left(v))
		print(v)
		inorder(right(v))
}
left > root > right
```

탐색 순서 : 5→6→4→3→1→7

### 후위 순회

```python
postorder(v)
{
	if (v != null)
		postorder(left(v))
		postorder(right(v))
		print(v)
}
left > right > root
```

탐색 순서 : 5→4→6→1→7→3