class Song:
    def __init__(self):
        self.text = []
        with open("song_text.txt", "r") as file:
            for line in file:
                if line != "\n":
                    self.text.append(line[:-1])
    