# Playblast_Tool
A script for quickly playblasting from multiple cameras in Maya.

I often need to playblast from multiple camera angles for my animation assignments. It's tedious to have to switch to each camera view and go through the same playblast settings just to change the name of the file being exported. I had tried implementing third-party tools, but none of them worked properly. This script was originally written by Kim Maglalang as a UI template for any kind of tool in Maya. I modified it as part of my "Programming in Maya" workshop series with WIA x AM to be a playblast tool.

This script can be added to any Maya shelf and, when clicked on, will cause a window to pop up with a button titled "Playblast". When you click that button, this tool cycles through every camera on it's list and playblasts from according to the settings set up by the user. To create the list of cameras, specify the playblast settings, and set the file names, the user must manually edit the code. You can do so by right-clicking on the script button in the shelf and selecting "Edit".

- You can add cameras to the "listCameras" array on line 43. Make sure to put the exact name of the camera (capitalization does matter in this case) and to put the name in single brackets ''.
- To change where the playblasts are saved and what name they are saved under, replace the filename on line 47 with a new save path that works for your machine.
- To adjust the playblast settings, edit the playblast command on line 48. There are many flags to the playblast command that you can edit according to your liking. Read more about them here: https://help.autodesk.com/cloudhelp/ENU/MayaCRE-Tech-Docs/Commands/playblast.html

See a video demo here: https://youtu.be/FvInZ2Dgfes

Future features:

- Create a UI where users can specify what cameras and settings they want, rather than requiring users to edit the code directly
- Have the tool return to the viewport the user had been in when they called the script, rather than leaving them looking through whichever camera is last on the list to playblast through
