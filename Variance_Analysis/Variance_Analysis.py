fisher005=[]
fisher005.append([161.4476,199.5000,215.7073,224.5832,230.1619,233.9860,236.7684,238.8827,240.5433,241.8817])
fisher005.append([18.5128,19.0000,19.1643,19.2468,19.2964,19.3295,19.3532,19.3710,19.3848,19.3959])
fisher005.append([10.1280,9.5521,9.2766,9.1172,9.0135,8.9406,8.8867,8.8452,8.8123,8.7855])
fisher005.append([7.7086,6.9443,6.5914,6.3882,6.2561,6.1631,6.0942,6.0410,5.9988,5.9644])
fisher005.append([6.6079,5.7861,5.4095,5.1922,5.0503,4.9503,4.8759,4.8183,4.7725,4.7351])
fisher005.append([5.9874,5.1433,4.7571,4.5337,4.3874,4.2839,4.2067,4.1468,4.0990,4.0600])
fisher005.append([5.5914,4.7374,4.3468,4.1203,3.9715,3.8660,3.7870,3.7257,3.6767,3.6365])
fisher005.append([5.3177,4.4590,4.0662,3.8379,3.6875,3.5806,3.5005,3.4381,3.3881,3.3472])
fisher005.append([5.1174,4.2565,3.8625,3.6331,3.4817,3.3738,3.2927,3.2296,3.1789,3.1373])
fisher005.append([4.9646,4.1028,3.7083,3.4780,3.3258,3.2172,3.1355,3.0717,3.0204,2.9782])
fisher001=[]
fisher001.append([4052.181,4999.500,5403.352,5624.583,5763.650,5858.986,5928.356,5981.070,6022.473,6055.847])
fisher001.append([98.503,99.000,99.166,99.249,99.299,99.333,99.356,99.374,99.388,99.399])
fisher001.append([34.116,30.817,29.457,28.710,28.237,27.911,27.672,27.489,27.345,27.229])
fisher001.append([21.198,18.000,16.694,15.977,15.522,15.207,14.976,14.799,14.659,14.546])
fisher001.append([16.258,13.274,12.060,11.392,10.967,10.672,10.456,10.289,10.158,10.051])
fisher001.append([13.745,10.925,9.780,9.148,8.746,8.466,8.260,8.102,7.976,7.874])
fisher001.append([12.246,9.547,8.451,7.847,7.460,7.191,6.993,6.840,6.719,6.620])
fisher001.append([11.259,8.649,7.591,7.006,6.632,6.371,6.178,6.029,5.911,5.814])
fisher001.append([10.561,8.022,6.992,6.422,6.057,5.802,5.613,5.467,5.351,5.257])
fisher001.append([10.044,7.559,6.552,5.994,5.636,5.386,5.200,5.057,4.942,4.849])
def CreateTable(q, p):
    Table=[]
    for i in range (0, q):
        tmp=[]
        for j in range (0, p):
            tmp.append(int(input("Enter an element in "+str(j+1)+" column and "+str(i+1)+" row")))
        Table.append(tmp)
    return Table
def CalculateGroupMean(table):
    mean=[]
    for j in range(0, len(table[0])):
        tmp=0
        for i in range(0, len(table)):
            tmp+=table[i][j]
        mean.append(tmp/len(table))
    return mean
def ArithmMean(list):
    sum=0
    for i in range (0, len(list)):
        sum+=list[i]
    return sum/len(list)
def MainSum(tab):
    tabmean=ArithmMean(CalculateGroupMean(tab))
    sum=0
    for i in range (0, len(tab)):
        for j in range (0, len(tab[0])):
            sum+=pow(tab[i][j]-tabmean, 2)
    return sum
def FactSum(tab):
    means=CalculateGroupMean(tab)
    arith=ArithmMean(means)
    sum=0
    for i in range (0, len(means)):
        sum+=pow(means[i]-arith, 2)
    return sum*len(tab)
def RemSum(tab):
    return MainSum(tab)-FactSum(tab)
def FactVariance(tab):
    return FactSum(tab)/(len(tab[0])-1)
def RemVariance(tab):
    return RemSum(tab)/(len(tab[0])*(len(tab)-1))
def FisherTest(alpha, tab):
    currentFisher=FactVariance(tab)/RemVariance(tab)
    if (alpha=="0.05"):
        tablevalue=fisher005[len(tab)][len(tab[0])]
    elif (alpha=="0.01"):
        tablevalue=fisher001[len(tab)][len(tab[0])]
    if (currentFisher<tablevalue):
        return True
    return False
def Console():
    while (1):
        q=int(input("Enter q "))
        p=int(input("Enter p "))
        Table=CreateTable(q, p)
        quan=input("Enter quantile ")
        print(MainSum(Table))
        print(FactSum(Table))
        print(RemSum(Table))
        print(FactVariance(Table))
        print(RemVariance(Table))
        print(FisherTest(quan, Table))
Console()