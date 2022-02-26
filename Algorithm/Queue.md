## Queue

> - 삽입과 삭제의 위치가 제한적인 구조
> - 큐의 뒤에서는 삽입, 앞에서는 삭제
> - FIFO (First-In-First-Out). 선입선출
> - 앞을 Front-머리, 뒤를 Rear-꼬리로 부른다.
> - 삽입: enQueue, 삭제: deQueue



### Queue 연산 과정

1. createQueue()
   - front = rear = -1
2. enQueue(A)
   - front = -1, rear = 0 (A)
3. enQueue(B)
   - front = -1, rear = 1 (B)
4. deQueue()
   - front = 0, rear = 1