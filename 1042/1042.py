values = list(map(lambda x: int(x),input().split()))
values_backup = values[:]

def order_from_smallest_to_largest(values):
    for i in range(len(values)):
        for j in range(len(values)):
            if values[i] < values[j]:
                previous_value_on_j_position = values[j]
                values[j] = values[i]
                values[i] = previous_value_on_j_position

    return values

values = order_from_smallest_to_largest(values)

for i in range(len(values)):
    print(f"{values[i]}", end="\n")

print()

for i in range(len(values_backup)):
    print(f"{values_backup[i]}", end="\n")
    