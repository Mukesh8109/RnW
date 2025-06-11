import uuid
def uid1():
    t = uuid.uuid1()
    return t
def uid2():
    f=uuid.uuid4()
    return f


print(uid1)
print(uid2)

