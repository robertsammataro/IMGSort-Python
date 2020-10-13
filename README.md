IMGSort v1.1  
Generate Archives of Image Files!  
Build Date: 13 October 2020  

Welcome to IMGSort, the simplest tool for creating image archives!

System Requirements:
   - 2GB Memory                          
   - Windows XP Service Pack 3 or Later  
   - 11 MB Available Storage             

Additional Software:  
- IMGSort.exe will run without the need for any additional software. For those
looking to view the raw Python file, ensure you have installed the following
modules to ensure compatibility:  
  - shutil
  - Tkinter
  - Pillow (PIL)
  - datetime

Installation:
There is no requirement for a folder IMGSort must be installed in. To avoid
undesired behavior, ensure that all assets stay in the same folder as
IMGSort.exe.

How to use:
  - Before beginning, ensure that all files you wish to sort are in the same
    directory.
  - Upon launching IMGSort, navigate to the directory where the images to be
    sorted are located in the 'Input Directory Location' field
  - Navigate to the directory where you wish to form your archive in the
    'Output Directory Location' field
  - Select the file formats you wish to include. Currently IMGSort supports
    .png, .jpg, .jpeg, .gif, and .bmp images.
  - If you wish to force all your sorted images to a certain size, enter the
    desired height and width in pixels in the boxes under 'Advanced Settings.'
    NOTE: The forced scaling will not be applied unless 'Override Original
    Scaling' is also selected
  - To delete images from the input directory as they are sorted, click the
    'Delete Original Image' box.
  - Click "Run" and a window will pop up displaying one image at a time. In the
    box at the bottom, enter the name of the subfolder in the Output Directory
    you would like to send the image to. You may enter multiple subfolders by
    separating tags with a comma. Leaving the field empty will skip over the
    displayed image.

Troubleshooting:
  - IMGSort will not launch
      Ensure that all assets are in the same folder as IMGSort.exe. These Files
      include:
        - imgsort.ico
        - logo.png
        - question.png

  - Some images not appearing in the display window
      Ensure the desired image is in a compatible file format and that the format
      is selected on the main window upon launch.

  - Windows Defender or other Antivirus software flags IMGSort as a virus
      Create an exception in your antivirus software allowing IMGSort to run.
      Alternatively, you may also run the IMGSort.py script in the Python
      IDE of your choice which is identical in execution to the .exe

    
  If these solutions do not help, launch the file from the command prompt to
  receive more detailed error information.


  Written in Python 3.7.7  
  GUI Handled by Tkinter  
  EXE compiled with PyInstaller v4.0  
  (C) 2020 Robert Sammataro  
  robertsammataro@gmail.com
