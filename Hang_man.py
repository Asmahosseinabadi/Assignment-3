import random

words_bank=["tree","book","sky","woman","life","iran","green","cow","cat"]
user_mistakes=0

green_chars=[]
red_chars=[]

word=random.choice(words_bank)


while user_mistakes<6:
    for i in range(len(word)):    
        if word[i] in green_chars:
            print(word[i].lower(),end=" ")
        else:
            print("-",end=" ")
    user_char=input("enter your guess: ").lower()
    if user_char==word[i]:
        print("You Win🎉")
        break
    if len(user_char)==1:
        if user_char in word:
            green_chars.append(user_char)
            print("✅")
        else:
            red_chars.append(user_char)
            user_mistakes+=1
            print("❌")
    else:
        print("Error😑")       

if user_mistakes==6:
    print("Game Over 💀")
    
    





