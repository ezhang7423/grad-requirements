FILTERS = ['@', '&']
# AVOID = ['*']
AVOID = []

def not_wanted(clas):
    for filter in FILTERS:
        if filter not in clas:
            return True
    for avoid in AVOID:
        if avoid in clas:
            return True


if __name__ == '__main__':

    res= []
    with open('classes.txt', 'r') as fin:
        classes = fin.readlines()

    for clas in classes:
        if not_wanted(clas):
            continue
        res.append(clas)

    print('FOUND THESE CLASSES:')        
    print('\n'.join(res))