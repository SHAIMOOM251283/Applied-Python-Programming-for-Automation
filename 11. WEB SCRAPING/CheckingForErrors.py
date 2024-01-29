import requests
#res = requests.get('http://inventwithpython.com/page_that_does_not_exist')
#res.raise_for_status()

res = requests.get('http://inventwithpython.com/page_that_does_not_exist')
try:
   res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % (exc))

# Always call raise_for_status() after calling requests.get(). 