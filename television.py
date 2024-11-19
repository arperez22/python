class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3
    CURRENT_VOLUME = 0

    def __init__(self):
        self.__status = False
        self.__muted = False
        self.__volume = self.MIN_VOLUME
        self.__channel = self.MIN_CHANNEL

    def power(self):
        self.__status ^= True
        return

    def mute(self):
        if not self.__status:
            return

        self.__muted ^= True
        self.CURRENT_VOLUME, self.__volume = self.__volume, self.CURRENT_VOLUME

        return

    def channel_up(self):
        if not self.__status:
            return

        if self.__channel == self.MAX_CHANNEL:
            self.__channel = self.MIN_CHANNEL
        else:
            self.__channel += 1

        return

    def channel_down(self):
        if not self.__status:
            return

        if self.__channel == self.MIN_CHANNEL:
            self.__channel = self.MAX_CHANNEL
        else:
            self.__channel -= 1

        return

    def volume_up(self):
        if not self.__status:
            return

        if self.__muted:
            self.mute()

        if self.__volume == self.MAX_VOLUME:
            return

        self.__volume += 1

        return

    def volume_down(self):
        if not self.__status:
            return

        if self.__muted:
            self.mute()

        if self.__volume == self.MIN_VOLUME:
            return

        self.__volume -= 1

        return

    def __str__(self):
        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}.'