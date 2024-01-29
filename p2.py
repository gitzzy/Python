# s = 0
# for d in range(0,1000,10):
#     s=d
#     print(s)
# res = eval(input("Enter Your Exp : "))
# print(res)
import matplotlib.pyplot as plt

x= [5,8,2,7,9]
y = [10,3,8,9,4]
plt.plot(x,y)
plt.title('Graph')
plt.xlabel('X-Axis')
plt.ylabel('Y-label')
plt.show()