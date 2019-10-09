import os
class teacher:
    def __init__(self,name,log,pas):
        self.log=log
        self.pas=pas
        self.name=name
    def addteacher(self):
        fle=open('teacherid.txt','a')
        k=self.log+';'+self.pas+'\n'
        fle.write(k)
        fle.close()
class student:
    def __init__(self,name,roll,log,pas,depart,semester,fee,subject):
        self.name=name
        self.roll=roll
        self.depart=depart
        self.fee=fee
        self.subject=subject
        self.log=log
        self.semester=semester
        self.pas=pas
    def registersubjects(self):
        nol=0;line=0
        file=open('student.txt')
        while True:
            k=file.readline()
            nol+=1
            if self.log in k:
                break
        k=k[:len(k)-1]
        l=k.split(';')
        l[7]+=self.subject
        file.close()
        flee=open('student.txt')
        fl=open('test.txt','w')
        while True:
            k=flee.readline()
            line+=1
            if k=="":
                break
            if line==nol:
                for obj in l:
                    if obj==l[7]:
                        fl.write(obj)
                    else:
                        fl.write(obj+';')
                fl.write('\n')
                line+=1
            else:
                fl.write(k)
        flee.close()
        fl.close()
        os.remove('student.txt')
        os.rename('test.txt','student.txt')
    def addoffersub(self):
        d=(self.depart).upper()+'.txt'
        file=open(d,'a')
        lst=[];i=0
        ch='y'
        while ch=='y' or ch=='Y':
            name=str(input(f'Enter the name of subject you wish to add for {self.depart} department and semester {self.semester}\n'))
            lst.insert(i,name)
            i+=1
            code=str(input(f'Enter the subject code for {name}\n'))
            lst.insert(i,code)
            i+=1
            ch=str(input("Do you want to add another subject?\nEnter y if yes.Else press any key\n"))   
        file.write(';'+self.semester+';\n')
        for obj in lst:
            file.write(obj+';')
        file.write('\n*\n')
        file.close()
    def updateoffersub(self):
        l=[]
        ch='y'
        while ch=='y' or ch=='Y':
            sub=str(input("Enter the name of subject you wish to add\n"))
            cod=str(input("Enter the code for this subject\n"))
            l.append(sub)
            l.append(cod)
            ch=str(input("Enter y if you wish to add another subject.Else press any key\n"))
        ch='y'
        nol=0;line=0
        sem=';'+self.semester+';\n'
        d=(self.depart).upper()+'.txt'
        file=open(d)
        while True:
            k=file.readline()
            nol+=1
            if sem==k:
                break
        nol+=1
        k=file.readline()
        print(k)
        sub_lst=k.split(';')
        sub_lst.remove('\n')
        sub_lst.extend(l)
        file.close()
        flee=open(d)
        fl=open('test.txt','w')
        line=0
        while True:
            k=flee.readline()
            line+=1
            if k=="":
                break
            if line==nol:
                for obj in sub_lst:
                    fl.write(obj+';')
                fl.write('\n')
                line+=1
            else:
                fl.write(k)
        flee.close()
        fl.close()
        os.remove(d)
        os.rename('test.txt',d)
    def showoffersub(self):
        print('Your offered subjects are:\n')
        k='';l=[]
        fle=open('student.txt')
        while True:
            k=fle.readline()
            if self.name in k:
                break
            if k=="":
                break
        lst=k.split(';')
        fle.close()
        semes=';'+lst[5]+';\n';dep=lst[4]
        dep=dep.upper()+'.txt'
        file=open(dep)
        while True:
            k=file.readline()
            if k==semes:
                break
            if k=="":
                break
        k=file.readline()
        l=k.split(';')
        l.remove('\n')
        i=0
        while i<=len(l)-1:
            print("Name of offered subject is :",l[i])
            s7=l[i]
            i+=1
            print(f'Subject code of {s7} is :',l[i])
            i+=1
        file.close()   
            
    def addstudent(self):
        FILE=open('student.txt','a')
        k=self.name+';'+str(self.roll)+';'+self.log+';'+self.pas+';'+self.depart+';'+str(self.semester)+';'+self.fee+';\n'
        FILE.write(k)
        FILE.close()
        fle=open('studentid.txt','a')
        k=self.log+';'+self.pas+'\n'
        fle.write(k)
        fle.close()
    def payfee(self):
        count=0;t=True;p=True;nol=0;line=0
        file=open('student.txt')
        while True:
            k=file.readline()
            nol+=1
            if self.name in k:
                break
        for i in range(len(k)):
            if k[i]==';':
                count+=1
            if (count==6) and t:
                index=i
                t=False
            if (count==7) and p:
                p=False
                index1=i
        write=k[:index]+';'+self.fee+k[index1:]
        file.close()
        flee=open('student.txt')
        fl=open('test.txt','w')
        while True:
            k=flee.readline()
            line+=1
            if k=="":
                break
            if line==nol:
                fl.write(write)
                line+=1
            else:
                fl.write(k)
        flee.close()
        fl.close()
        os.remove('student.txt')
        os.rename('test.txt','student.txt')
        
        
        
            
                
            
    def show(self):
        t=True;k=''
        fle=open('student.txt')
        while True:
            k=fle.readline()
            if self.name in k:
                t=False
                break
            if k=="":
                break
        if t:
            print(f'{self.name} does not exist')
        lst=k.split(';')
        for i in range(8):
            if i==0:
                print(f'Name of student is {lst[i]}')
            if i==1:
                print(f'Student roll number is {lst[i]}')
                rno=int(lst[i])
            if i==2:
                print(f'Login ID of student is {lst[i]}')
            if i==3:
                print(f'Password is {lst[i]}')
            if i==4:
                print(f'Department is {lst[i]}')
                dep=lst[i]
            if i==5:
                print(f'Semester is {lst[i]}')
                sms=int(lst[i])
            if i==6:
                print(f'Fee status is {lst[i]}')
            if i==7:
                s7=student(' ',rno,' ',' ',dep,sms,' ',' ')
                s7.showregisteredsubjects()
        fle.close()
    def showregisteredsubjects(self):
        l=[];lst=[];la=[]
        FILE=open('student.txt')
        while True:
            k=FILE.readline()
            if (';'+str(self.roll)+';')in k:
                if (';'+self.depart+';')in k:
                    if (';'+str(self.semester)+';')in k:
                        break
        lst=k.split(';')
        l=lst[7].split('!')
        l.remove('\n')
        FILE.close()
        semes=';'+lst[5]+';\n';dep=lst[4]
        dep=dep.upper()+'.txt'
        file=open(dep)
        while True:
            k=file.readline()
            if semes in k:
                break
        k=file.readline()
        la=k.split(';')
        la.remove('\n')
        i=0;j=0
        print("Your registered subjects are:\n")
        while i<len(la):
            j=0
            while j<len(l):
                if l[j] in la[i]:
                    k=i-1
                    print(f'Subject is {la[k]}-{la[i]}')
                    break
                j+=1
            i+=1
        

def confirmID(l,p):
    file=open('studentid.txt')
    s=l+';'+p+'\n'
    while True:
        k=file.readline()
        if (s==k):
            return 'student'
        if k=="":
            break
    file.close()
    fl=open('teacherid.txt')
    while True:
        k=fl.readline()
        if (s==k):
            return 'teacher'
        if k=="":
            break
    fl.close()
    fle=open('accountantid.txt')
    while True:
        k=fle.readline()
        if (s==k):
            return 'accountant'
        if k=="":
            break
    fle.close()
    if k=="":
        print("Incorrect user name or password")
#---------------------------------------------------------------#

#----------------------------------------------------------------#
print("******Welcome to LMS(Learning Management System)******")
log=str(input("Enter login ID\n"))
pas=str(input("Enter password\n"))
typ=confirmID(log,pas)
charac='y'
while charac=='y' or charac=='Y':
    if typ=='accountant':
        print("What do you want to do?You can:")
        print("1:-Add a new student")
        print("2:-Change fee status of student")
        print("3:-Add an accountant ID and password")
        print("4:-Add a new teacher ID and password")
        print("5:-Add offered subjects for a department and semester")
        print("6:-Add new offered subjects for a department and semester")
        choice=int(input('Enter corresponding number for your action:\n'))
        if choice==1:
            ch='y'
#Function for adding a student#
            while ch=='y' or ch=='Y':
                l=str(input(f"Enter login ID of student you wish to add:\n"))
                p=str(input(f"Enter password for this login ID:\n"))
                n=str(input(f"Enter name of student you wish to add:\n"))
                r=int(input(f"Enter roll number of {n}:\n"))
                d=str(input(f"Enter department of {n}\n"))
                sm=int(input("Enter the semester\n"))
                st=str(input("Enter fee status i.e. paid or not paid\n"))
                S=student(n,r,l,p,d,sm,st,[])
                S.addstudent()
                print(f'{n} was added successfully.Do you want to add another student?Enter y if yes.Otherwise press any key')
                ch=str(input())
#Function to show student#
        if choice==2:          
            n=str(input(f"Enter name of student whose details you wish to see:\n"))
            s2=student(n,0,' ',' ',' ',7,' ',[])
            s2.show()
            pa=str(input("Enter fee status i.e. paid or not paid\n"))
            s3=student(n,0,' ',' ',' ',7,pa,[])
            s3.payfee()
        if choice==3:
                   n=str(input("Enter login ID for new accountant\n"))
                   p=str(input("Enter password for this accountant\n"))
                   file=open('accountantid.txt','a')
                   k=n+';'+p+'\n'
                   file.write(k)
                   file.close()
                   print("This ID and password was added successfully")
        if choice==4:
            l=str(input(f"Enter login ID of teacher you wish to add:\n"))
            p=str(input(f"Enter password for this login ID:\n"))
            n=str(input(f"Enter name of teacher you wish to add:\n"))
            t=teacher(n,l,p)
            t.addteacher()
        if choice==5:
            d=str(input("Enter the department for which you wish to add offered subjects\n"))
            s=str(input("Enter the semester\n"))
            s4=student(' ',32,' ',' ',d,s,' ',[])
            s4.addoffersub()
        if choice==6:
            d=str(input("Enter the department for which you wish to add new offered subjects\n"))
            s=str(input("Enter the semester\n"))
            s5=student(' ',32,' ',' ',d,s,' ',[])
            s5.updateoffersub()
    if typ=='teacher':
        print("Login accepted for teacher")
    if typ=='student':
        s=''
        char='y'
        s1=student(log,34,' ',' ',' ',7,' ',[])
        s1.show()
        print("Do you want to register your subjects?Enter y if yes.Else press any key")
        choice=str(input())
        if choice=='y' or choice=='Y':
            s1.showoffersub()
            while char=='y' or char=='Y':
                cod=str(input("Enter the subject code of the subject you want to register\n"))
                s+=(cod+'!')
                char=str(input("Do you want to register another subject.Enter y if yes.Else enter any key\n"))
            st=student(' ',4,log,' ',' ',' ',' ',s)
            st.registersubjects()
    charac=str(input("Enter y if you want to do something more.Else press any key to exit\n"))
    
    
        
        

    
