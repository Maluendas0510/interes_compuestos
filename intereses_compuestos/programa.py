# interes de los meses

print("--------------------")
print("-----intereses------")
print("--------------------")

#input
c=int(input("dijite el valor del capital:"))
b=2*c
n=0
#processing
while(c<b):
    c=c+0.05*c
    n=n+1
    
#fin
print("------resultado-----")
print("el interes compuesto:" +str(n))