def badge_maker(name):
    return (f"Hello, my name is {name}.")

name = "Guido van Rossum"
print(badge_maker(name))


def batch_badge_creator(names):    
    
    # Using for loop
    badges = []
    for name in names:
        badge = badge_maker(name)
        badges.append(badge)
    return badges
    
    
    # Using list comprehensions
    badges = [badge_maker(name) for name in names]
    
    return badges

names = ['Guido', 'Edsger', 'Ada', 'Charles', 'Alan', 'Grace', 'Linus', 'Matz']
print(batch_badge_creator(names))


def assign_rooms(names):
    index = 1
    messages = []    
    for name in names:
        # print(index)
        message = f"Hello, {name}! You'll be assigned to room {index}!"
        messages.append(message)
        index +=1
        
    return messages


names = ['Guido', 'Edsger', 'Ada', 'Charles', 'Alan', 'Grace', 'Linus', 'Matz']
print(assign_rooms(names))

def printer(names):
    
    output1 = batch_badge_creator(names)
    for message in output1:
        print(message)
        
    output2 = assign_rooms(names)
    for message2 in output2:
        print(message2)
    

names = ['Guido', 'Edsger', 'Ada', 'Charles', 'Alan', 'Grace', 'Linus', 'Matz']
    
printer(names)