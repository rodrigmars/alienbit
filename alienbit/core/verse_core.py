from random import randrange, choice

def get_estrategy():
    return {"economy":choice(["strong", "weak", "average"]),
    "coin": randrange(1000, 9000),
    "economy_": choice([[.1, 25], [.1, 25], [.1, 25]]),
    "percent": choice([0.5, 1.5, 3.1, 5.4, 8.9])}

def hard_verse(economy:str):

    def x_play(x):
        def y_stop(y:list):
            def z_pause(z):
                return "teste"
            return z_pause
        return y_stop
    return x_play

