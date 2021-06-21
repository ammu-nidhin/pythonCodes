import time

# print(time.localtime().tm_hour)
current_time=time.localtime().tm_hour
if (current_time<6 or current_time>18):
    print("Its night")
else:
    print("Its day")


