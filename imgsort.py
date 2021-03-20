import os
import json
import shutil
import tkinter as tk
from tkinter import *
from PIL import ImageTk,Image
from datetime import datetime

imgsorticon = "imgsort.ico"
logoimage = "logo.png"
helpimage = "question.png"

def sortWindow(inp, out, png, jpg, jpeg, gif, bmp, height, width, scaleEnable, delOriginal, dirList):
    
    if not inp.endswith("\\"):
        inp += "\\"
        
    if not out.endswith("\\"):
        out += "\\"
    
    #Tracks what number files is currently being sorted
    count = 1
    
    window = Tk()
    window.iconbitmap(imgsorticon)
    window.title("IMGSort")
    window.geometry("500x500")
    
    #This line makes it so that way the picture scales properly the first time around
    window.update()
    
    for file in dirList:
        
        #Scales the Image to fill the tag window

        image = Image.open(inp+file)
        width, height = image.size
        factor = (width/height)
        
        window_height = int(window.winfo_height()*.75)
        window_width = window.winfo_width()
        
        image = image.resize((int(window_height*factor),(window_height)), Image.ANTIALIAS)
        
        if(int(window_height*factor) > window_width):
            image = image.resize((window_width,int(window_width/factor)),Image.ANTIALIAS)
            
        #Loads widgets into the tag window

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
        
        #This window.quit command breaks the mainloop()
        okButton = Button(buttonFrame, text="OK", command=window.quit)
        okButton.place(anchor='ne', relx=1, rely=0, width=70, height=20)
                       
        window.mainloop()
        
        
        #Moves on to scanning the tags entered by the user
        #This section of code only runs once when the user clicks "OK" on the tag entry screen
        
        
        tags = tagEntry.get()
        
        #Makes it so that if no tags are entered, the file is copied to the directory specified as the output
        if tags == "":
            tags += "?"
    
        
        if(tags != ""):
            tags = tags.replace(" ","")
            tags = tags.replace(".",",")
            tags = tags.lower()
            tags = tags.split(",")
            
            #Checks to see if any of the inputed tags are supertags and then strikes out any duplicate values 
            parsedtags = []
            for tag in tags:
                
                for item in get_json_tags(tag):
                    try:
                        parsedtags.append(item)
                    except:
                        continue
                    
            tags = remove_duplicates(parsedtags)
            
            timeStamp = str(datetime.now().year)+str(datetime.now().month)+str(datetime.now().day)+str(datetime.now().hour)+str(datetime.now().minute)+str(datetime.now().second)+str(datetime.now().microsecond)
            
            for tag in tags:
                
                #This line prevents the software from trying to create a file with reserved characters. If a specific tag consists strictly of
                #reserved characters it will be copied to the root output directory
                
                tag = tag.replace("<","").replace(">","").replace(":","").replace('"',"").replace("/","").replace("|","").replace("?","").replace("*","")
                
                if(os.path.exists(out+tag)==False):
                    os.makedirs(out+tag)
                
                if not os.path.exists(out+tag+"\\"+timeStamp+"."+(file.split(".")[-1])):
                    shutil.copy(inp+file, out+tag+"\\"+timeStamp+"."+(file.split(".")[-1]))
        
        if(delOriginal == True):
            os.remove(inp+file)
        
        count += 1
    
    # Message box for when all files have been scanned/copied
    root = Tk()
    root.withdraw()
    messagebox.showinfo(title="Info", message="All Files Have Been Sorted. View Files At:\n"+str(out))
    exit()

def remove_duplicates(tags:list):
    final_tags = []
    for value in tags:
        if value not in final_tags:
            final_tags.append(value)
    return final_tags


    # This method will take in a string (key:str) and return a list of strings consisting
    # of the original key string alongside any values at key "key:str" in usertags.json
    
    # This funciton allows the user to create their own custom multitags for IMGSort
    # without the need to hardcode checks into the software. If the json file is
    # unloadable, the function will return just the original string. For this to work,
    # supertag.json needs to be in the cwd.

def get_json_tags(key:str):
    
    expanded_keys = []
    
    if not os.path.exists(os.getcwd()+"//supertag.json"):
        expanded_keys.append(key.replace("$",""))
        return expanded_keys
    
    if(len(key) == 0):
        expanded_keys.append("")
        return expanded_keys
    
    if key[0] == '$':
        expanded_keys.append(key.replace("$",""))
        return expanded_keys
    
    #Tries to open the Json file and sees if it's in a valid format
    try:
        openjson = open("supertag.json")
        usertags = json.load(openjson)
        openjson.close()
        
    except:
        print("supertag.json is not readable. Check for syntax and try again.")
        expanded_keys.append(key)
        return expanded_keys
    
    #Adds tags from supertag.json to a list and returns it
    try:
        expanded_keys.append(key)
        if key in usertags:
            for value in (list(usertags.get(key))):
                expanded_keys.append(str(value))
        return expanded_keys
    
    #If there's an error it returns a list containing only the original key.
    except:
        expanded_keys.append(key)
        return expanded_keys
        
            

def fileToList(inp, png, jpg, jpeg, bmp, gif):
    
    #This is the line that adds files to the list of files that will be sorted. Here
    #you can easily add a check to sort a certain way depending on some kind of input.
    
    #We might also wnat to go ahead and make it so that the list of file extensions to
    #use are included in a list, so that way it's more user friendly to call the
    #function down the road. 
    
    dirList = os.listdir(inp)
    masterList = []
    for file in dirList:
        if(file.lower()[-4:] == ".png" and png == True):
            masterList.append(file)
        elif(file.lower()[-4:] == ".jpg" and jpg == True):
            masterList.append(file)
        elif(file.lower()[-5:] == ".jpeg" and jpeg == True):
            masterList.append(file)
        elif(file.lower()[-4:] == ".bmp" and bmp == True):
            masterList.append(file)
        elif(file.lower()[-4:] == ".gif" and gif == True):
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
    
    copyright_Label = Label(optionWindow, text="     © 2020-2021 Robert Sammataro\n\t         Free For Home Use")
    copyright_Label.config(font="Times")
    copyright_Label.place(anchor='ne', relx=.975, rely = .05)
    
    
    inputDirectory_Label = Label(optionWindow, text="Input Directory Location")
    inputDirectory_Label.config(font=("Arial",10))
    inputDirectory_Label.place(anchor='w', relx=.045, rely = .2)
    
    inputDirectory = Entry(optionWindow)
    inputDirectory.configure(font=("Arial",11))
    inputDirectory.place(anchor='w', relx=.05, rely=.25, height=20, width=490)
    inputDirectory.insert(0,r"")
    
    inputBrowse = Button(optionWindow, text="Browse", command=selectInputDirectory)
    inputBrowse.place(anchor='w', relx=.84, rely=.25, height=20, width=70)
    
    outputDirectory_Label = Label(optionWindow, text="Output Directory Location")
    outputDirectory_Label.config(font=("Arial",10))
    outputDirectory_Label.place(anchor='w', relx=.045, rely = .32)
    
    outputDirectory = Entry(optionWindow)
    outputDirectory.configure(font=("Arial",11))
    outputDirectory.place(anchor='w', relx=.05, rely=.37, height=20, width=490)
    outputDirectory.insert(0,r"")
    
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
    
    versionLabel = Label(optionWindow, text = "Version 1.2.2", borderwidth = 1, relief="sunken", width=15, bg="white")
    versionLabel.place(anchor='sw', relx=0, rely=1)
    
    spacerLabel = Label(optionWindow, text = "", borderwidth = 1, relief="sunken", width=100, bg="white")
    spacerLabel.place(anchor='sw', x=108, rely=1)
    
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
    
    closeButton = Button(optionWindow, text="Exit", command=exit)
    closeButton.place(anchor='w', relx=.67, rely=.89, width=75)
    
    mainloop()

if __name__ == "__main__":
    
    optionsWindow()