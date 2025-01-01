class TV:
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        self.channels = []
        self.volume = 0

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def show_status(self):
        if self.is_on:
           if self.channel_no <= len(self.channels):
                print(f"TV is on, channel {self.channel_no} ({self.channels[self.channel_no - 1]}), , Volume {self.volume}")
           else:
                print(f"TV is on, channel {self.channel_no}, , Volume {self.volume}")
        else:
            print(f"TV is off, Volume {self.volume}")
    
    def set_channel(self, new_channel_no):
        if self.is_on:
            self.channel_no = new_channel_no
        else:
            print("Cannot change channel while the TV is off")


    def set_channels(self, channels_list):
        self.channels = channels_list
        print("Channels updated")

    def show_channels(self):
        if self.channels:
            for i, channel in enumerate(self.channels, start=1):
                print(f"{i}. {channel}")
        else:
            print("No channels are set")
    
    def increase(self):
        if self.volume < 10:
            self.volume += 1
        else:
            print("Volume cannot be increased beyond 10")

    def decrease(self):
        if self.volume >= 0:
            self.volume -= 1
        else:
            print("Volume cannot be decreased below 0")
