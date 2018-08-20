lt = ['Justin', 'caterpillar', 'openhome']
print(list(filter(lambda ele: len(ele) > 6, lt)))
print(list(filter(lambda ele: 'i' in ele, lt)))
print(list(map(lambda ele: ele.upper(), lt)))
print(list(map(lambda ele: len(ele), lt)))