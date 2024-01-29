#def spam():
#   bacon()
#def bacon():
#    raise Exception('This is the error message.')
#spam()

#def spam():
#    try:
#        bacon()
#    except Exception as e:
#        print(f'An exception occurred: {e}')
#def bacon():
#    raise Exception('This is the error message.')
#spam()

#def function_a():
    # This function calls another function that raises an exception
#    function_b()
#def function_b():
    # This function raises an exception
#    raise ValueError("This is an unhandled exception")
# Call the first function that triggers the exception
#function_a()

#def function_a():
#    try:
#        function_b()
#    except Exception as e:
#        print(f'An exception occured: {e}')
#def function_b():
#    raise ValueError("This is an unhandled exception.")
#function_a()

import traceback
try:
   raise Exception('This is the error message.')
except:
   errorFile = open('errorInfo.txt', 'w')
   errorFile.write(traceback.format_exc())
   errorFile.close()
   print('The traceback info was written to errorInfo.txt.')
