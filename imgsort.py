import os
from os import *
import shutil
import tkinter as tk
from tkinter import *
from PIL import ImageTk,Image
from datetime import datetime
from tkinter import filedialog
from tkinter import messagebox

imgsorticon = "imgsort.ico"
logoimage = "logo.png"
helpimage = "question.png"

def sortWindow(inp, out, png, jpg, jpeg, gif, bmp, height, width, scaleEnable, delOriginal, dirList):
    
    count = 1
    
    
    window = Tk()
    window.iconbitmap(imgsorticon)
    window.title("IMGSort")
    window.geometry("500x500")
    
    #This line makes it so that way the picture scales properly the first time around :)
    window.update()
    
    for file in dirList:

        
        

        image = Image.open(inp+'\\'+file)
        width, height = image.size
        factor = (width/height)
        
        window_height = int(window.winfo_height()*.75)
        window_width = window.winfo_width()
        
        image = image.resize((int(window_height*factor),(window_height)), Image.ANTIALIAS)
        
        if(int(window_height*factor) > window_width):
            image = image.resize((window_width,int(window_width/factor)),Image.ANTIALIAS)
            
        
          #Outdated Scaling Technique. Included for reference
        
#         #Portrait
#         if(width<height):
#             image = image.resize((int(350*factor), 350), Image.ANTIALIAS)
#         
#         #Landscape
#         if(width>=height):
#             image = image.resize(((window.winfo_width()),(int((window.winfo_width())/factor))), Image.ANTIALIAS)

        img1 = ImageTk.PhotoImage(image=image)
        label = tk.Label(window, image=img1)
        label.place(anchor='center',relx=.5,rely=.4)     
        
        fileLabel = Label(window, text=("File", str(count), "of", str(len(dirList))))
        fileLabel.place(anchor='n', relx=.5, rely=.91)

        tagLabel = Label(window, text="Enter Tags")
        tagLabel.place(anchor='n', relx=.5, rely=.80)

        buttonFrame = Frame(window, width=245, height=20)
        buttonFrame.place(anchor='n', relx=.5, rely=.87)

        tagEntry = Entry(buttonFrame)
        tagEntry.place(anchor='nw', relx=0, rely=0, width = 175, height=20)
        
        okButton = Button(buttonFrame, text="OK", command=window.quit)
        okButton.place(anchor='ne', relx=1, rely=0, width=70, height=20)
                       
        window.mainloop()
        
        tags = tagEntry.get()
    
        
        if(tags != ""):
            tags = tags.replace(" ","")
            tags = tags.replace(".",",")
            tags = tags.lower()
            tags = tags.split(",")
            timeStamp = str(datetime.now().year)+str(datetime.now().month)+str(datetime.now().day)+str(datetime.now().hour)+str(datetime.now().minute)+str(datetime.now().second)+str(datetime.now().microsecond)
            
            
            ##THIS IS A BRUTE FORCE METHOD. FIND A WAY TO TURN THIS INTO A JSON FILE!
            
            if("lucario" in tags):
                tags.append("pokemon")
                tags.append("canine")
            if("blaziken" in tags):
                tags.append("pokemon")
                tags.append("avian")
            if("zoroark" in tags):
                tags.append("pokemon")
                tags.append("canine")
            if("zeraora" in tags):
                tags.append("pokemon")
                tags.append("feline")
            if("arcanine" in tags):
                tags.append("pokemon")
                tags.append("canine")
            if("lycanroc" in tags):
                tags.append("pokemon")
                tags.append("canine")
            if("braixen" in tags):
                tags.append("pokemon")
                tags.append("canine")
            if("lugia" in tags):
                tags.append("pokemon")
            if("charizard" in tags):
                tags.append("pokemon")
                tags.append("dragon")
                tags.append("scalie")
            if("noivern" in tags):
                tags.append("pokemon")
                tags.append("dragon")
                tags.append("scalie")
            if("garchomp" in tags):
                tags.append("pokemon")
                tags.append("dragon")
                tags.append("scalie")
            if("mienshao" in tags):
                tags.append("pokemon")
            if("floatzel" in tags):
                tags.append("pokemon")
            if("buizel" in tags):
                tags.append("pokemon")
            
            
            for tag in tags:
                
                if(os.path.exists(out+"\\"+tag)==False):
                    os.makedirs(out+"\\"+tag)
                
                if(os.path.exists(out+"\\"+tag+"\\"+timeStamp+"."+(file.split(".")[-1])) == False):
                    shutil.copy(inp+"\\"+file, out+"\\"+tag)
                    os.rename(out+"\\"+tag+"\\"+file, out+"\\"+tag+"\\"+timeStamp+"."+(file.split(".")[-1]))
        
        if(delOriginal == True):
            os.remove(inp+"\\"+file)
        count = count + 1
    
    root = Tk()
    root.withdraw()
    messagebox.showinfo(title="Info", message="All Files Have Been Sorted. View Files At:\n"+str(out))
    quit()
        
        
            

def fileToList(inp, png, jpg, jpeg, bmp, gif):
    dirList = os.listdir(inp)
    masterList = []
    for file in dirList:
        if(file[-4:] == ".png" and png == True):
            masterList.append(file)
        elif(file[-4:] == ".jpg" and jpg == True):
            masterList.append(file)
        elif(file[-5:] == ".jpeg" and jpeg == True):
            masterList.append(file)
        elif(file[-4:] == ".bmp" and bmp == True):
            masterList.append(file)
        elif(file[-4:] == ".gif" and gif == True):
            masterList.append(file)
    return(masterList)
      

def optionsWindow():
    
    def checkValidLocations(inp, out, png, jpg, jpeg, gif, bmp, height, width, scaleEnable, delOriginal):
        
        if(png == False and jpg == False and jpeg == False and gif == False and bmp == False):
            png ==  True
            jpg ==  True
            jpeg ==  True
            gif ==  True
            bmp ==  True
    
        #Checks to ensure valid path for file locations
        if(os.path.exists(inp) == False or os.path.exists(out) == False):
            messagebox.showerror("Location Error", "The path specified does not exist. Please check your\nspelling and try agian.")
        
        #Checks to see if height and width are valid
        if(str(height) != "" and str(width) != ""):
            if(height.isdigit() == False):
                messagebox.showerror("Input Error", "The height or width specified is not valid. Please try again.")
            elif(width.isdigit() == False):
                messagebox.showerror("Input Error", "The height or width specified is not valid. Please try again.")
            elif(int(height) <= 0 or int(height) >= 10000):
                messagebox.showerror("Input Error", "The height and width specified must be less\nthan 10000 px. Please try again.")
            elif(int(width) <= 0 or int(width) >= 10000):
                messagebox.showerror("Input Error", "The height and width specified must be less\nthan 10000 px. Please try again.")
        
        else:
            dirList = fileToList(inp, png, jpg, jpeg, bmp, gif)
            if(len(dirList)==0):
                messagebox.showerror("Source Folder Error", "No valid images could be located in the source\nfolder. Please try again.")
            else:
                optionWindow.destroy()
                sortWindow(inp, out, png, jpg, jpeg, gif, bmp, height, width, scaleEnable, delOriginal, dirList)
        
    def selectInputDirectory():
        filename = filedialog.askdirectory()
        inputDirectory.delete(0,END)
        inputDirectory.insert(0, str(filename).replace("/","\\"))
    
    def selectOutputDirectory():
        filename = filedialog.askdirectory()
        outputDirectory.delete(0,END)
        outputDirectory.insert(0, str(filename).replace("/","\\"))
        
    optionWindow = Tk()
    optionWindow.geometry("600x400")
    optionWindow.title("IMGSort")
    optionWindow.iconbitmap(imgsorticon)
    optionWindow.resizable(False, False)
    
    logo_img = ImageTk.PhotoImage(Image.open(logoimage).resize((200,50),Image.ANTIALIAS))
    logo_label = Label(optionWindow, image=logo_img, width = 200, height = 50)
    logo_label.place(anchor="nw", relx=.025, rely=.025)
    
    copyright_Label = Label(optionWindow, text="     © 2020 Robert Sammataro\n\tFree For Home Use")
    copyright_Label.config(font="Times")
    copyright_Label.place(anchor='ne', relx=.975, rely = .05)
    
    
    inputDirectory_Label = Label(optionWindow, text="Input Directory Location")
    inputDirectory_Label.config(font=("Arial",10))
    inputDirectory_Label.place(anchor='w', relx=.045, rely = .2)
    
    inputDirectory = Entry(optionWindow)
    inputDirectory.configure(font=("Arial",11))
    inputDirectory.place(anchor='w', relx=.05, rely=.25, height=20, width=490)
    inputDirectory.insert(0,r"D:\Robby Sammataro\Downloads\toSort")
    
    inputBrowse = Button(optionWindow, text="Browse", command=selectInputDirectory)
    inputBrowse.place(anchor='w', relx=.84, rely=.25, height=20, width=70)
    
    outputDirectory_Label = Label(optionWindow, text="Output Directory Location")
    outputDirectory_Label.config(font=("Arial",10))
    outputDirectory_Label.place(anchor='w', relx=.045, rely = .32)
    
    outputDirectory = Entry(optionWindow)
    outputDirectory.configure(font=("Arial",11))
    outputDirectory.place(anchor='w', relx=.05, rely=.37, height=20, width=490)
    outputDirectory.insert(0,r"D:\Robby Sammataro\Pictures\GDrive")
    
    outputBrowse = Button(optionWindow, text="Browse", command=selectOutputDirectory)
    outputBrowse.place(anchor='w', relx=.84, rely=.37, height=20, width=70)
    
    fileFormats = LabelFrame(optionWindow, text="Included File Formats", pady=7)
    fileFormats.place(anchor="center", relx=.5, rely=.5)
    
    pngVar = IntVar()
    jpgVar = IntVar()
    jpegVar = IntVar()
    gifVar = IntVar()
    bmpVar = IntVar()
    
    pngButton = Checkbutton(fileFormats, text='.png', variable=pngVar)
    pngButton.grid(row = 0, column = 0, padx=30)
    pngButton.select()
    
    jpgButton = Checkbutton(fileFormats, text='.jpg', variable=jpgVar)
    jpgButton.grid(row = 0, column = 1, padx=30)
    jpgButton.select()
    
    jpegButton = Checkbutton(fileFormats, text='.jpeg', variable=jpegVar)
    jpegButton.grid(row = 0, column = 2, padx=30)
    jpegButton.select()
    
    gifButton = Checkbutton(fileFormats, text='.gif', variable=gifVar)
    gifButton.grid(row = 0, column = 3, padx=30)
    gifButton.select()
    
    bmpButton = Checkbutton(fileFormats, text='.bmp', variable=bmpVar)
    bmpButton.grid(row = 0, column = 4, padx=30)
    bmpButton.select()
    
    advSettings = LabelFrame(optionWindow, text="Advanced Settings", pady=15 , padx=40)
    advSettings.place(anchor="center", relx=.5, rely=.7)
    
    heightEntry = Entry(advSettings)
    heightEntry.config(font=("Arial",11), width=8)
    heightEntry.grid(row=1,column=0,padx=30)
    
    heightLabel = Label(advSettings, text="Height (px)")
    heightLabel.config(font=("Arial",10))
    heightLabel.grid(row=0,column=0,padx=30)
    
    widthEntry = Entry(advSettings)
    widthEntry.config(font=("Arial",11), width=8)
    widthEntry.grid(row=1,column=1,padx=30)
    
    widthLabel = Label(advSettings, text="Width (px)")
    widthLabel.config(font=("Arial",10))
    widthLabel.grid(row=0,column=1,padx=30)
    
    scaleOvr = IntVar()
    delOrig = IntVar()
    
    scaleOverride = Checkbutton(advSettings, text='Override Original Scaling', variable=scaleOvr)
    scaleOverride.grid(row = 0, column = 3, padx=30)
    
    delOriginal = Checkbutton(advSettings, text='Delete Original Image      ', variable=delOrig)
    delOriginal.grid(row = 1, column = 3, padx=30)
    delOriginal.select()
    
    image = Image.open(helpimage)
    image = image.resize((12,12), Image.ANTIALIAS)
    img1 = ImageTk.PhotoImage(image=image)
    label = Button(advSettings, image=img1, command=lambda:messagebox.showinfo(title="Info", message="If both height and width boxes have a valid size then the output images will be forced to have the same resolution. Not recommended to be used with 'Delete Original Image'"))
    label.config(borderwidth=0)
    label.place(anchor='center', relx=.95, rely=.25)
    
    versionLabel = Label(optionWindow, text = "Version 1.2.0", borderwidth = 1, relief="sunken", width=15, bg="white")
    versionLabel.place(anchor='sw', relx=0, rely=1)
    
    spacerLabel = Label(optionWindow, text = "", borderwidth = 1, relief="sunken", width=100, bg="white")
    spacerLabel.place(anchor='sw', x=108, rely=1)
    
    eulaLabel = Label(optionWindow, text = "View EULA", borderwidth = 1, relief="sunken", width=15, bg="white")
    eulaLabel.place(anchor='se', relx=1, rely=1)
    
    runButton = Button(optionWindow, text="Run", command=lambda:checkValidLocations(inputDirectory.get(),      #Directory for the source location
                                                                                    outputDirectory.get(),     #Directory for the destination location
                                                                                    bool(pngVar.get()),        #Yes/No to .png files
                                                                                    bool(jpgVar.get()),        #Yes/No to .jpg files
                                                                                    bool(jpegVar.get()),       #Yes/No to .jpeg files
                                                                                    bool(bmpVar.get()),        #Yes/No to .bmp files
                                                                                    bool(gifVar.get()),        #Yes/No to .gif files 
                                                                                    heightEntry.get(),         #Custom Height Value (May be blank)
                                                                                    widthEntry.get(),          #Custom Width Value (May be Blank) 
                                                                                    bool(scaleOvr.get()),      #Enables custom scaling with heightEntry and widthEntry
                                                                                    bool(delOrig.get())))      #Enables deleting original files
    runButton.place(anchor='w', relx=.84, rely=.89, width=75)
    
    closeButton = Button(optionWindow, text="Exit", command=optionWindow.destroy)
    closeButton.place(anchor='w', relx=.67, rely=.89, width=75)
    
    mainloop()

optionsWindow()