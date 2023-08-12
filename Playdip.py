import requests
from bs4 import BeautifulSoup
import os


class playdip:

    def check_cred():
        files = os.listdir()
        if "USERNAME.txt" and "PASSWORD.txt" in files:
            with open("USERNAME.txt", "r") as f:
                user = f.read()
                f.close()
            with open("PASSWORD.txt", "r") as w:
                passw = w.read()
                w.close()
            print(f"Would you like to proceed with {user} as username and {passw} as password? Y/N")
            Ch = input()
            check = Ch.lower()
            if check == "y":
                playdip.send_request(username=user, password=passw)
                exit()
            elif check == "n":
                pass
        else:
            print("DID NOT DETECT CREDENTIAL FILES, continuing to login...")
                


    def get_auth():
        user = input("Please input your PlayDip username: ")
        passw = input("Please input your PlayDip password: ")
        print("")
        print("Would you like the program to remember you? this will create two text files named 'PASSWORD.txt' and 'USERNAME.txt'.\nthis will store your info to remember who you are to later login automatically. please be aware that the files MUST be in the same directory as the program.")
        remember = input("would you like the program to remember you? Y/N\n")
        return user, passw, remember
    
    def check_remember(user, passw, confirm):
        conf = confirm.lower()
        if conf == "y":
            with open("PASSWORD.txt", "x") as f:
                f.write(passw)
                f.close()
            with open("USERNAME.txt", "x") as w:
                w.write(user)
                w.close()
        elif conf == "n":
            pass
    

    def send_request(username, password):
        payload = {
            'page_act': '', 
            'username': f'{username}',
            'password': f'{password}',
            'remember_me': '1'
            }
        response = requests.post("https://www.playdiplomacy.com/login.php", params=payload)
        soup = BeautifulSoup(response.text, features="lxml")
        data = soup.find("div", id="member_box").find("ul")
        text = list(data.descendants)
        for i in range(2, len(text), 2):
            print(text[i], end="\n")
        print('-'*30)
        print(data.text)
        print("")
        input("Press enter to leave...")
    

if __name__ == "__main__":
    playdip.check_cred()
    user, passw, remember = playdip.get_auth()
    playdip.check_remember(user=user, passw=passw, confirm=remember)
    playdip.send_request(username=user, password=passw)

