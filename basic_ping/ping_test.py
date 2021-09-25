import os
import os.path
import shutil
i=0

with open("device_list.txt") as f:
    hostname = f.read().splitlines()

    for x in hostname:
        response = os.system("ping -n 1 " + x )
        if response == 0:
            pingstatus = "Network Active"
            print("%s is active" %(x))
            with open("active_device_list.txt", "a") as df:
                df.write("%s is active\n" %(x))
            df.close()
        else:
            pingstatus = "Network Error"
            print("%s is inactive" %(x))
            with open("active_device_list.txt", "a") as df:
                df.write("%s is inactive\n" %(x))
            df.close()