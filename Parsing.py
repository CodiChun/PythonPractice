from re import A
import string

input = "date,process,host,log,bytes\n20200206,cme_trader_2,cme0001,0345-cme_trader_2.log.gz,15400000\n20200206,phlx_trader_1,phlx0001,0651-phlx_trader_1.log.gz,14100000\n20200206,phlx_trader_2,phlx0001,0645-phlx_trader_2.log.gz,13800000\n20200207,cme_trader_2,cme0001,0345-cme_trader_2.log.gz,15800000\n20200207,cme_trader_3,cme0001,0345-cme_trader_3.log.gz,14200000\n20200207,phlx_trader_1,phlx0001,0651-phlx_trader_1.log.gz,24100000"


def change_name(x: str) -> str:
    if x == "cme0001":
        
        return "cme"
    elif x == "phlx0001":
        return "phlx"

# Split the input to array
info = [x.split(',') for x in input.split('\n')]

# Store the data to dictionary
dic = dict()
for i in info:
    if(i[0] == 'date'):
        continue

    new_name = change_name(i[2])
    if not dic.__contains__(i[0]):
        dic[i[0]] = {new_name: i[4]}

    else:
        if dic.get(i[0], {}).__contains__(new_name):
            count = int(dic.get(i[0]).get(new_name))
        else:
            count = 0

        dic[i[0]][new_name] = int(i[4]) + count


print("data, exchange, total_bytes")
for x in dic.keys():
    for j, k in dic[x].items():
        print(x,',',j,',',k)
