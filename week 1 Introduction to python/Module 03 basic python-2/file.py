#. csv comma separeted value
# .txt text File

# with open('massage.txt', 'w') as file:
#     file.wr('I love python')
# with open('massage.txt', 'a') as file:
#     file.write('I love python')
with open('massage.txt', 'r') as file:
    text = file.read()
    print(text)