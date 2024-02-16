def solution(coin, cards):
    answer = 0
    hand = set()
    left = set()
    
    left_matched = 0
    half_matched = 0
    matched = 0
    N = len(cards)
    
    for card in cards[:N//3] :
        if N+1-card in hand :
            matched += 1
            hand.discard(N+1-card)
        else :
            hand.add(card)
    
    round = 1
    for i in range(N//3, N, 2) :
        for card in cards[i:i+2] : 
            if N+1-card in hand :
                half_matched += 1
                hand.discard(N+1-card)
            elif N+1-card in left :
                left_matched += 1
                left.discard(N+1-card)
            else :
                left.add(card)
            
        if matched :
            matched -= 1
        elif coin > 0 and half_matched :
            half_matched -= 1
            coin -= 1
        elif coin > 1 and left_matched :
            left_matched -= 1
            coin -= 2
        else :
            break
        round += 1
            
    return round