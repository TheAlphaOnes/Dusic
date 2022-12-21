import os,time

def cleaner():
    try:
        temp = os.listdir("static\\temp")
        if len(temp) != 0 :
            print(True)
            for file in temp:
                os.remove("static\\temp\\"+ file)
                time.sleep(.1)

        else:
            print(False)
    except:
        pass

