import sys
import socket
from gtts import gTTS


class voicegen:
    def __init__(self, text, filename, lang='en'):
        if not self.check_internet_connection():
            print('You are not connected to the internet!')
            return
        filename = filename + '.mp3'

        # Render teks ke dalam file MP3
        tts = gTTS(text, lang=lang)
        tts.save(filename)

    def check_internet_connection(self):
        try:
            # Mencoba membuat koneksi ke DNS Google pada port 53, timeout 3 detik
            socket.create_connection(("8.8.8.8", 53), timeout=3)
            return True
        except socket.error:
            return False

def main():
    try:
        if len(sys.argv) < 3 or sys.argv[1] == '--help':
            print("\n"*3)
            print('Voice Generator\n')
            print('Usage  : voicegen <text> <filename> optional [lang]\n')
            print('Example: voicegen "Text to speech" "speach name" "id"\n')
            print('         voicegen --help (to show this help message)')
            print("\n"*3)
            sys.exit(0)
        text = sys.argv[1]
        filename = sys.argv[2]
        lang = sys.argv[3] if len(sys.argv) >= 4 else 'en'
        voicegen(text, filename, lang)
    except KeyboardInterrupt:
        print('\nInterrupted by user')
        sys.exit(0)

if __name__ == "__main__":
    main()
