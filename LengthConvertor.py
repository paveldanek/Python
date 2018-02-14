Units=('mm','cm','m','km','in','ft','yd','mi')
Conversions=(10,100,1000,0.0000254,12,3,1760)

inp1='100'
inp2='100'

print("Length convertor")
while str.isdigit(inp1)==False or (int(inp1)<1 or int(inp1)>len(Units)):
    for k in range(len(Units)):
        print("'",k+1,"'=from ",Units[k]," ",sep="",end="")
    print()
    inp1=input("> ")
inp1=int(inp1)
while str.isdigit(inp2)==False or (int(inp2)<1 or int(inp2)>len(Units)):
    for k in range(len(Units)):
        print("'",k+1,"'= to  ",Units[k]," ",sep="",end="")
    print()
    inp2=input("> ")
inp2=int(inp2)
number=float(input("The value being converted: "))
result=number
                   
if inp1<inp2:
    for k in range(inp1-1,inp2-1):
        result=result/Conversions[k]
if inp1>inp2:
    for k in range(inp1-1,inp2-1,-1):
        result=result*Conversions[k-1]

print(number,Units[inp1-1],"=",format(result,'.6f'),Units[inp2-1],sep="")
