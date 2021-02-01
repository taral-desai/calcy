responses=["welcome to smart calculator","I'm calcy","Thanks",
           "Sorry, this is beyond my abilities at this moment."]
def extract_numbers_from_text(texts):
    l=[ ]
    for text in texts.split(" "):
        try:
            l.append(float(text))
        except ValueError:
               pass
    return(l)

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def multiply(a,b):
    return a*b

def division(a,b):
    return a/b

def lcm(a,b):
    LCM=a if a>b else b
    while LCM<=a*b:
        if L%a==0 and L%b==0:
            return LCM
        LCM+=1

def hcf(a,b):
    HCF=a if a<b else b
    while H>=1:
        if a%HCF==0 and b%HCF==0:
            return HCF
        HCF-=1

def end():
    print(responses[2])
    input("Press Enter key to exit")
    exit()

def myname():
    print(responses[1])

def sorry():
    print(responses[3])

operations={"PLUS":add, "ADD":add, "ADDITION":add, "SUM":add, "SUB":sub,
            "MINUS":sub,"SUBTRACTION":sub,"DIFF":sub,"DIFFERENCE":sub,
            "PRODUCT":multiply,"MULTIPLY":multiply,"MULTIPLICATION":multiply,
            "DIVIDE":division,"UPON":division}
commands={"NAME":myname,"END":end,"EXIT":end,"CLOSE":end}

