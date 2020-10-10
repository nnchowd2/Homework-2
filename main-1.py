password = input()
new_pass = ""

for i in password:
   if i == 'i':
       new_pass += '!'

   elif i == 'a':
       new_pass += '@'

   elif i == 'm':
       new_pass += 'M'

   elif i == 'B':
       new_pass += '8'

   elif i == 'o':
       new_pass += '.'

   else:
       new_pass += i

print(new_pass + "q*s")
