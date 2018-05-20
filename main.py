# MACOS (tested via PyCharm)
#  from faster_homework import config

# WINDOWS (tested via PyCharm)
import config

githubURL = input("Enter the URL to the base repo: ")

id1 = input("Enter ID of the pull for %s: " % config.name1)
id2 = input("Enter ID of the pull for %s: " % config.name2)
id3 = input("Enter ID of the pull for %s: " % config.name3)
id4 = input("Enter ID of the pull for %s: " % config.name4)
id5 = input("Enter ID of the pull for %s: " % config.name5)
id6 = input("Enter ID of the pull for %s: " % config.name6)
id7 = input("Enter ID of the pull for %s: " % config.name7)
id8 = input("Enter ID of the pull for %s: " % config.name8)
idList = [id1, id2, id3, id4, id5, id6, id7, id8]

print("\ncopy the entire block of text below and paste it into your terminal at the root repo\n")

for i, n in enumerate(config.nameList):
        print("git fetch origin pull/"+idList[i]+"/head:"+n)

print("\nfor example: use `git checkout %s` to access the students code" % config.name1)
