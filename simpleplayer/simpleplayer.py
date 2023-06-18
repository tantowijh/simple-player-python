""""
Module for playing audio files using soundfile and sounddevice.
"""

import soundfile as sf
import sounddevice as sd
import time


class AudioPlayer:
    def __init__(self, filename: str):
        self.filename = filename
        self.data, self.sample_rate = sf.read(filename)
        self.stream = None
        self.paused = False
        self.current_index = 0
        info = sf.info(filename)
        self.duration = info.duration

    def play(self) -> None:
        channels = 1 if self.data.ndim == 1 else self.data.shape[1]
        self.stream = sd.OutputStream(
            samplerate=self.sample_rate,
            channels=channels,
            callback=self._audio_callback
        )
        self.stream.start()


    def _audio_callback(self, outdata, frames, time, status):
        if self.paused:
            outdata.fill(0)  # If paused, output silence
        else:
            remaining_frames = len(self.data) - self.current_index
            if remaining_frames <= frames:
                if self.data.ndim == 1:
                    self.data = self.data.reshape(-1, 1)  # Reshape to (n, 1)
                    outdata[:remaining_frames, :] = self.data[self.current_index:self.current_index+remaining_frames, :]
                else:
                    outdata[:remaining_frames, :] = self.data[self.current_index:self.current_index+remaining_frames, :]
                outdata[remaining_frames:, :] = 0
                self.stop()
            else:
                if self.data.ndim == 1:
                    self.data = self.data.reshape(-1, 1)  # Reshape to (n, 1)
                    outdata[:frames, :] = self.data[self.current_index:self.current_index+frames, :]
                else:
                    outdata[:frames, :] = self.data[self.current_index:self.current_index+frames, :]
                self.current_index += frames

    def pause(self) -> None:
        self.paused = True

    def resume(self) -> None:
        self.paused = False

    def stop(self) -> None:
        if self.stream is not None:
            self.stream.stop()
            self.stream.close()
            self.stream = None
            self.current_index = 0
            self.paused = False

    def wait(self) -> None:
        seconds = int(self.duration)
        time.sleep(seconds)
