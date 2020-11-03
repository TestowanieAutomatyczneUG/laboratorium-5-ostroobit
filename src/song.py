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