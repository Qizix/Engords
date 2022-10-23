import test
import studing
import edit
pair = edit.read_base("base.txt")
main_text = '''Hi! This app will help you learn English words.
Now you can:

1. Learn words
2. Take the test
3. Close the program
'''
print(main_text)
ans = input()
if ans == "1":
    studing.teach(pair)
    studing.cls()
    print(main_text)
    input()
elif ans == "2":
    test.testt(pair, 3, 20)
    studing.cls()
    print(main_text)
    input()






