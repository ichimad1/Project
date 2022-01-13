#1
x = ['Aug', 'Mar', 'May']
y = [67, 20, 22]
lists = zip (x, y)
new_dict = dict(lists)
print(new_dict)

#2
z = list(range(26, 29))
print(z)

#3
str1 = 'AB'
str2 = '34'
v = [x + y for x in str2 for y in str1]
print(v)

#4
int_list = [5, -2, -4, 6]
print(n for n in int_list if n < 0)
# Select the correct answer

#5
names = ['Thor Odinson', 'Steve Rogers']
avengers = list(enumerate(names, start = 3))
print(avengers)

#6
b = [2, 'L', 4, 'M', 'N', 6]
strings = [y for y in b if type(y) == str]
print(strings)

#7
f = [3, 2, 4, 6]
squares = {i: i ** 2 for i in f}
print(squares)

#8
floats = [9.87, 7.57, 3.19, 0.72]
intergers = [round(i) for i in floats]
print(intergers)

#9
#link_to_df =
#df_chunks = pd.read_csv(link_to_df, chunksize=5)
#print(next(df_chunks))

#10
teams = [['barry', 'cisco', 'caitlin'],
         ['oliver', 'john', 'felicity']]
print([member[0] for member in teams])

#11
scarlet_speedster = iter('Barry Allen')
print(*scarlet_speedster)

#12
a = range(0, 5)
print(list(a))
print(a)
print(sum(a))

#13
names = ['Natasha Romanoff', 'Clint Barton']
characters = ['Black Widow', 'Hawkeye']
names1 = ['Chris Hemsworth', 'Chris Evans']
characters1 = ['Thor Odinson','Steve Rogers']
avengers1 = zip(characters, names1)
a1, a2 = zip(*avengers1)
print(avengers1)

#14
k = '123'
print([y * 2 for y in k])
