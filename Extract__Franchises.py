from API_call import API_Call

def Extract__Franches():
    data = API_Call('franchises')
    return(data)
