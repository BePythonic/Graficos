from matplotlib import pyplot as plt 
from collections import Counter as count

'''years = [1950,1960,1970,1980,1990,2000,2010]
gdp = [300.2,543.3,1075.9,2862.5,5979.6,10289.7,14958.3]
plt.title("GDP Nominal") 
plt.ylabel("Billions of $")
plt.xlabel("Ano")

plt.show()'''

'''------------------------------------------------------------------------------------------------------'''

'''movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
num_oscars =[5,11,3,8,10]

xs = [i+0.1 for i,_ in enumerate(movies)]

plt.bar(xs,num_oscars)

plt.title("Meus Filmes Favoritos")
plt.xlabel("Filmes")
plt.ylabel("de Premiacoes")

plt.xticks([i+0.1 for i,_ in enumerate(movies)], movies)

plt.show()'''
'''--------------------------------------------------------------------------------------'''

'''lista = ["maca","pera","goiaba"]
for _,j in enumerate(lista):
	print(j)

for i,_ in enumerate(lista):
	print(i)

for i,j in enumerate(lista):
	print(i,j)'''

grades = [83,95,91,87,70,0,85,82,100,67,73,77,0]
decile = lambda grade: (grade//10)*10
grades_dec = [decile(grade) for grade in grades]

histogram = count(grades_dec)

plt.bar(([x for x in histogram.keys()]),histogram.values(),8)
plt.axis([-5,105,0,5])

plt.xticks([10*i for i in range(11)])
plt.xlabel("Decile")
plt.ylabel("# of Students")
plt.title("Distribution of Exam")
plt.show()