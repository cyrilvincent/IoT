from stepper import Stepper

in1 = 19
in2 = 18
in3 = 5
in4 = 17
delay = 1 #  mode==1 & delay==1 ne fonctionne pas
mode = 0 # 0 for half step, 1 for full step, 0 est 2x plus lent

def main() -> None:
    s1 = Stepper(in1, in2, in3, in4, delay, mode)
    s1.step(100)
    s1.step(100,-1)
    s1.angle(180)
    s1.angle(360,-1)

if __name__ == "__main__":
    main()