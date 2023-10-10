users=["sachin","rahul","rohit","kohli","dravid","ganguly"]
sachin_following=["rahu","ganguly","dravid"]
sachin=set(users).difference(set(sachin_following))
sachin.remove("sachin")
print(sachin)