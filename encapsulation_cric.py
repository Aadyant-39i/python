class Cricket:

    def __init__(self, player, score):
        self.__player = player
        self.__score = score

    def set_score(self, new_score):
        if new_score >= 0:              # validation check
            self.__score = new_score
            print(f"Score updated to {self.__score}")
        else:
            print("Score cannot be negative.")   # rejected safely


cricket = Cricket("Rohit", 85)
cricket.set_score(100)     # Score updated to 100
cricket.set_score(-5)      # Score cannot be negative.