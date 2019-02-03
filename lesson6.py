def countdown(i):
    while i > 0:
        print i
        i = i -1

    print "Blastoff!"

#countdown(3)

def find_last(s, target):
    last_target = -1

    while True:
        target_location = s.find(target, last_target+1)
        if target_location == -1:
            break
        last_target = target_location

    return last_target

print find_last('aaaa', 'a')
