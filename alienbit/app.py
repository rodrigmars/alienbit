def hard_verse(track:str):

    def x_play(x):
        def y_stop(y:list):
            def z_pause(z):
                return "teste"
            return z_pause
        return y_stop
    return x_play

if __name__ == "__main__":

    score = hard_verse("sadsa")(25)([.1, 25])(2.5)

    print(score)