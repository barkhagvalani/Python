import MySQLdb
import time

con = MySQLdb.connect(host='127.0.0.1',user='root')
with con:
        cur = con.cursor()
        #Use the database schema of your table
        cur.execute('use memex')
        #Capture start time
        print (time.strftime("%H:%M:%S"))
        cur=con.cursor()
        for i in range(1,1000001):
                #Generate sample data, SCAN_SHA cannot have the same value more that 7 times in the table
                cur.execute('''INSERT INTO IBI_UNION (SCAN_ID,SCAN_SHA,SCAN_TYPE,SCAN_COUNT,MACHINE_TYPE,SEQUENCE_NBR,IOS_LOAD_DATE,\
MPT_LOAD_DATE,LOAD_DATE) VALUES (%d,'%s','vv',1,'xxx','ss','2-14-01-19 03:14:07','2014-01-19 03:14:07','2015-01-19')'''\
%(i,str(i%200000)))
                #periodic commits to enable concurrent read/write
                if i%10000:
                        cur.execute('COMMIT')
        #Capture end time to calculate load rate
        print (time.strftime("%H:%M:%S"))
