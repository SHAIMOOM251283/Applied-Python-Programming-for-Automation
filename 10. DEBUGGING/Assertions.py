podBayDoorStatus = 'open'
assert podBayDoorStatus == 'open', 'The pod bay doors need to be "open".'
podBayDoorStatus = "I\'m sorry, Dave. I\'m afraid I can't do that.'"
assert podBayDoorStatus == 'open', 'The pod bay doors need to be "open".' 

#podBayDoorStatus = 'open'
#assert podBayDoorStatus == 'open', 'The pod bay doors need to be "open".'
##podBayDoorStatus = "I'm sorry, Dave. I'm afraid I can't do that."
#assert podBayDoorStatus == "I'm sorry, Dave. I'm afraid I can't do that.", 'The pod bay doors need to be "open".'

market_2nd = {'ns': 'green', 'ew': 'red'}
mission_16th = {'ns': 'red', 'ew': 'green'}
def switchLights(stoplight):
    for key in stoplight.keys():
        if stoplight[key] == 'green':
            stoplight[key] = 'yellow'
        elif stoplight[key] == 'yellow':
            stoplight[key] = 'red'
        elif stoplight[key] == 'red':
            stoplight[key] = 'green'
switchLights(market_2nd)
assert 'red' in market_2nd.values(), 'Neither light is red! ' + str(market_2nd)

