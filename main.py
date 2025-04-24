import time, sys, os, keyboard

record_key = "up" # This is the key that will be either recorded or played back by the program.
trigger_key = "q" # This key is used to start and end the program and cannot be a key registered by Boxel Rebound.
recording = True # If True, the program will record the key presses, otherwise it will play them back.

start_time = 0
timestamps = [0.6827207000023918, 1.3041474000056041, 1.798270200000843, 2.355487799999537, 3.990442099995562, 4.789909400002216, 5.412814099996467, 6.161928999994416, 6.877343100000871, 7.634098099995754, 8.097202299992205, 8.667540800001007, 9.142353200004436, 9.824183299992]

# 20: [0.7915839999914169, 2.631869499993627, 4.092787599991425, 5.125166300000274, 6.328917899998487, 6.9950744999950984, 8.226053199992748, 8.860056699995766, 10.110228699995787, 11.059896599996137, 11.676495899999281, 12.910312899999553, 13.545494699996198]
# 21: [0.6827207000023918, 1.3041474000056041, 1.798270200000843, 2.355487799999537, 3.990442099995562, 4.789909400002216, 5.412814099996467, 6.161928999994416, 6.877343100000871, 7.634098099995754, 8.097202299992205, 8.667540800001007, 9.142353200004436, 9.824183299992]
recording = len(timestamps)==0 # if there are no timestamps then we should be recording, otherwise we are playing back.

if __name__ == "__main__":
    if recording:
        print(f"Recording will begin after you press: '{trigger_key}' and will stop when you press it again.")
        timestamps = []

        keyboard.wait(trigger_key)
        print("Recording...")
        keyboard.on_press_key(record_key, lambda _:timestamps.append(time.perf_counter() - start_time))

        # Initialise the start_time with the current time.
        start_time = time.perf_counter()

        # When the trigger key is pressed again remove all keybindings and exit the program.
        keyboard.wait(trigger_key)
        keyboard.unhook_all()
        print(f"Here are your times: {timestamps}")
        sys.exit()
    else:
        print(f"Playback will begin after you press: '{trigger_key}' and will finish either when the file ends or if terminated with the same key.")
        keyboard.wait(trigger_key)
        print("Playing...")
        keyboard.on_press_key(trigger_key, lambda _:(keyboard.unhook_all(),print("Bye"),os._exit()))

        start_time = time.perf_counter()
        for i in timestamps:
            while time.perf_counter() - start_time < i:
                pass # TODO: wait for most of the time and then to this for the last little bit
            keyboard.press_and_release(record_key)

        print("Finished")
