class Hangman:
    def __init__(self, word):
        self.word = word
        self.correct_guesses = []
        self.incorrect_guesses = []
        self.gameOver = False
        #Initialize correct guesses with blank dashes
        for x in range(len(self.word)):
            self.correct_guesses.append("--")
            
    def guess(self, letter):
        in_word = False
        if letter not in self.incorrect_guesses:
            for index, x in enumerate(self.word):
                if letter == x:
                    self.correct_guesses[index] = letter
                    in_word = True
            if not in_word:
                self.incorrect_guesses.append(letter)
                
    def display(self):
        # Draw gallows
        background(150)
        fill(255)
        strokeWeight(7)
        line(200, 800, 800, 800)
        line(500, 800, 500, 200)
        line(500, 200, 300, 200)
        line(300, 200, 300, 300)
        
        # Draw guy
        if len(self.incorrect_guesses) > 0:
            ellipse(300, 350, 100, 100) #head
            if len(self.incorrect_guesses) > 1:
                line(300, 400, 300, 650) #body
                if len(self.incorrect_guesses) > 2:
                    line(300, 500, 200, 350)#left arm
                    if len(self.incorrect_guesses) > 3:
                        line(300, 500, 400, 350) #right arm
                        if len(self.incorrect_guesses) > 4:
                            line(300, 650, 200, 750)#left leg
                            if len(self.incorrect_guesses) > 5:
                                line(300, 650, 400, 750) #right leg
                                if len(self.incorrect_guesses) > 6:
                                    # Frowny Face
                                    noFill()
                                    arc(300, 400, 50, 50, PI+PI/6, 2*PI - PI/6)
                                    ellipse(280, 340, 20, 20)
                                    ellipse(320, 340, 20, 20)
                                    text("You Lose! The secret word was: %s\n Press any key to restart" %self.word, 500, 300)
                                    self.gameOver = True
        if '--' not in self.correct_guesses:
            text("You Win! Press any key to restart", 500, 300)
            self.gameOver = True
                                    
            
        # Display guessed letters
        textSize(18)
            # Wrong guesses
        text("Wrong Guesses:", 0, 50)
        for index, letter in enumerate(self.incorrect_guesses):
            text(letter, index*25, 100)
            # Right guesses
        for index, letter in enumerate(self.correct_guesses):
            text("Secret Word", 0, 700)
            text(letter, index*25, 800)