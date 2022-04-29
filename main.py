import time


# if your using a text file, set to true, if your copy and pasting set to false
TextFile = False
def main():
    if TextFile is True:
        InputTex = input("File Directory: ")
        InputText = open(InputTex,"r")
    else:
        InputText = input("Paste Cipher Text: ")
    OutPut = []
    SolveKey = 0
    for x in range(1,27):
        start = time.time()
        for i in InputText:
            if i == " ":
                OutPut.append(i)
                pass
            temp = ord(i)
            temp += SolveKey
            if temp > 122:
                overval = temp - 122
                temp = 96
                temp += overval
            tempx = chr(temp)
            OutPut.append(tempx)
        print(f"[{SolveKey}] ", end="")
        for i in OutPut:
            print(i,end="")
        EndTime = time.time()
        ElapsedTime = EndTime - start
        print(f" in f{ElapsedTime} seconds!")
        SolveKey += 1
        OutPut = []
if __name__ == "__main__":
    main()
