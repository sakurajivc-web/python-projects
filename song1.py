import time

print('...')
time.sleep(8)
print()

part_1 = [
('So', 0.3), ('what', 0.3), ('if', 0.2), ('I', 0.25), ('call?', 3.3)
]
part_2 = [
('And', 0.3), ('you', 0.3), ('pick', 0.4), ('up', 0.3), ('the', 0.3), ('phone?', 3.4) 
]
part_3 = [
('And', 0.4), ('I', 0.3), ('use', 0.3), ('this', 0.35), ('holiday', 1.4)
]
part_4 = [
('To', 0.3), ('make', 0.45), ('my', 0.4), ('way', 0.35), ('to', 0.4), ('your', 0.25), ('ghost', 0.4)
]
for word, delay in part_1:
    print(word, end=" ", flush=True)

    time.sleep(delay)
 
print()   
for word, delay in part_2:
    print(word, end=" ", flush=True)

    time.sleep(delay)
print()    
for word, delay in part_3:
    print(word, end=" ", flush=True)

    time.sleep(delay)
print()    
for word, delay in part_4:
    print(word, end=" ", flush=True)

    time.sleep(delay)