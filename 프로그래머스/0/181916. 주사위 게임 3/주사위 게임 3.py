def solution(a, b, c, d):
    dice = sorted([a, b, c, d])
    if dice[0] == dice[-1]:
        return dice[0] * 1111
    if dice[0] != dice[1] == dice[2] == dice[3]:
        return (10 * dice[3] + dice[0]) ** 2
    if dice[0] == dice[1] == dice[2] != dice[3]:
        return (10 * dice[0] + dice[3]) ** 2
    if dice[0] == dice[1] != dice[2] == dice[3]:
        return (dice[2] - dice[1]) * (dice[2] + dice[1])
    if dice[0] == dice[1]:
        return dice[2]*dice[3]
    if dice[1] == dice[2]:
        return dice[0]*dice[3]
    if dice[2] == dice[3]:
        return dice[0]*dice[1]
    return dice[0]