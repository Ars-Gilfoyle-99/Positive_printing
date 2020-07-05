n=input("Enter the size of your list");
n=int(n);
input_list=[None]*n;
i=0;
while i<n:
    t=input();
    input_list[i]=int(t);
    i+=1;
print(input_list);
for num in input_list:
    if num>0:
        print(num);

        
    
