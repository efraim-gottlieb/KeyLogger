from pynput import keyboard
input_keys = []

def check_language(letter):
    print(letter)
    english_l = range(65,90)
    english_s = range(97,122)
    hebrew = range(1488,1514)
    if letter in english_l or letter in english_s:
        return 'en'
    elif letter in hebrew:
        return 'he'
    else:
        pass


def on_press(key):
    try:
        # print(check_language(ord(key.char)))
        print(chr(ord(key.char)))
        input_keys.append(ord(key.char))
        print(input_keys)
    except:
        input_keys.append(str(key))


###     stop monitoring     ###
def on_release(key):
    try:
        show = input_keys[-1] == 'w' and input_keys[-2] == 'o' and input_keys[-3] == 'h' and input_keys[-4] == 's'
        if show:
            input_keys.pop()
            input_keys.pop()
            input_keys.pop()
            input_keys.pop()
            output_text = "".join(input_keys)
            print(output_text)
        ###     pree "c + delete" to stop monitoring       ###
        elif key == keyboard.Key.delete and input_keys[-2] == 'c':
            return False
        else:
            pass
    except:
        pass

###     Collect events until released      ###
with keyboard.Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()
