# Simple Player

The `AudioPlayer` module allows you to play audio files using the `soundfile` and `sounddevice` libraries.

## Installation

You can install the module using pip:

```plaintext
pip install simpleplayer
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

## Play Audio

To start playing the audio, call the play() method:

    ```python
    player.play()
    ```

## Pause and Resume

You can pause the audio playback by calling the pause() method:

    ```python
    player.pause()
    ```

To resume the playback, call the resume() method:
        
    ```python
    player.resume()
    ```

## Stop Audio

To stop the audio playback, use the stop() method:
    
    ```python
    player.stop()
    ```

## Example

Here's an example that demonstrates the usage of the AudioPlayer module:
    
    ```python
    from simpleplayer import AudioPlayer

    # Create an instance of AudioPlayer
    player = AudioPlayer('path/to/your/audio/file.wav')

    # Start playing the audio
    player.play()

    # Perform actions or wait for the audio to finish

    # Pause the audio playback
    player.pause()

    # Resume the audio playback
    player.resume()

    # Stop the audio playback
    player.stop()

    ```

Remember to replace 'path/to/your/audio/file.wav' with the actual path to your audio file.