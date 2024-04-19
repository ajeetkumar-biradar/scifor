# :A teacher told students to write an essay on themselves. Nidhi created a python program that can generate an essay just by taking inputs. She shared the program with her friends to help them. Write a python program that can take inputs like name, age, address, etc, and convert it into an essay. ● Rakshita wants to create a simple chatbot using python language. Write a program in python to help Rakshita in creating the chatbot. ● Hint: with the help of variables store the answers of the user and use it for further conversation by the chatbot. ● Example : ● >> ● Hi, I am a chatbot. What is your name? ● >>Nidhi ● Oh, Nidhi in which grade you are right now? ● >>8 ● Nidhi you are in 8th grade. Can I ask you one question? yes or no? ● >>yes ● Tell me 1024+98=? ● >>1122 ● Good! Your answer is correct. Bye ● >>bye

print("Hi, I am a chatbot. What is your name?")
name = input(">> ")

print(f"Oh, {name}, in which grade are you right now?")
grade = input(">> ")

print(f"{name}, you are in {grade} grade. Can I ask you one question? yes or no?")
response = input(">> ")

if response.lower() == "yes":
    print("Tell me, what is 1024 + 98?")
    answer = input(">> ")
    if answer == "1122":
        print("Good! Your answer is correct. Bye")
    else:
        print("Sorry, your answer is incorrect. Bye")
else:
    print("Okay, Bye!")
