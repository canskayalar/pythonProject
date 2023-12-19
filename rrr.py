class cec():
    def __init__(self,members,tasks,motion):
        self.members=members
        self.tasks=tasks
        self.motion=motion

emre=cec("emre","sunum","lider")
print(emre.members,emre.tasks,emre.motion)
mert=cec("mert","yemek","temizlik")
print(mert.members,mert.tasks,mert.motion)

class sec():
    def __init__(self,
