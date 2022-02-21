#Bank_management
import sys
import mysql.connector
con=connector.connect(host="localhost",user="root",passwd="Dipti@123",databse="BANK")
def newAcc():
    name=input("Enter your name:")
    accno=input("Enter your account no:")
    dob=input("Enter your date of birth:")
    mob=int(input("Enter your mpbile no:"))
    add=input("Enter your address:")
    ob=int(input("Enter your opening balance:"))
    data1=(name,accno,dob,mob,add,ob)
    data2=(name,accno,ob)
    sql1=insert into account values(%s,%s,%s,%s,%s,%s)
    sql2=insert into amount values(%s,%s,%s)
    c=con.cursor()
    c.execute(sql1,data1)
    c.execute(sql2,data2)
    con.commit()
    print("data entered successfully")
def depamt():
    amo=int(input("Enter the amount you want to deposit:"))
    accno=input("Enter account number:")
    a="select balance from amount where accno=%s"
    data=(accno,)
    c=con.cursor()
    c.execute(a,data)
    result=c.fetchone()
    tam=result[0]+amo
    sql="update amount set balance=%s where accno=%s"
    d=(tam,accno)
    c.executes(sql,d)
    con.commit()
    main()
def withamt():
    amo=int(input("Enter amount you want to withdraw:"))
    accno=input("Enter your account number:")
    a="select balance from amount where accno=%s"
    data=(accno,)
    c=con.cursor()
    c.execute(a,data)
    result=c.fetchone()
    tam=result[0]-amo
    sql="update amount set balance=%s ehere accno=%s"
    d=(tam,accno)
    c.executes(sql,d)
    con.commit()
    main()
def balance():
    accno=input("Enter your account number:")
    a="select balance from amount where accno=%s"
    data=(accno,)
    c=con.cursor()
    c.execute(a,data)
    result=c.fetchone()
    print("Balance for account",accno,"is",result[0])
    main()
def dispacc():
    accno=input("Enter your account number:")
    a="select * from account where accno=%s"
    data=(accno,)
    c=con.cursor()
    c.execute(a,data)
    result=c.fetchone()
    for i in result:
        print(i,end=" ")
    main()
def closeacc():
    accno=input("Enter your account number:")
    sql1="delete from account where account no=%s"
    sql2="delete from amount where account no=%s"
    data=(accno,)
    c=con.cursor()
    c.execute(sql1,data)
    c.execute(sql2,data)
    con.commit()
    main()
def main():
    print("""
    1.OPEN NEW ACCOUNT
    2.DEPOSIT AMOUNT
    3.WITHDRAW AMOUNT
    4.BALANCE ENQUIRY
    5.DISPLAY CUSTOMER DETAILS
    6.CLOSE AN ACCOUNT
    7.EXIT
    """)
    choice=input("Enter task no:")
    if choice==1:
        newAcc()
    elif choice==2:
        depamt()
    elif choice==3:
        withamt()
    elif choice==4:
        balance()
    elif choice==5:
        dispacc()
    elif choice==6:
        closeacc()
    elif choice==7:
        print("thank you ...  visit again")
        sys.exit()
    else:
        print("please provide valid choice")
        main()
main()

    
    
    

    
    
