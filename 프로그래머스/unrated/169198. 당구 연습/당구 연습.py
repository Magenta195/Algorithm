rx = list()
ry = list()

get_dist = lambda x, y, _x, _y : (x - _x) ** 2 + (y - _y) ** 2

def wall_move(m, n, x, y, ballX, ballY) :
    result = float('inf')
    for cX, _ballX in [(0, -ballX), (m, m*2 - ballX)] :
        if y != ballY or get_dist(x, y, cX, y) < get_dist(_ballX, y, cX, y) :
            result = min(result, get_dist(x, y, _ballX, ballY))
    for cY, _ballY in [(0, -ballY), (n, n*2 - ballY)] :
        if x != ballX or get_dist(x, y, x, cY) < get_dist(x, _ballY, x, cY) :
            result = min(result, get_dist(x, y, ballX, _ballY))
        
    return result

def corner_move(m, n, x, y, ballX, ballY) :
    result = float('inf')
    for cX, _ballX in [(0, -ballX), (m, m*2 - ballX)] :
        for cY, _ballY in [(0, -ballY), (n, n*2 - ballY)] :
            if x*(_ballY) == y*(_ballX) and get_dist(x, y, cX, cY) < get_dist(_ballX, _ballY, cX, cY) :
                result = min(result, get_dist(x, y, _ballX, _ballY))
    
    return result

def solution(m, n, startX, startY, balls):
    answer = []
    
    for ballX, ballY in balls :
        result1 = wall_move(m, n, startX, startY, ballX, ballY)
        result2 = corner_move(m, n, startX, startY, ballX, ballY)
        answer.append(min(result1, result2))
    return answer