import pyray
from game.shared.os_tool import OSTool
from config import *
import pathlib
from game.casting.basics.sound import Sound

class SoundService:

    def __init__(self):
        self._sounds = {}
        self._muted = False
        self._master_volume = 1

    def initialize(self):
        pyray.init_audio_device()

    def release(self):
        pyray.close_audio_device()

    def load_sounds(self, directory):
        filepaths = OSTool.get_filepaths(directory, [".wav", ".mp3", ".wma", ".aac"])
        for filepath in filepaths:
            self._sounds[filepath] = pyray.load_sound(filepath)
    
    def unload_sounds(self):
        for sound in self._sounds.values():
            pyray.unload_sound(sound)
        self._sounds.clear()
    
    def play_sound(self, sound):
        if not isinstance(sound, Sound):
            sound = Sound(sound)
        filepath = str(pathlib.Path(sound.get_filename()))
        
        sound = self._sounds[filepath]
        pyray.play_sound(sound)

    def is_sound_playing(self, sound):
        """Check if a sound is currently playing
        """
        if not isinstance(sound, Sound):
            sound = Sound(sound)
        filepath = str(pathlib.Path(sound.get_filename()))
        sound = self._sounds[filepath]
        return pyray.is_sound_playing(sound)

    def toggle_mute(self):
        self._muted = not self._muted
        if self._muted:
            pyray.set_master_volume(0)
        else:
            pyray.set_master_volume(self._master_volume)

    def increase_volume(self):
        self._master_volume += 0.1
        if self._master_volume > 1:
            self._master_volume = 1
        if not self._muted:
            pyray.set_master_volume(self._master_volume)

    def decrease_volume(self):
        self._master_volume -= 0.1
        if self._master_volume < 0:
            self._master_volume = 0
        if not self._muted:
            pyray.set_master_volume(self._master_volume)
        # CHANGE MASTER VOLUME INSTEAD OF THE BELOW

        # if self._muted:
        #     for sound in self._sounds:
        #         if self.is_sound_playing(sound):
        #             pyray.pause_sound(sound)
        # else:
        #     for sound in self._sounds:
        #         pyray.resume_sound(sound)

    # def play_sound_looped(self, sound):
    #     if not isinstance(sound, Sound):
    #         sound = Sound(sound, .5, True)
    #     filepath = str(pathlib.Path(sound.get_filename()))
    #     sound = self._sounds[filepath]
    #     pyray.play_sound(sound)