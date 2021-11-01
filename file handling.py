#1.f=open(“data.txt”)
    #1.Identifynameoffile.
    #ans:- name of file is "data"
    #identifynameoffunction.
    #ans:- name of function is open
    #3.Whatis‘f’inabovecode?
    #ans:- 'f' is pointer in the above code 
    #Theabovestatementwill___open_______filein__text______mode
#2. Whatisthedefaultmodeofopeningafile?
      # The default mode of opening file means reading file in text mode.
 #3 Q3.Writethecodeinpythontoopenafilenamed“try.txt 
f =open("try.txt")
f.close()
#Writeastatementinpythontoopenafilenamed“data.txt”storedinfolder“content”inDdrive
f = open(“d:\\content\\data.txt”)

#Q5.Namethethreemodesinwhichfilecanbeopenedinpython
#read(r),write(w),read and write(r+). 
#Whatdoyoumeanbyfileobjectinpython?
#A file object allows us to use, access and manipulate all the user accessible files.
#One can read and write any such files.
#Q7.Write the symbols used in textfile mode for the following operations
# r,w,w+,r+
#Q8Writethestatementtoclosethefile“test.txt”whichisassociatedwithfileobjectnamed“fo”.
#fo.close()
#Q9Writeaprogramtoreadfirst10charactersfromafilenamed“data.txt”
f=open("data.txt",'r+')
data=f.read(10)
print(data)
f.close()
#Q10Writeaprogramtoreadentirecontentfromthefilenamed“test.txt”
=open("test.txt",'r+')
test=f.read()
print(test)
f.close()
#Q11Writeaprograminpythontoreadfirstlinefromthefile(“data.txt”)
f=open("data.txt",'r+')
data=f.readline(1)
print(data)
f.close()
