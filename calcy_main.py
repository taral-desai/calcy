from calcy import *
print(responses[0])
print(responses[1])
while True:
    print()
    texts=input("what you want to calculate? ")
    for word in texts.split(" "):
        if word.upper() in operations:
            try:
                l=extract_numbers_from_text(texts)
                r=operations[word.upper()](l[0],l[1])
                print(r)
            except:
                print("Something is wrong please retry")
            finally:
                break
        elif word.upper() in commands:
            commands[word.upper()]()
            break
    else:
        sorry()
            
                    

