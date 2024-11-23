class Television:
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3
    CURRENT_VOLUME: int = 0

    def __init__(self) -> None:
        """
        Method to set default values of a television object
        """
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = self.MIN_VOLUME
        self.__channel: int = self.MIN_CHANNEL

    def power(self) -> None:
        """
        Method to toggle the power status of a television Object
        """
        self.__status ^= True
        self.CURRENT_VOLUME, self.__volume = self.__volume, self.CURRENT_VOLUME


    def mute(self) -> None:
        """
        Method to toggle the mute status of a television object.
        Saves the volume before television is muted to be displayed
        after television is unmuted.
        """
        if not self.__status:
            return

        self.__muted ^= True
        self.CURRENT_VOLUME, self.__volume = self.__volume, self.CURRENT_VOLUME

    def channel_up(self) -> None:
        """
        Method to increase the channel of a television object.  If the channel
        of the television object is equal to the MAX_CHANNEL class variable after
        increasing the channel, the channel number will wrap around to the MIN_CHANNEL\
        class variable.
        """
        if not self.__status:
            return

        if self.__channel == self.MAX_CHANNEL:
            self.__channel = self.MIN_CHANNEL
        else:
            self.__channel += 1

    def channel_down(self) -> None:
        """
        Method to decrease the channel of a television object.  If the channel
        of the television object is equal to the MIN_CHANNEL class variable after
        decreasing the channel, the channel number will wrap around to the MAX_CHANNEL
        class variable.
        """
        if not self.__status:
            return

        if self.__channel == self.MIN_CHANNEL:
            self.__channel = self.MAX_CHANNEL
        else:
            self.__channel -= 1

    def volume_up(self) -> None:
        """
        Method to increase the volume of a television object.  If the volume
        of the television object is equal to the MAX_VOLUME class variable before
        increasing the volume, the volume will not be increased.
        """
        if not self.__status:
            return

        if self.__muted:
            self.mute()

        if self.__volume == self.MAX_VOLUME:
            return

        self.__volume += 1

    def volume_down(self) -> None:
        """
         Method to decrease the volume of a television object.  If the volume
         of the television object is equal to the MIN_VOLUME class variable before
         decreasing the volume, the volume will not be decreased.
        """
        if not self.__status:
            return

        if self.__muted:
            self.mute()

        if self.__volume == self.MIN_VOLUME:
            return

        self.__volume -= 1

    def __str__(self) -> str:
        """
        Method to access a string representation of a television object
        :return: String representation of the television object
        """
        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'