import sys
from adam6xxx import ADAM6052

if len(sys.argv) > 1:
    ipAdam = sys.argv[1]
    try:
        adam = ADAM6052(ip=ipAdam, connect=True)
        if not adam.isError() :
            print("connected !")
        else:
            print("not connected !")
    except:
        print("error connecting !")
else:
    print("tambahin ip nya ya !")

