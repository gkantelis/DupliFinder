DupliFinder is a simple, easy-to-use tool designed to help users manage duplicate or near-duplicate files on their local storage. It provides a user-friendly graphical interface to select a directory, finds similar files based on a configurable similarity threshold, and prompts the user to choose which file to delete.

Features
File selection: DupliFinder lets users choose a directory to scan for duplicate files.
Similarity threshold: Users can set the similarity threshold for file name comparison. This threshold can be adjusted using a slider.
Recursive search: DupliFinder searches not only the selected directory but also its subdirectories.
Group similar files: Instead of comparing file names pairwise, DupliFinder groups all similar files together, providing a more efficient way to manage duplicates.
Deletion prompt: When similar files are found, DupliFinder prompts the user to select a file to delete, ensuring user control over file management.
Installation
Download the DupliFinder.zip file from this repository.
Extract the contents of the zip file.
Run the DupliFinder.exe file.
Note: If you are using Python and want to run the Python script directly, you will need Python 3 and the following Python libraries: os, difflib, tkinter, and collections.

Usage
Run DupliFinder.exe.
Click "Select Folder" to choose a directory.
Adjust the similarity threshold as desired.
The program will automatically find similar files in the selected directory and its subdirectories.
When prompted, select a file to delete or choose "None" to keep all files.
Important: Always ensure you have backups of your files when using this program. DupliFinder has the ability to delete files, so use it with care.
