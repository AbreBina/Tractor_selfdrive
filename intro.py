import time
import datetime

def intro():
    file = open("tractor.txt", "r")
    for line in file:
        print(line,end='')
        time.sleep(0.05)

    print("\r\nLogin to Sun-Bot via SSH:")
    user = input("Username: ")
    passw = input("Password: ")
    print("Welcome back, " + user)
    print("Last login: " + datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
    print("\r\n1) Logitech 3.1 megapixel Ip-camera via network(172.16.1.110)")
    print("2) Built-in Webcam(0) Acer Laptop ap201")
    print("Number of camera(s): 2")
    input("Which? 1~2: ")

if __name__ == "__main__":
    intro()