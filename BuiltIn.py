#1. abs function : used to remove negative sign ffrom any number
a = -10
print(a)
print('Use of ABS : ',abs(a))

#2. Filter Function : used to filter the elements from the list
x = (1,2,3,4,5,6,7,8,9)
odd  = list(filter(lambda y:y%2==1,x))
print(odd)

#3. Map function : it is used to applies to changes to all the items in list.
sqr = list(map(lambda y:y*y,x))
print(sqr)

#4. len function : used to return the lenght of the data
name =  'Devansh'
print('Len Function : ',len(name))

#5. List function : create the list from iterable
print(list(name))

#6. Max and Min : used to return the maximum and minimum element from an iterbale.
print('Max function : ',max(x))
print('Min function : ',min(x))

#7. pow function
print('Pow function : ',pow(2,10))

#8. Sum function : it is used to return the sum of iterables.
print(sum(x))


