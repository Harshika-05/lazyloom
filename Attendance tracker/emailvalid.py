email = input("Enter your email : ")
k,j,d=0,0,0
if len(email) >=6:
    if email[0].isalpha():
        if ( "@" in email) and (email.count("@") == 1):
            if (email[-4] == ".") or (email[-3] == "."):
                for i in email:
                    if i==i.isspace():
                        k=1 
                    elif i.isalpha():
                        if i==i.upper():
                            j=1 
                        elif i.isdigit():
                            continue
                        elif i=="_" or i=="." or i=="@":
                            continue
                        else:
                            d=1
                            if k==1:
                                print("Invalid email because no spaces are allowed!")
                                
                                if j==1:
                                    print("Invalid email because uppercase letteres are not allowed!")
                                    if d==1:
                                        print("Invalid email!")
                                    else:
                                        print("Your email has been verified")
            else:
                print("Invalid email because of incorrect position of '.' ")
        else:
            print("There should be only one @ ")
    else:
        print("Invalid email beacuse the email you entered must have an alphabet as its first letter.")
else:
    print("Invalid email.Minimum letter should be 6 !")
    