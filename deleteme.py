# variable
number = 130
print(f"This is cs {number}")

# list
data = [1,4,6]
for item in data:
    print(item)

# input
age = int(input("What is your age?: "))
print(f"You are {age} years old.")

# for loop
for value in range(10):
    print(value)

#while loops
start = int(input("Where do you want to start?"))
end = int(input("Where do you want to end?"))
step = int(input("Where do you want to count by?"))

counter = start
while counter <= end:
    print(counter)
    counter += step

prompt = "yes"
while prompt != "no":
    prompt = input("Do you want to continue?")



# bool
answer = input("What is your gender?: ")
if answer == "boy":
    is_male = True
else:
    is_male = False

print("Male?", is_male)