from datetime import date
from datetime import time
import csv
import time
admin='qcinemas'
global price
price =150.00
def seats(booked):
    print('Reserved seats are shown as "XX" ')
    print('-------------------------------------------------')
    print('-------------------------------------------------')
    for k in 'SCREEN':
        print(k,end='\t ')
    print('\n')
    print('-------------------------------------------------')
    print('-------------------------------------------------\n')
    for i in range(1):
        for j in range(1,101):
            if j in range(1,11):
                if j in booked:
                    print('XX',end='    ')
                else:
                    print(j,end='    ')       
            else:
                if j in booked:
                    print('XX', end='   ')
                else :
                    print(j,end='   ')
        
            if j%10==0:
                print('')     
                 
def changeprice():
    decision=input("Do you really want to change the price ? Yes/No :")
    p=['yes','y','YES','Yes']
    if decision in p:
        pswd=input('Enter Password To Continue :')
        if pswd==admin:
            global price
            price=float(input(("Enter New Price :")))
            print('Price Change Successful...\nNew Price:',price)
    


def user():
  name=input("Enter Name :")
  tim=time.strftime('%H:%M')
  date=time.strftime('%d/%m/%Y')
  print(date)
  seat='11,12'
  showt='1:30'
  movie='Bheeshma'
  bookid=0
  showtime='12:30'
  f=open('sales.csv','w')
  fieldnames=["Booking id",'Date','Time','Name','Seat','Movie','Show Time']

  writer=csv.DictWriter(f,fieldnames=fieldnames)
  writer.writeheader()
  writer.writerow({"Booking id":bookid,'Date':date,'Time':tim,'Name':name,'Seat':seat,'Movie':movie,'Show Time':showtime})
  f.close()
def createinfo():
  f=open('shows.csv','a')
  fieldnames=['Show Number','Show Name','Showtime','Seats filled']
  writer=csv.DictWriter(f,fieldnames=fieldnames)
  while True:
      shownumber=int(input("enter the show number"))
      showname=input("Enter The Name of the movie :")
      showtime=input("enter the time of the movie:")
      seat=input("seat filed(separate the seat numbers with a comma)")
      writer.writerow({'Show Number':shownumber,'Show Name':showname,'Showtime':showtime,'Seats filled':seat})
      ch=input("do you want to quit?")
      if ch in['y','Y']:
          break
  f.close()
def info():
    print("enter name:")
    name=input()
    print('    Upcoming Shows')
    fin=open('shows.csv','r')
    reader=csv.DictReader(fin)
    templist=list(reader)
    for row in templist:
        print(row['Show Number'],row['Show Name'],row['Showtime'],sep='\t')
    userchoice=input("enter the show number to proceed")
    for row in templist:
        print(row['Show Number'])
        if row['Show Number']==userchoice:
            temp=row['Seats filled'].split(',')
            for i in range(0, len(temp)):
                temp[i] = int(temp[i])
            seats(temp)
            rowno=input("enter the seat number you want")
            row['Seats filled']=row['Seats filled']+','+rowno
            break
    fout=open('shows.csv','w')
    fieldnames=['Show Number','Show Name','Showtime','Seats filled']
    writer=csv.DictWriter(fout,fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(templist)
    fout.close()
    fin.close()
    
 
 seats([12,22])


    
