from backend import *
from random import randint


def SearchId(Id):
    try:
        cur=db.coll1.Movie.count_documents({"_id":Id})
        if(cur==0):
            print("No movie ID found!")
        else:
            curs=db.coll1.Movie.find_one({"_id":Id})
            st=curs['Seat']
            ts=int(st)

            print("Available seats : ",st)
            if (ts > 0):

                print("Enter the no.of tickets you want to Book : ")
                ticket=int(input())
                
                key=randint(1000,10000)
                print("Your Booking Id",key)

                Mov=curs['MovieName']
                
                dur=curs['Duration']
               
                price=curs['Price']
               
                showtime=curs['ShowTime']
                
                seat=ticket

            rec={
                "_id":key,
                "MovieName":Mov,
                "Duration":dur,
                "Price":price,
                "ShowTime":showtime,
                "Seat":seat
            }
            try:
                db.coll1.Booking.insert_one(rec)
            except Exception as e:
                print(e)
            updatetk=ts-ticket
            curs=db.coll1.Movie.update_one({"_id":Id},{"$set":{"Seat":updatetk}})
               
            
    except Exception as e:
        print(e)




        
def adminLogin():
    i=1
    while i!=-1:
        print('\n'*3+"1. View movie list\n2. Add movie \n3. Update existing movie timing\n4.Update Movie ticket Price\n5.Delete a movie \n6.Exit\n")
        ch=input("What you would you like to do? : ")
        if(ch=='1'):
            cur=db.coll1.Movie.find({})
            for obj in cur:
                print(obj)
        elif(ch=='2'):
            key=randint(1,1000)
            print("Enter Movie Name",end=" ")
            Mov=input()
            print("Enter the duration",end=" ")
            dur=input()
            print("Enter the ticket price",end=" ")
            price=int(input())
            print("Enter show time",end=" ")
            showtime=input()
            print("Enter the total no of seats",end=" ")
            seat=input()

            rec={
                "_id":key,
                "MovieName":Mov,
                "Duration":dur,
                "Price":price,
                "ShowTime":showtime,
                "Seat":seat
            }
            try:
                db.coll1.Movie.insert_one(rec)
            except Exception as e:
                print(e)
        elif(ch=='3'):
            cur=db.coll1.Movie.find({})
            for obj in cur:
                print(obj)
            print("Enter the id of the movie : ")
            item=int(input())  
            try:
                cur=db.coll1.Movie.count_documents({"_id":item})
                if(cur==0):
                    print("No movie ID found!")
                else:
                    print("Enter the new showtime to be changed : ")
                    st=input()
                    curs=db.coll1.Movie.update_one({"_id":item},{"$set":{"ShowTime":st}})
                    print("Showtime changed successfully!!!")
            except Exception as e:
                print(e)
            
        elif(ch=='4'):
            cur=db.coll1.Movie.find({})
            for obj in cur:
                print(obj)
            print("Enter the id of the movie : ")
            item=int(input())  
            try:
                cur=db.coll1.Movie.count_documents({"_id":item})
                if(cur==0):
                    print("No movie ID found!")
                else:
                    print("Enter the new price to be changed : ")
                    pr=input()
                    curs=db.coll1.Movie.update_one({"_id":item},{"$set":{"Price":pr}})
                    print("Price Updated!!!")
            except Exception as e:
                print(e)
        elif(ch=='5'):
            cur=db.coll1.Movie.find({})
            for obj in cur:
                print(obj)
            print("Enter the id of the movie : ",end=" ")
            item=int(input()) 
            try:
                cur=db.coll1.Movie.count_documents({"_id":item})
                if(cur==0):
                    print("No movie ID found!")
                else:
                    curs=db.coll1.Movie.delete_one({"_id":item})
                    print("Movie Deleted!!!")
            except Exception as e:
                print(e) 
        else:
            i=-1
            main()

def customer():
   
    i=1
    while i!=-1:
        print('\n'*3+"1. View movie list\n2. Book tickets \n3. Delete Booking \n4. view customer details \n5.Exit")
        ch=input("What you would you like to do? : ")
        if(ch=='1'):
            cur=db.coll1.Movie.find({})
            for obj in cur:
                print(obj)
        elif(ch=='2'):
            cur=db.coll1.Movie.find({})
            for obj in cur:
                print(obj)
            print("Enter the id of the movie : ")
            item=int(input())  
            SearchId(item)
        elif(ch=='3'):
            cur=db.coll1.Booking.find({})
            for obj in cur:
                print(obj)
            print("Enter the id of the movie Customer : ",end=" ")
            item=int(input()) 
            try:
                cur=db.coll1.Booking.count_documents({"_id":item})
                if(cur==0):
                    print("No ID found!")
                else:
                    curs=db.coll1.Booking.delete_one({"_id":item})
                    print("Booking Deleted!!!")
            except Exception as e:
                print(e) 
        elif(ch=='4'):
            cur=db.coll1.Booking.find({})
            for obj in cur:
                print(obj)
        else:
            quit()
            

            
            
           
            

def main():
    print("\n"+"1.Customer\n"+"2.Admin")
    ch=input("Enter an option : ")
    if(ch=='1'):
        customer()
    else:
        user=(input("Enter Username : "))
        if(user=='qwerty'):
            pwd=(input("Enter the password : "))
            if(pwd=='123'):
                adminLogin()

main()
