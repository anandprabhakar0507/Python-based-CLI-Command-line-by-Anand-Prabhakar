import os
os.system("color 0e")
print("==========================================================================")
print("\n||\tCommand Line Interface CLI 1.0 By Anand Prabhakar,Bihar,India\t||\n||\tPowered by Python. \t\t\t\t\t\t||\n||\tjust learning..no commercial use.. \t\t\t\t||\n")
print("==========================================================================")
def main():
    command = input("\n\tEnter the command you want to execute : ")
    print("Output after execution : \n")
    print("============================================================")
    commanding(command)
    print("============================================================")
    
    
    

def commanding(i):
    os.system("color 0a")
    a = os.system(i)
    print("\n\t\tDo you want to Enter Command again\n")
    print("-------------------------------------------------------------")
    main()
    return a

if __name__ == "__main__":
    main()
