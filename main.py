import time, sys, os, keyboard

record_key = "up" # This is the key that will be either recorded or played back by the program.
trigger_key = "q" # This key is used to start and end the program and cannot be a key registered by Boxel Rebound.
recording = True # If True, the program will record the key presses, otherwise it will play them back.

start_time = 0
timestamps = [3.7763341999998374, 4.646306399999958, 6.338568199999827, 6.78818739999997, 9.974909399999888, 11.422785499999918, 12.38981160000003, 13.59222520000003, 14.26676499999985, 15.47998349999989, 16.115305199999966, 17.406824499999857, 18.31655899999987, 18.913924799999677, 20.096910799999932, 20.638120399999934, 21.946245799999815, 23.388349099999687, 23.946588799999972, 25.155145100000027, 25.742236000000048, 26.965936600000077, 27.905601500000103, 28.439262999999755, 29.615941399999883, 30.149274299999888, 31.300674900000104, 31.855745299999853, 33.148954199999935, 33.79339469999968, 35.0490907999997, 35.99983239999983, 36.59989760000008, 37.8633520999997, 38.505017699999826, 39.46254169999975, 40.43832049999992, 41.059918299999936, 41.55621489999976, 42.0715852999997, 43.75497319999977, 44.53505499999983, 45.11562409999988, 45.92139959999986, 46.580325999999786, 47.388050399999884, 48.44698749999998, 48.98648000000003, 49.47398669999984, 51.199275699999816, 51.93942310000011, 52.607601599999725, 53.33883059999971, 54.090664299999844, 54.78144569999995, 55.25058020000006, 55.81322730000011, 56.27167809999992, 56.99620109999978, 58.639052399999855, 59.07282439999972, 59.89914869999984, 61.05565660000002, 61.79944010000008, 64.23044690000006, 64.70779719999973, 65.21640099999968, 66.37224809999998, 67.58258269999988, 70.9267034999998, 73.07233719999977, 73.53349299999991, 74.06245409999974, 75.03827060000003, 77.2855110999999, 78.74330439999994, 81.18077829999993, 81.8540450999999, 82.47219859999996, 84.14651559999993, 84.830019, 85.50041119999969, 86.95571029999974, 87.63836559999982, 88.29033579999987]
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
