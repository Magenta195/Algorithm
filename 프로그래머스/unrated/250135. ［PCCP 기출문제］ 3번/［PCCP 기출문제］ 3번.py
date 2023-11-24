def solution(h1, m1, s1, h2, m2, s2):
    start = h1 * 3600 + m1 * 60 + s1
    end = h2 * 3600 + m2 * 60 + s2
    
    ## 1 + x / 43200 = x / 60
    ## x = 43200 / 719
    h_interval = 43200 / 719
    ## 1 + x / 3600 = x / 60
    ## x = 3600 / 59
    m_interval = 3600 / 59
    
    h_list, m_list = list(), list()
    
    result = 0
    
    t = 0
    while t <= end + 1e-5 :
        if start - 1e-5 <= t :
            print(t)
            result += 1
        t += h_interval

    t = 0
    while t <= end + 1e-5 :
        if start - 1e-5 <= t :
            result += 1
        t += m_interval
        
    if start == 0 :
        result -= 1
    if start <= 43200 <= end :
        result -= 1
    
    return result