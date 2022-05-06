import os 
import cv2
import glob
import random
import shutil
from tkinter import *
import datetime
import webbrowser
from PIL import Image,ImageTk

def page1():
    root = Tk()
    root.geometry('1000x800')
    root.minsize(300,400)
    root.maxsize(1000,800)
    root.title('Title page of the assignment')
    f1 = Frame(root,bg='black',borderwidth = 1,pady=0)
    f1.pack(side=TOP,anchor='ne',pady=0)
    f = Frame(root,bg='green',borderwidth =2,pady=30)
    f.pack(side=TOP)
    f2 = Frame(root)
    f2.pack(side=TOP,pady=10)
    f3 = Frame(root)
    f3.pack(side=TOP)
    f4 = Frame(root)
    f4.pack(side = TOP)
    l1= Label(f1,text=f'Date:{datetime.date.today()}',font = ('comicsams',9),pady=0)
    l1.pack(fill =X)
    l = Label(f,text='INFYU LABS Assignment',font = ('comicsams',19,'bold'),pady=0)
    l.pack(fill =X)
    l2 = Label(f2,text = 'Description: This GUI is used generate frames from video given as input and display any number of random frames',font='comicsams 14',pady=100)
    l2.pack(fill=X)
    l3 = Label(f3,text = 'Would you like to continue?',font='comicsams 14',pady=10)
    l3.pack(fill=Y)
    getresult = IntVar()
    b1 = Checkbutton(f4,text = 'do you want to continue?',borderwidth=7,variable= getresult)
    b1.pack(side=LEFT,padx=40)
    b2 = Button(f4,text = 'Submit',command = lambda:gvs(getresult,root))
    b2.pack()
    root.mainloop()
def page2():
    root1 = Tk()
    root1.geometry('1000x800')
    root1.minsize(100,200)
    root1.maxsize(600,250)
    root1.title('This page gets the input path from the user')
    path_value = StringVar()
    path = Label(root1,text= 'Please enter the path of the video without quotes',borderwidth = 10,font =('comicsams',15,'bold'),padx=10,pady=30)
    path.pack(side =TOP)
    pathentry = Entry(root1,textvariable = path_value)
    pathentry.pack(side = TOP,pady = 20,fill = X)
    b1 = Button(text = 'Submit',command = lambda:gpv(path_value,root1))
    b1.pack(side = TOP,pady =20)
    root1.mainloop()
def page3():
    root2 = Tk()
    root2.geometry('1000x800')
    root2.minsize(100,200)
    root2.maxsize(900,200)
    root2.title('This page checks if the previous contents of the folder should be retained or not')
    path_value = StringVar()
    path = Label(root2,text= 'Would you like to delete the previous contents of the folders?',font =('comicsams',20,'bold'),padx=50)
    path.grid(row=0,column=0)
    checkresult = IntVar()
    checkentry = Checkbutton(root2,text ='delete the previous contents?',variable = checkresult)
    checkentry.grid(row=1,column=0)
    b1 = Button(text = 'Submit',command = lambda:cpf(checkresult,root2))
    b1.grid(row=2,column=0,pady=30)
    root2.mainloop()
def page4():
    root3 = Tk()
    root3.geometry('1000x800')
    root3.minsize(100,200)
    root3.maxsize(1100,200)
    root3.title('This page gets the total number of frames that needs to be randomly generated')
    lab = Label(root3,text = f'Please enter the number of images that need to be randomly generated less than {len(store)}',font =('comicsams',16,'bold'))
    lab.pack(side = TOP)
    nFrames = StringVar()
    frame_entry = Entry(root3,textvariable = nFrames)
    frame_entry.pack(pady=20)
    b2 = Button(root3,text = 'Submit',command = lambda:nof(nFrames,root3))
    b2.pack()
    root3.mainloop()
def page5():
    root4 = Tk()
    root4.geometry('1000x800')
    root4.minsize(100,200)
    root4.maxsize(800,800)
    root4.title('This page displays the output and random folders link and also asks if the images needs to be displayed or not')
    t = Label(root4,text = 'Do you want to view the images generated at random ?',font = ('comicsams',20,'bold'))
    t.pack(side = TOP,pady=40)
    viewimages = IntVar()
    b1 = Checkbutton(root4,text = 'check if you want to see the images',borderwidth=7,variable= viewimages)
    b1.pack(side=TOP,padx=0,pady =20)
    b2 = Button(root4,text = 'Submit',command = lambda:vri(viewimages,root4))
    b2.pack(side = TOP,padx=0,pady=10)
    temp_label = Label(root4,text = 'Click the below link to see all the frames of given video')
    temp_label.pack(pady=30)
    lbl = Label(root4, text=outputpath, fg="blue", cursor="hand2")
    lbl.pack(pady=20)
    temp_label1= Label(root4,text = 'Click the below link to see all the frames of given video')
    temp_label1.pack(pady=30)
    lb2 = Label(root4, text=randompath, fg="blue", cursor="hand2")
    lb2.pack(pady=20)
    lbl.bind("<Button-1>", lambda e: callback(outputpath))
    lb2.bind("<Button-1>", lambda e: callback(randompath))
    root4.mainloop()
def page6(files,nFrames):
    l=[]
    for j in range(nFrames):
        try:
            i = random.choice(files)
            l.append(i)
        except IndexError:
            print('the contents are of the random folder are empty')
    root5 = Tk()
    root5.geometry('1920x1080')
    root5.minsize(100,200)
    root5.maxsize(1920,1080)
    root5.title('This page displays the random images')
    t=1
    r=1
    for i in l:
        img = Image.open(i)
        img = img.resize((100,100))
        img = ImageTk.PhotoImage(img)
        e1 = Label(root5)
        e1.grid(row=r,column=t)
        e1.image=img
        e1['image']=img
        t+=1
        if t==12:
            r+=1
            t=1
    b1 = Button(root5,text = 'Close',command = root5.destroy)
    b1.grid(column=3)
    root5.mainloop()   
def vri(viewimages,root4):
    g = viewimages.get()
    with open('temp.txt','w') as file:
        file.write(str(g))
    return root4.destroy() 
def callback(url):
    webbrowser.open_new(url)
def nof(nFrames,root3):
    g = nFrames.get()
    with open('temp.txt','w') as file:
        file.write(str(g))
    return root3.destroy()
    
def cpf(checkresult,root2):
    g = checkresult.get()
    with open('temp.txt','w') as file:
        file.write(str(g))
    return root2.destroy()  
def gvs(getresult,root):
    g = getresult.get()
    with open('temp.txt','w') as file:
        file.write(str(g))
    return root.destroy()
def gpv(path_value,root1):
    g = path_value.get()
    with open('temp.txt','w') as file:
        file.write(g)
    return root1.destroy()  
    
def delete_folders(folder_path):
    try:
        os.chdir(folder_path)
        temp_path  = folder_path
        shutil.rmtree(temp_path+'output')
        shutil.rmtree(temp_path+'random')        
    except OSError:
        print('invalid path')
    except FileNotFoundError:
        print('File might have already been deleted')
def create_folder():
    try:
        if not os.path.exists('output'):
            os.makedirs('output')
        if not os.path.exists('random'):
            os.makedirs('random')
    except OSError:
            print('something went wrong while creating the folders')
def take_input(path):
    folder_path =''
    input_folder_path =path
    temp = input_folder_path.split('\\')
    for i in temp:
        if '.mp4' not in i:
            folder_path=folder_path+i+'\\'  
    try:
        os.chdir(folder_path)
    except FileNotFoundError:
        return -1,0
    except OSError:
        return -1,0
    return folder_path,input_folder_path
def read_video_get_frames(pos=1):
    flag=1
    frame_count=pos
    store_img=[]
    cap = cv2.VideoCapture(input_folder_path)
    while True:
        success,img = cap.read()
        if success:
            name = os.getcwd() +'\\output\\'+ str(frame_count) + '.jpg'
            cv2.imwrite(name,img)
            store_img.append(img)
            frame_count+=1
        else:
            if len(store_img)==0:
                print('unable to read the video')
                flag=0
            break
    if flag==1:
        return store_img
def get_random_frames(store_img,frames,pos=0):
    n = frames
    frame_count=pos+1
    for i in range(n):
            temp = random.choice(store_img)
            name = os.getcwd() +'\\random\\'+str(frame_count)+'.jpg'
            cv2.imwrite(name,temp)
            random_store.append(name)
            frame_count+=1

page1()

k=0
random_store = []
with open('temp.txt','r') as file:
    if int(file.read())==1:
        page2()
        
    else:
        k =-1
if k!=-1:
    with open('temp.txt','r') as file:
        path = file.read()
       
    folder_path,input_folder_path = take_input(path)
   
    if folder_path !=-1:
        page3()
        with open('temp.txt','r') as file:
            if int(file.read())==1:
                check = 'y'
            else:
                check ='n'
        
        if check.lower() == 'y':
                delete_folders(folder_path)
                create_folder()
                store = read_video_get_frames()
                page4()
                with open('temp.txt','r') as file:
                    try:
                        n = int(file.read())
                    except ValueError:
                        n=1
               
                get_random_frames(store,n)
                outputpath = folder_path +'output'
                randompath = folder_path +'random'
                page5()
                output_files = [(x[0], x[2]) for x in os.walk(folder_path+'\\'+'output')]
                random_files = [(x[0], x[2]) for x in os.walk(folder_path+'\\'+'random')]
                with open('temp.txt','r') as file:
                    n1 = int(file.read())
                if n1==1:
                    page6(random_store,n)
        else:
            os.chdir(folder_path)
            
            if not os.path.exists(folder_path+'\\'+'output'):
                os.makedirs('output')
            if not os.path.exists(folder_path+'\\'+'random'):
                os.makedirs('random')
            output_files = [(x[0], x[2]) for x in os.walk(folder_path+'\\'+'output')]
            
            if len(output_files[0][1])==0:
                store = read_video_get_frames() 
                page4()
                with open('temp.txt','r') as file:
                    try:
                        n = int(file.read())
                    except ValueError:
                        n=1
                get_random_frames(store,n)
                random_files = [(x[0], x[2]) for x in os.walk(folder_path+'\\'+'random')]
                outputpath = folder_path +'output'
                randompath = folder_path +'random'
                page5()  
                with open('temp.txt','r') as file:
                    n1= int(file.read())
                if n1==1:
                    page6(random_store,n)
            else:   
                l=[]
                temp=''
                output_files = [(x[0], x[2]) for x in os.walk(folder_path+'\\'+'output')]
                for i in output_files[0][1]:
                    temp = i.split('.')
                    l.append(int(temp[0]))
                starting_outputfiles = max(l)
                random_files = [(x[0], x[2]) for x in os.walk(folder_path+'\\'+'random')]
                l = []
                for i in random_files[0][1]:
                    temp = i.split('.')
                    l.append(int(temp[0]))
                starting_randomfiles = max(l)
                store = read_video_get_frames(starting_outputfiles)
                page4()
                with open('temp.txt','r') as file:
                    try:
                        n = int(file.read())
                    except ValueError:
                        n=1
                get_random_frames(store,n,starting_randomfiles)
                outputpath = folder_path +'output'
                randompath = folder_path +'random'
                page5()
                with open('temp.txt','r') as file:
                    n1 = int(file.read())
                if n1==1:
                    page6(random_store,n)
    else:
        print('Invaid Path')