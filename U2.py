def filter_lt(predicate, lt):
    result = []
    for ele in lt:
        if predicate(ele):
            result.append(ele)
    return result


lt = ['Justin', 'caterpillar', 'openhome']
print(filter_lt(lambda ele: len(ele) > 6, lt))
print(filter_lt(lambda ele: 'i' in ele, lt))
