import serial, sys, threading;
import PySimpleGUI as sg;



def main():
    x = 0;
    y = 1;
    z = 2;
    comPort = "COM3"; #com port that will be used if one is not specified
    baud = 9600; #default baudrate
    if(len(sys.argv) > 1): #accept other com port and baudrate if one is given
        comPort = sys.argv[1];
        if(len(sys.argv) > 2):
            baud = sys.argv[2];
            
    
    sg.theme('DarkAmber'); #UI creation, btw I love PySimpleGUI, check it out if you need UI stuff
    #and you aren't a UI designer and don't wanna fight with tkinter
    windowText = sg.Text("00000000 00000000 00000000")
    layout = [ [windowText]];
    window = sg.Window("Window Title", layout, auto_size_text = True, resizable = True);
            
    serialConn = serial.Serial(comPort,baud, timeout=.1); #creates an object that watches the given port at the given baudrate
    
    while True:
        event, values = window.read(timeout = 0); #UI main loop; timeout = 0 means that this window does not block the thread <3
        if event == sg.WIN_CLOSED:
            break;
        data = serialConn.readline()[:-2] #reads a line; the last byte is a newline character and we don't need it
        if data:
            curStart = 0;
            curEnd = 0;
            curIndex = 0;
            data = str(data)[2:-2]; #data starts out as a byte sequence, this line changes it into a string and removes b' '
            m = [" ", " ", " "];
            for i in range(len(data)):
                if(data[i] == ' '):
                    m[curIndex] = data[curStart:curEnd-1];
                    curStart = curEnd;
                    curIndex+=1;
                curEnd+=1;
            m[z] = data[curStart:];
            print(m[x] + " " + m[y] + " " + m[z]);
            toShow = str(m[x] + " " + m[y] + " " + m[z]);
            windowText.update(value = toShow); #updates UI text 
            
            
    
if __name__ == "__main__":
    main();