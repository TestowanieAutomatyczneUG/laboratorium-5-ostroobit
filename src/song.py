class Song:
    def __init__(self):
        self.text = []
        with open("src/song_text.txt", "r") as file:
            for line in file:
                if line != "\n":
                    self.text.append(line[:-1])
    
    def get_verse(self, index):
        if index == 1:
            return self.text[0]
        elif index == 2:
            return self.text[1]
        elif index == 3:
            return self.text[2]