def solution(numbers, hand):
    answer = ''
    left_pos='*'
    right_pos='#'
    maps={1:{'x':0, 'y':0},
         2: {'x':0, 'y':1},
         3: {'x':0, 'y':2},
         4: {'x':1, 'y':0},
         5: {'x':1, 'y':1},
         6: {'x':1, 'y':2},
         7: {'x':2, 'y':0},
          8:{'x':2, 'y':1},
          9:{'x':2, 'y':2},
          '*':{'x':3, 'y':0},
          0:{'x':3, 'y':1},
          '#':{'x':3, 'y':2}
    }
    
    onlyLeft=[1,4,7]
    onlyRight=[3,6,9]
    for number in numbers:
        if number in onlyLeft:
            answer+='L'
            #왼손의 현재위치를 변경
            left_pos=number
            
        elif number in onlyRight:
            answer+='R'
            right_pos=number
            
        else:# 2,5,8,0
            left_distance=abs(maps[left_pos]['x']-maps[number]['x'])+abs(maps[left_pos]['y']-maps[number]['y'])
            right_distance=abs(maps[right_pos]['x']-maps[number]['x'])+abs(maps[right_pos]['y']-maps[number]['y'])
            
            #거리가 같다면-> 무슨손잡이냐에 따라 결정
            if left_distance==right_distance:
                if hand=='left':
                    answer+='L'
                    left_pos=number
                else:
                    answer+='R'
                    right_pos=number
                
            #거리가 다르다면
            elif left_distance>right_distance:
                answer+='R'
                right_pos=number
            else:
                answer+='L'
                left_pos=number
                
    return answer
