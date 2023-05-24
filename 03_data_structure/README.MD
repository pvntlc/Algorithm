### Stack

- LIFO(Last In First Out) 방식
- 자료의 맨 끝 위치에서만 모든 연산이 이루어진다.
- 모든 연산에 대한 시간 복잡도는 O(1)이다.
- 연산이 이루어지는 위치를 top이라고 한다.
- 삽입은 push, 삭제는 pop.
- 파이썬은 따로 Stack 자료 구조를 제공하지 않으며, 이미 list에 모두 구현되어 있다.

### Stack in Python

stack = list()일 때

- stack.append(element)하면 top에 원소를 추가
- stack.pop()하면 top에 있는 원소 반환
- stack[-1]은 top에 있는 원소
- len(stack)은 스택 사이즈 및 top-1
- len(stack) == 0이면 스택이 비어있는지 확인하는 것.

### Queue

- FIFO(First In First Out) 방식
- 자료의 왼쪽 끝 위치에서 삭제, 오른쪽 끝 위치에서 삽입 연산.
- 모든 연산에 대한 시간 복잡도는 O(1)이다.
- 삭제가 이루어지는 위치를 front, 삽입이 이루어지는 위치를 rear라고 한다.
- 삭제는 dequeue, 삽입은 enqueue.

### Deque

- Double - Ended Queue
- 스택과 큐가 합쳐진 구조.
- 자료의 양 끝에서 연산이 이루어 진다.
- 모든 연산에 대한 시간 복잡도는 O(1)이다.

### Queue and Deque in Python

collection.deque를 활용한다.

- deq = collection.deque()
- appendleft() : 덱의 앞에 원소 추가
- append() : 덱의 뒤에 원소 추가
- popleft() : 덱의 앞에 원소 반환하고 삭제
- pop() : 덱의 뒤의 원소를 반호나하고 삭제
- deq[0] : 가장 앞에 있는 원소
- deq[-1] : 가장 뒤에 있는 원소 등
- queue.Queue가 따로 있지만 사용하지 않는 이유?
    - 스레드 프로그래밍을 위한 것으로 일반적으로 collections.deque보다 느리기 때문.