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

## [Simple Player Example](https://raw.githubusercontent.com/tantowijh/simple-player-python/main/example.py)

<br>
<br>


# Voice Generator

The `voicegen` module allows you to convert text to speech and save it as an audio file using the `gtts` library.

To use the `voicegen` module, you need to follow these steps:

1. Import the `voicegen` class from the `voicegen` module:

    ```python
    from simpleplayer import voicegen
    ```
2. Create an instance of the voicegen class, providing the text, filename, and an optional language parameter:

    ```python
    voicegen(text, filename, lang='en')
    ```
    Replace text with the text you want to convert to speech, filename with the desired name of the output audio file, and lang with the language code (default is 'en').

3. If the internet connection is available, the text will be converted into speech and saved as an MP3 file with the specified filename.

<br>

Example usage:

```python
from simpleplayer import voicegen

# Generate the voice
voicegen("Hello, world!", "output")
```
This will generate an audio file named output.mp3 containing the speech for the text "Hello, world!".

<br>

## Terminal Usage
You can also use the voicegen module directly from the terminal:
```
voicegen "Hello, world!" output
```

Replace "Hello, world!" with the desired text and output with the desired filename (without the file extension). The generated audio file will be saved as output.mp3 in the current directory.

Note: Ensure that you have a stable internet connection to use the voicegen module successfully.

<br>
<br>

# LICENSE
This project is licensed under the [MIT License](LICENSE) - see the LICENSE file for details.
