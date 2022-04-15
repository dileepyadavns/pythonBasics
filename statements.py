
st = 'Print only the words that start with s in this sentence'
for i in st.split():
    if i[0]=='s':
        print(i)

for i in range(0,10):
    if i%2==0:
        print(i)

myli=[x for x in range(1,50) if x%3==0]
print(myli)

st = 'Print every word in this sentence that has an even number of letters'
for i in st.split():
    if len(i)%2==0:
        print('even!')
        
for i in range(1,100):
    if (i%3==0) and (i%5==0):
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    elif  i%3==0: 
        print("FizzBuzz")

string=[i[0] for i in st.split()]
print(string)
