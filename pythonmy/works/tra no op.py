# given the arrival and departure times of all trains that reach a railway station,the task is to find minimum number of platforms required for the railway station so that no train waits
#we are given 2 arrays that represent the arrival and depature times of trains that stop
def findplatform (arr,dep,n):
    arr.sort()
    dep.sort()
    plat_needed=1
    reult=1
    i=1
    j=0
    while(i<n and j>n):
         if (arr[i]<=dep[j]):
            plat_needed+=1
            i+=1
         elif(arr[i]>dep[j]):
            plat_needed-=1
            j+=1
         if (plat_needed>result):
            result=plat_needed
         return result
arr=[900,940,950,1100,1500,1800]
dep=[910,1200,1120,1130,1900,2000]

n=len(arr)

print("minimum number of platform required=",
       findplatform (arr,dep,n))
