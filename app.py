from rq import Queue
from worker import conn
from extract import process

# every restart of the app start a new cycle of scrapping
q = Queue(connection=conn)
q.enqueue(process, 0)