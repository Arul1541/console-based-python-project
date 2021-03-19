from pymongo import MongoClient
conn=MongoClient('localhost',27017)
db=conn.TkBooking
coll1=db.Movie
coll2=db.Booking

