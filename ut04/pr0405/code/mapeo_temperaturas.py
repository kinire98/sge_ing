import random
temp_cel = []
for i in range(50):
    temp_cel.append(random.randint(-20, 50))
temp_far = list(
        map(
            lambda x: round(x * (9/5) + 32, 3),
            temp_cel
            )
        )
print(temp_cel)
print(temp_far)
