class TextState:
    def __init__(self):
        self.current_text = ""
        self.processed_text = ""
        self.augmented_text = ""

    def reset(self):
        self.__init__() 