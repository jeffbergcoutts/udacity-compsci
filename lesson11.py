'''
How to Manage Data
'''
# Quiz: Stooges
stooges = ['Moe', 'Larry', 'Curly']

# Quiz: Days in a Month
days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]
def how_many_days(month):
    return days_in_month[month - 1]

print how_many_days(2)
print how_many_days(9)

# Quiz: Countries

countries = [['China','Beijing',1350],
             ['India','Delhi',1210],
             ['Romania','Bucharest',21],
             ['United States','Washington',307]]

print countries[1][1]

# Quiz: Relative Size

print countries[0][2]/countries[2][2]

# Quiz: Different Stooges

stooges = ['Moe','Larry','Curly']
stooges[2] = 'Shemp'
print stooges

# Yello Mutation
'''
Lists are mutatable. Changing the value of a list 
effect any variable with that list. eg:
'''
p = ['H', 'E', 'L', 'L', 'O']
q = p
p[0] = 'Y'
print p, q

# known as aliasing
spy = [0,0,7]
agent = spy
print spy, agent
print agent[2]
spy[2] = agent[2] + 1
print agent[2]
