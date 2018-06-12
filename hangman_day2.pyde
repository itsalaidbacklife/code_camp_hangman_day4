def setup():
    size(1000, 1000)
    global show_guy, guesses
    show_guy = False
    guesses = []
def draw():
    # Draw gallows
    background(150)
    fill(255)
    strokeWeight(7)
    line(200, 800, 800, 800)
    line(500, 800, 500, 200)
    line(500, 200, 300, 200)
    line(300, 200, 300, 300)
    
    global show_guy
    if show_guy:
        # Draw guy
        ellipse(300, 350, 100, 100) #head
        line(300, 400, 300, 650) #body
        line(300, 500, 200, 350)#left arm
        line(300, 500, 400, 350) #right arm
        line(300, 650, 200, 750)#left leg
        line(300, 650, 400, 750) #right leg
        # Frowny Face
        noFill()
        arc(300, 400, 50, 50, PI+PI/6, 2*PI - PI/6)
        ellipse(280, 340, 20, 20)
        ellipse(320, 340, 20, 20)
        
    # Display guessed letters
    textSize(18)
    text("Guesses:", 0, 50)
    for index, letter in enumerate(guesses):
        text(letter, index*25, 100)
    
def mousePressed():
    global show_guy
    show_guy = not show_guy
    
def keyPressed():
    global guesses
    guesses.append(key)