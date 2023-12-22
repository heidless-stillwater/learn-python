
lucky_numbers = [15, 7, 12, 30, 1]
friends = ['arjuna', 'Heidless', 'Heidless', 'heidless', 'havana', 'Kevin']

# basec
print(friends)

print('# examples')
print(friends[1])
print(friends[1:3])
print(friends[:2])
print(friends[-1])

friends[0] = 'Toby'
print(friends)

print(lucky_numbers)

# extend
print('# extend')
#friends_0 = friends
#friends_0.extend(lucky_numbers)
#print(friends_0)

# append
print('# append')
print(friends)
friends_1 = friends
friends_1.append(lucky_numbers[2])
print(friends_1)
print(friends)

# insert
print('# insert')
friends.insert(2, "Kelly")
print(friends)

# remove
print('# remove')
friends.remove("Kelly")
print(friends)

# pop - remove last element
print('# pop')
friends.pop()
print(friends)

# index
print('# index')
print(friends.index('Kevin'))

# count
print('# count')
print(friends.count('heidless'))

# sort
print('# sort')
print(friends)
friends.sort()
print(friends)

print('--')
print(lucky_numbers)
lucky_numbers.reverse()
print(lucky_numbers)

print('--')
print(lucky_numbers)
lucky_numbers.sort(reverse=True)
print(lucky_numbers)

# copy
print('# copy')
print(friends)
friends2 = friends.copy()
print(friends2)