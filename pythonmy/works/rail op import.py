# given the arrival and departure times of all trains that reach a railway station,the task is to find minimum number of platforms required for the railway station so that no train waits
#we are given 2 arrays that represent the arrival and depature times of trains that stop
#arr=[900,940,950,1100,1500,1800]
#dep=[910,1200,1120,1130,1900,2000]
def findplatform (arr,dep,n):
    plat_needed=1
    result=1
    for i in range(n):
        plat_needed =1
        for j in range(n):
            if i!=j:
                if (arr[i]>=arr[j] and dep[j]>=arr[i]):
                    plat_needed += 1
        result=max(result,plat_needed)
    return result
def main():
    arr=[900,940,950,1100,1500,1800]
    dep=[910,1200,1120,1130,1900,2000]

    n=len(arr)
    print("{}".format(
        findplatform(arr,dep,n)))
if __name__=='__main__' :
    main()

