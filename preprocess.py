def preprocess_onlineorder(onlineorder):
    if onlineorder.lower == 'yes':
        return 1
    else:
        return 0
    
    
def preprocess_booktable(booktable):
    if booktable.lower == 'yes':
        return 1
    else:
        return 0

def preprocess_data(data):
    votes = data['votes']
    cost = data['cost']
    onlineorder = preprocess_onlineorder(data['onlineorder'])
    booktable = preprocess_booktable(data['booktable'])
    location = data['locationEnc']
    resttype = data['rest_typeEnc']
    cuisines = data['cuisinesEnc']
    listtype = data['typeEnc']
    city = data['cityEnc']
    final_data = [ 'votes', 'cost', 'location', 'resttype', 'cuisines', 'listtype', 'city', 'onlineorder', 'booktable' ]