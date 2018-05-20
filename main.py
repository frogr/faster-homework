from faster_homework import config

githubURL = input("Enter the URL to the base repo: ")

id1 = input("Enter ID of the pull for %s: " % config.name1)
id2 = input("Enter ID of the pull for %s: " % config.name2)
id3 = input("Enter ID of the pull for %s: " % config.name3)
id4 = input("Enter ID of the pull for %s: " % config.name4)
id5 = input("Enter ID of the pull for %s: " % config.name5)
id6 = input("Enter ID of the pull for %s: " % config.name6)
id7 = input("Enter ID of the pull for %s: " % config.name7)
id8 = input("Enter ID of the pull for %s: " % config.name8)
print("\ncopy the entire block of text below and paste it into your terminal at the root repo\n")
print("git fetch origin pull/"+id1+"/head:"+config.name1)
print("git fetch origin pull/"+id2+"/head:"+config.name2)
print("git fetch origin pull/"+id3+"/head:"+config.name3)
print("git fetch origin pull/"+id4+"/head:"+config.name4)
print("git fetch origin pull/"+id5+"/head:"+config.name5)
print("git fetch origin pull/"+id6+"/head:"+config.name6)
print("git fetch origin pull/"+id7+"/head:"+config.name7)
print("git fetch origin pull/"+id8+"/head:"+config.name8)

