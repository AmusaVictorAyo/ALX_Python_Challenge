#Mad Libs is a classic word game where players fill in the blanks of a story with random words, creating a silly and often nonsensical narrative.
#Building a Mad Lib Generator.
My_Story = (
    f"\"On a beautiful (Adjective_1) day, I went to the Zoo. I saw a funny (Adjective_2) monkey swinging from the trees.  Then, I spotted a \n"
    f"majestic (Adjective_3) lion lounging in the sun. What a wild and (Adjective_4) experience!\""
)
print(f"Input adjectives(not more than seven characters) where necessary in the text below:\n\n{My_Story}\n")
print("Enter your 'adjectives' in the prompt below\n")
Adjective_1 = input("Enter Adjective_1: ")
Adjective_2 = input("Enter Adjective_2: ")
Adjective_3 = input("Enter Adjective_3: ")
Adjective_4 = input("Enter Adjective_4: ")

Adjectives = [Adjective_1, Adjective_2, Adjective_3, Adjective_4]
for adj in range(len(Adjectives)): 
    if len(Adjectives[adj]) > 9: #Checking if adjectives are more than 9 characters.
        Adjectives[adj] = "\"Wrong, input!\""

Reformed_Story = (
    f"On a beautiful {Adjectives[0]} day, I went to the Zoo. I saw a funny {Adjectives[1]} monkey swinging from the trees. Then, I spotted a "
    f"majestic {Adjectives[2]} lion lounging in the sun. What a wild and {Adjectives[3]} experience!"
)
print(Reformed_Story)