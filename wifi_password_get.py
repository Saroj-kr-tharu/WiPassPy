""" Program to get all the wifi passwords saved in a device """
from msvcrt import getch
import os
import subprocess,re

class wifi:

    def __init__(self):
        self.ssid=[]
        self.passwords=[]

    def save(self):
        ''' This function is to save ssid and pass to file '''
        listfloder=os.listdir();
        if "saved_file" not  in  listfloder:
            os.mkdir("saved_file")
        

        with open("saved_file/file.txt","w") as file:
            for i in range(len(self.ssid)):
                msg=(f"\t\t {i} SSID  ----> {self.ssid[i]} ")
                file.write(msg)
                msg=(f"\t\t {i} PASSWORDS  ----> {self.passwords[i]} ")
                file.write(msg)
                msg=("\n")
                file.write(msg)
        file.close()
        print("\n\t\t ssid and passwords is saved to file.txt ")
        

    def show( self):
        for i in range(len(self.ssid)):
            print(f"\t\t {i} SSID  ----> {self.ssid[i]} ")
            print(f"\t\t {i} PASSWORDS  ----> {self.passwords[i]} ")
            print("\n",end="")
        

    def geting_password(self):
        command="netsh wlan show profile"
        networks=subprocess.check_output(command,shell=True)
        networks=networks.decode("utf-8")
        network_name=re.findall("(?:Profile\s*:\s)(.*)",str(networks))

        #checking 
        os.system("cls")
        print(f"\t <----- Getting All The Siid and Password ------>")
        for name in network_name:
            command="netsh wlan show profile "+ '''"'''+name + '''"''' +" key=clear "
            result_with_key=subprocess.check_output(command,shell=True)
            result_with_key=result_with_key.decode("utf-8")

            password=re.findall("(?:Key Content\s*:)(\s*.*)",result_with_key)
            is_preset=re.findall("(?:Security key\s*:)(\s*.*)",result_with_key)

            if is_preset[0]==" Present\r":
                for pas in password:
                    self.ssid.append(name)
                    self.passwords.append(pas)

            elif is_preset[0] ==" Absent\r":
                    self.ssid.append(name)
                    self.passwords.append("NO PASSWORD")

            


def main():
    wi=wifi ()
    wi.geting_password()
    wi.show()
    wi.save()
    # getch()


if __name__=="__main__":
    main()


