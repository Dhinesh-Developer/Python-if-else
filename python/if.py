  # DK Online notes for some logical control statemnts

#if
balance = 5000
if balance >0:
    print("Your account balance is positive")


# if_else
balance = -100
if balance>=0:
    print("your account balance i postive")
else:
    print("your account balance is negative")

 # Nested if statements

balance = 1000
withdrawal_Amount = 1500
if balance>0:
       if withdrawal_Amount<=balance:
            print("withdrawal approved")
       else:
            print("Insufficient funds")
else:
     print("Account balance is negative")



#elif statements

account_type = "Savings"
if account_type == "checking":
     print("checking account selected")
elif account_type == "Selecting":
     print("selecting account selected")
elif account_type == "withdraw":
    print("withdraw account selected")
else:
     print("Account not found")


# loop statements  = for

account_numbers = [611223104034,611223104035,611223104040]
for number in account_numbers:
     print(f"Processing account number: {number}")

# while loop statements

correct_pin = 7777
attempt = 0
while attempt < 3:
     Enter_pin = int(input("Enter your Atm pin"))
     if Enter_pin == correct_pin:
          print("PIN Accepted")
     else:
          print("Enter the PIN once Again")
          attempt = attempt+1
if attempt ==3:
     print("oops...Wrong PIN , Account Locked")


# break statements    checking and exciting loop when sufficient balance is found

account_balance = [200,500,1000,1500]

for balance in account_balance:
     if balance >= 1000:
          print(f"Found sufficient balance: {balance}")
          break

#continue  statements    skip the account with balance below 500

account_balance = [200,500,1000,1500]
for balance in account_balance:
     if balance >=500:
          print("Processing account with: {balance}")
          continue

#Normal Functions
def check_Balance(account_number):
     account_balance = 
     {
          123456 = 1000,
          7697654 = 500,
          872906 = 1500
    }
     return account_balance.get(account_number,"Account not found")    
account_number = 123456
balance = check_Balance(account_number)
print(f"Balance checking {account_number} : ${balance}")


#factorial
def factorial(n):
     if n==0:
          return
     else:
          return n*factorial(n-1)


number = 5
result = factorial(number)
print(f"Factorial if {number} : {result}")