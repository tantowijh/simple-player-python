import time
from test import AudioPlayer

class AudioMenu:
    def __init__(self):
        self.player = None

    def display_menu(self):
        print("1. Load audio file")
        print("2. Play audio")
        print("3. Pause audio")
        print("4. Resume audio")
        print("5. Stop audio")
        print("6. Exit")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")

            if choice == "1":
                filename = input("Enter the audio file path: ")
                self.player = AudioPlayer(filename)
                print("Audio file loaded.")

            elif choice == "2":
                if self.player is not None:
                    self.player.play()
                    print("Audio playback started.")
                else:
                    print("No audio file loaded.")

            elif choice == "3":
                if self.player is not None:
                    self.player.pause()
                    print("Audio playback paused.")
                else:
                    print("No audio file loaded.")

            elif choice == "4":
                if self.player is not None:
                    self.player.resume()
                    print("Audio playback resumed.")
                else:
                    print("No audio file loaded.")

            elif choice == "5":
                if self.player is not None:
                    self.player.stop()
                    print("Audio playback stopped.")
                    self.player = None
                else:
                    print("No audio file loaded.")

            elif choice == "6":
                break

            else:
                print("Invalid choice. Please try again.")

            time.sleep(1)  # Add a small delay to allow time for audio operations to take effect

# Create an instance of AudioMenu and run the menu
menu = AudioMenu()
menu.run()