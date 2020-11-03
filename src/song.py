class Song:
    def __init__(self):
        self.text = []
        with open("src/song_text.txt", "r") as file:
            for line in file:
                if line != "\n":
                    self.text.append(line[:-1])
    
    def get_verse(self, index):
        return self.text[index - 1]
    
    def get_verses(self, index1, index2):
        if index1 == index2:
            return self.get_verse(index1)
        return self.text[index1 - 1 : index2 ]