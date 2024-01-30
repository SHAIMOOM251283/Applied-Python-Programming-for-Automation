#print('Cats', 'Dogs', 'Frogs', sep=' & ')

import threading
threadObj = threading.Thread(target=print, args=['Cats', 'Dogs', 'Frogs'], kwargs={'sep': ' & '})
threadObj.start()