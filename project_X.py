import tkinter as tk
from tkinter import ttk
import os, shutil
root =tk.Tk()
root.title("Application for file arrangement")

########################################################################################################################
path_lable = ttk.Label(root,text= "Enter your folder\'s path here:  ")
path_lable.grid(row=1, column=0)

path_var = tk.StringVar()
path_box = ttk.Entry(root, width=100, textvariable = path_var)
path_box.grid(row=1, column=1)

about_label = ttk.Label(root, text= "The owner of this application is  NITISH CHAURASIYA ")
about_label.grid(row=3, columnspan=4)

new_text_var = tk.StringVar()
new_text = ttk.Entry(root,text = "new textfield", textvariable = new_text_var)
new_text.grid(row=3, column=0)





def action():
    path= path_var.get() 
    dict_extension = {
        'audio_extension' : ('.mp3', '.m4a', '.wave', '.flac'),
        'videos_extension' : ('.mp4', '.mkv', '.flv', '.mpeg'),
        'documents_extension' :('.doc','.pdf', '.txt'),
        'image_extension': ('.img','.png','.gif','.jpg','.jpeg')
    }

    
    def file_finder(url,extension):
        files=[]
        for f in os.listdir(url):
            for exe in extension:
                if f.endswith(exe):
                    files.append(f)            
        return files
    




    for exe_type,exe_tupple in dict_extension.items():
        folder_name = exe_type.split('_')[0] +" " + 'Files'
        folder_path = os.path.join(path, folder_name)
        os.mkdir(folder_path)
        for items in (file_finder(path, exe_tupple)):
            itmes_path = os.path.join(path,items)
            shutil.move(itmes_path,folder_path)
    l1=tk.Label(root,text = new_text_var)
    l1.grid(row=4,column = 0)
       

    

ok_button= ttk.Button(root, text= "OK", command=action)
ok_button.grid(row=2, column=1)
##########################################################################################################################

root.mainloop()