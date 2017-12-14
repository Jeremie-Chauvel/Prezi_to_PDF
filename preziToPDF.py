print("How to use ?")
try :
    import pyautogui, time
    import os
    import random
    import string
    from PyPDF2 import PdfFileWriter, PdfFileReader
except:
    print("You need pyautogui and PyPDF2")
print("This script assume that you use one screen (for multi-screen you need to tweark it)")
print("1- Go on prezi\n2- Open your presentation >edition mode< \n3- Come back to this script\n4- Press enter")
def combine(dirpath):
    listeOfFiles = os.listdir(dirpath)
    print("number of files : "+str(len(listeOfFiles)))
    output = PdfFileWriter()
    for fileNumber in range(len(listeOfFiles)):
        inputFile = PdfFileReader(open(os.path.join(dirpath,'image'+str(1+fileNumber)+".pdf"),"rb"))
        output.addPage(inputFile.getPage(0))
    outStream = open("SlidesFromPrezi.pdf","wb")
    output.write(outStream)
    outStream.close()

input()
pyautogui.PAUSE = 0.1 
pyautogui.FAILSAFE = True
pyautogui.keyDown('altleft')
time.sleep(0.5)
pyautogui.press('tab')
time.sleep(0.5)
pyautogui.keyUp('altleft')
time.sleep(2)
#a=pyautogui.locateOnScreen('click.png')
#if a != None:
#    print("Slides found")
#else:
#    raise Exception("Can't find presentation make sur your presentation is open")
#
#
#pyautogui.click(pyautogui.center(a))
pyautogui.hotkey('ctrl','p')
time.sleep(2)

pyautogui.typewrite(['left'])
im = pyautogui.screenshot()
width, height = im.size
imPart = im.crop((0,0,2,2))
pyautogui.moveTo(width, 0)
time.sleep(5)
index = 1
directory = os.path.join(''.join([random.choice(string.ascii_letters + string.digits) for n in range(32)]),'')
try:
    os.mkdir(directory)
    while imPart != pyautogui.screenshot().crop((0,0,width,height)):
        print("getting slide number : "+str(index))
        imPart = pyautogui.screenshot().crop((0,0,width,height))
        imPart.save(os.path.join(directory,'image'+str(index)+'.pdf'))
        index+=1
        pyautogui.typewrite(['right'])
        imPart_1 = imPart
        while imPart_1 != pyautogui.screenshot().crop((0,0,width,height)):
            imPart_1 = pyautogui.screenshot().crop((0,0,width,height))
            time.sleep(0.2)
    
    
    pyautogui.press('esc')
    combine(directory)
except KeyboardInterrupt:
    print('KeyboardInterrup')
listFiles=os.listdir(directory)
for path in os.listdir(directory):
    os.remove(os.path.join(directory, path))
os.rmdir(directory)
