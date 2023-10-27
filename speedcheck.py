import time
a=input("Enter the testing input:")
b=time.time()
test=input("Enter the testing input:")
c=time.time()
minutes =(c-b)/60
wpm = int(len(test)/ minutes)
print("%.2f wpm" %wpm)
mistake=0
for i in range(len(a)):
    try:
        if a[i]!=test[i]:
            mistake+=1
    except:
        mistake=mistake+len(a)-i
        break

print("Accuracy: "+str(int(100-(mistake/len(a)*100)))+"%")