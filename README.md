## IMGSort v1.2.3
Build Date: 20 March 2021  

#### Welcome to IMGSort, the simplest tool for creating image archives!

### How to use:
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
    'Delete Original Image' box. If no destination tags are entered, the files
    will be copied to the absolute path of the output directory (new to v1.2.2)

  - Click "Run" and a window will pop up displaying one image at a time. In the
    box at the bottom, enter the name of the subfolder in the Output Directory
    you would like to send the image to. You may enter multiple subfolders by
    separating tags with a comma or period. Leaving the field empty will skip over the
    displayed image.


### Using Supertags:
  - IMGSort can easily be configured so that entering a certain tag will
    automatically sort the current image to multiple destination instead of  
    having to write in each individual folders name.  

  - To create a supertag, in the supertag.json file, create keys representing  
    the tag you wish to use as a supertag and set its value to a list of  
    strings of folders you would like to output to.  

  - To override a supertag, add a '$' to the beginning of the tag and IMGSort  
    will not send the current image to any of the folders associated with the  
    supertag.

### Tips and Shortcuts:  

  - Entering a question mark (?) as a tag will result in a copy of the current image
    being copied to the output directory's absolute path.  

  - Entering a dollar sign ($) at the beginning of a tag will treat it like a regular tag if it is a supertag.  

### Troubleshooting:

**IMGSort will not launch:**  
Ensure that all assets are in the same folder as IMGSort.py  
These Files include:  
- imgsort.ico
- logo.png
- question.png


**Some images not appearing in the display window:**  
Ensure the desired image is in a compatible file format and that the format
is selected on the main window upon launch.


### Changelog:

### 20 March 2021: v1.2.3

    - Added supertags  

    - Added check_json_tags() (See Using Supertags)  

    - Added remove_duplicates(): This is a more streamlined way of removing  
      repeated values from within a list of tags to be copied.  

    - Added supertag.json  

#### 9 March 2021: v1.2.2  

    - If no tags are entered, the image will be copied to the root directory of  
      the destination folder. If the delete original option is enabled, the  
      original picture will be removed (Undone from v1.2.1)

    - Fixed a bug where entering a character that could not be used as a folder  
      name would cause the program to crash

    - Added better comments explaining the purpose of variables and loops

    - Removed broken EULA button since the license is included in repository

    - Added feature where Entering '?' as a tag will copy the specified image  
      to the absolute path of the output directory

    - Updated Changelog and removed old references to imgsort.exe

#### 8 March 2021: v1.2.1

    - Fixed a bug where filed extensions with upper case letters were not
      being recognized

    - Added feature where the original file will not be erased when no tags are
      entered, even if the 'Delete Original' option is selected

    - Removed tag checks that were originally added for testing and debugging

    - Removed default hard-coded file paths that were originally added for
      testing and debugging

    - Added if __name__ == "__main__": statement so that the script can be
      imported without immediately executing the GUI

    - Updated copyright information to 2020-2021

    - Reformatted README with better markdown and updated information

### Future Additions:
  - Feature where the user can add default Input and Output directories  

  - Feature where the user can send images to multiple folders with one tag  

  - Feature checking to make sure a file will not be overwritten as it is copied  
    (currently not implemented)

### Known Bugs:  
  - If a non-image file has a file extension that IMGSort can recognize, it
    will cause a crash when loaded in  

  - Selecting a folder that doesn't exist will force IMGSort to the tag screen
    after closing out of the error window  


Written in Python 3.7.8  
© 2020-2021 Robert Sammataro  
github.com/robertsammataro  
robbysam@udel.edu  
robertsammataro@gmail.com
