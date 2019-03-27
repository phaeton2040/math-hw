
# Не совсем понял задание. То же самое можно сделать и через numpy, но в задании этого не написано
# Поэтому реализую задание на чистом python
vector_1 = [1, 2, 3]
vector_2 = [4, 5, 6]


def vector_sum(v1, v2):
    result = []
    if len(v1) != len(v2):
        raise ValueError('Можно складывать векторы только одинаковой размерности')
    for i in range(len(v1)):
        result.append(v1[i] + v2[i])
    return result


print(vector_sum(vector_1, vector_2))

