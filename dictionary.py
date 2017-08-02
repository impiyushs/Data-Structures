"""Time to play with Python dictionaries!
We're going to work on a dictionary that
stores cities by country and continent.

We need to add the cities listed below by
modifying the structure.
Then, should print out the values specified
by looking them up in the structure.

Cities to add:
Mountain View (USA, North America)
Bangalore (India, Asia)
Atlanta (USA, North America)
Cairo (Egypt, Africa)
Shanghai (China, Asia)"""

"""We will print the following (using "print").
1. A list of all cities in the USA in
alphabetic order.
2. All cities in Asia, in alphabetic
order, next to the name of the country.
In your output, label each answer with a number
so it looks like this:
1
American City
American City
2
Asian City - Country
Asian City - Country"""

locations = {'North America': {'USA': ['Mountain View']}}
locations['Asia']= {'India':['Bangalore'], 'China': ['Shanghai']}
locations['North America']['USA'].append('Atlanta')
locations['Africa']={'Egypt':['Cairo']}

us_cities= sorted(locations['North America']['USA'])
print 1
for i in us_cities:
    print i

asian_cities= sorted(locations['Asia'])
print 2

asia=[]
for country, city in locations['Asia'].iteritems():
    temp=city[0] + ' - ' + country
    asia.append(temp)
asian_cities=sorted(asia)
for i in asian_cities:
    print i
