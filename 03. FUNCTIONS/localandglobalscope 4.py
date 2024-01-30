def spam():
    eggs = 'spam local'
    print(eggs) #prints 'spam local'

def bacon():
    eggs = 'bacon local'
    print(eggs) #prints 'bacon local'
    spam()
    print(eggs) #prints 'bacon local'

eggs = 'global'
bacon()
print(eggs) #prints 'global'

# 1. bacon local
# 2. spam local
# 3. bacon local
# 4. global