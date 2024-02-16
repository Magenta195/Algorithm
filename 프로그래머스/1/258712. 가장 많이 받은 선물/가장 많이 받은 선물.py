def solution(friends, gifts):
    length = len(friends)
    gift_map = [[0]*length for _ in range(length)]
    gift_score = [0]*length
    
    for gift in gifts :
        sender, receiver = gift.split()
        sender, receiver = friends.index(sender), friends.index(receiver)
        gift_score[sender] += 1
        gift_score[receiver] -= 1
        gift_map[sender][receiver] += 1
        
    result = [0]*length
    for i in range(length-1) :
        for j in range(i+1, length) :
            if gift_map[i][j] > gift_map[j][i] :
                result[i] += 1
            elif gift_map[i][j] < gift_map[j][i] :
                result[j] += 1
            elif gift_score[i] > gift_score[j] :
                result[i] += 1
            elif gift_score[i] < gift_score[j] :
                result[j] += 1
    
    return max(result)