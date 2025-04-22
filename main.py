import time, sys, keyboard

record_key = "up" # This is the key that will be either recorded or played back by the program.
trigger_key = "q" # This key is used to start and end the program and cannot be a key registered by Boxel Rebound.
recording = False # If True, the program will record the key presses, otherwise it will play them back.

timestamp = 0
timestamps = [0.9860084056854248, 1.3622310161590576, 1.1661436557769775, 1.267514705657959, 1.1863276958465576, 1.8957114219665527, 1.2910470962524414, 0.9431734085083008, 0.9000339508056641]

def write_key(thingy_data_whaaat):
    global timestamps,timestamp
    t = time.time() # Use 1 recording of the time so that the program stays in step.
    timestamps.append(t - timestamp)
    timestamp = t


if __name__ == "__main__":
    if recording:
        print(f"Recording will begin after you press: '{trigger_key}' and will stop when you press it again.")
        timestamps = []

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
