import requests
import time
from rq import Queue
from worker import conn

q = Queue(connection=conn)

def process(current=0):
    if current < 1000000:
        pcode = '{0:06d}'.format(current)
        print("data is")
        print(pcode_to_data(pcode))
        next = current + 1
        q.enqueue(process, next)
    else:
        next = 0
        q.enqueue(process, next)

def pcode_to_data(pcode):
    if int(pcode) % 1000 == 0:
        print(pcode)
    
    page = 1
    results = []
    
    while True:
        try:
            response = requests.get('http://developers.onemap.sg/commonapi/search?searchVal={0}&returnGeom=Y&getAddrDetails=Y&pageNum={1}'
                                    .format(pcode, page)) \
                               .json()
        except requests.exceptions.ConnectionError as e:
            print('Fetching {} failed. Retrying in 2 sec'.format(pcode))
            
            time.sleep(2)
            continue
            
        results = results + response['results']
    
        if response['totalNumPages'] > page:
            page = page + 1
        else:
            break
            
    return results
