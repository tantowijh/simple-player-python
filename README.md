# Simple Player

The `AudioPlayer` module allows you to play audio files using the `soundfile` and `sounddevice` libraries.

<br>

## Installation

You can install the module using pip:

```
pip install simpleplayer
```

<br>

## Terminal Usage

You can also use the module directly from the terminal:
```
simpleplayer path/to/your/audio/file.wav
```

## Usage

Import the `AudioPlayer` class from the `simpleplayer` module:

```python
from simpleplayer import AudioPlayer
```

Create an instance of the AudioPlayer class, providing the filename of the audio file as a parameter:

```python
player = AudioPlayer('path/to/your/audio/file.wav')
```

Replace 'path/to/your/audio/file.wav' with the actual path to your audio file.

<br>

## Play Audio

To start playing the audio, call the play() method:

```python
player.play()
```

<br>

## Pause and Resume

You can pause the audio playback by calling the pause() method:

```python
player.pause()
```

To resume the playback, call the resume() method:
        
```python
player.resume()
```

<br>

## Stop Audio

To stop the audio playback, use the stop() method:
    
```python
player.stop()
```

<br>

## Example

Here's an example that demonstrates the usage of the AudioPlayer module:
    
```python
from simpleplayer import AudioPlayer

# Create an instance of AudioPlayer
player = AudioPlayer('path/to/your/audio/file.wav')

# Start playing the audio
player.play()
player.wait()

# Perform actions or wait for the audio to finish

# Pause the audio playback
player.pause()

# Resume the audio playback
player.resume()

# Stop the audio playback
player.stop()

```

Remember to replace 'path/to/your/audio/file.wav' with the actual path to your audio file.

<br>

## Simple Player Example

```python
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
```
