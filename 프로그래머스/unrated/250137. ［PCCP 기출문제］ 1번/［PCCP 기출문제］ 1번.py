def solution(bandage, health, attacks):
    prev = 0
    cur_health = health
    for cur, power in attacks :
        x, y = (cur - prev - 1)*bandage[1] , ((cur - prev - 1) // bandage[0]) * bandage[2]
        cur_health = min(health, cur_health + x + y)
        cur_health -= power
        prev = cur
        if cur_health <= 0 :
            return -1
    return cur_health