import time, sys, keyboard

record_key = "up" # This is the key that will be either recorded or played back by the program.
trigger_key = "q" # This key is used to start and end the program and cannot be a key registered by Boxel Rebound.
recording = False # If True, the program will record the key presses, otherwise it will play them back.

timestamp = 0
timestamps = [0.7613341808319092, 0.7608239650726318, 0.9649488925933838, 3.307446002960205, 1.5021884441375732, 0.8427848815917969, 0.8084704875946045, 0.7449967861175537, 1.0090446472167969, 0.7854504585266113, 0.597069501876831, 0.5920851230621338, 0.764451265335083, 0.8824634552001953]

def write_key(thingy_data_whaaat):
    global timestamps,timestamp
    t = time.time() # Use 1 recording of the time so that the program stays in step.
    timestamps.append(t - timestamp)
    timestamp = t


if __name__ == "__main__":
    if recording:
        print(f"Recording will begin after you press: '{trigger_key}' and will stop when you press it again.")

        keyboard.wait(trigger_key)
        print("Recording...")
        keyboard.on_press_key(record_key, write_key)

        # Initialise the timestamp with the current time.
        timestamp = time.time()

        # When the trigger key is pressed again remove all keybindings and exit the program.
        keyboard.wait(trigger_key)
        keyboard.unhook_all()
        print(f"Here are your times: {timestamps}")
        sys.exit()
    else:
        print(f"Playback will begin after you press: '{trigger_key}' and will finish either when the file ends or if terminated with the same key.")
        keyboard.wait(trigger_key)
        print("Playing...")
        keyboard.on_press_key(trigger_key, lambda:(keyboard.unhook_all(),print("Bye"),sys.exit()))
        for i in timestamps:
            time.sleep(i)
            keyboard.press(record_key)
        print("Finished")
