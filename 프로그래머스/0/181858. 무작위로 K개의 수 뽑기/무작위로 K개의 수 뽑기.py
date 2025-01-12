def solution(arr, k):
    answer = []
    idx = 0
    while len(answer) < k and idx < len(arr):
        if arr[idx] not in answer:
            answer.append(arr[idx])
        idx += 1
            
    return answer + [-1]*(k - len(answer))