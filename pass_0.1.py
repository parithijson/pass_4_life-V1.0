"""
MIT License

Copyright (c) 2021 PARITHI_POTTER

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
import os
import random
from time import sleep
import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)

# plz don't touch this part
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "[]{}()*;:/_-"
ap = "a1Ab2Bc3Cd4De5Ef6Fg7Gh8Hi9Ij0Jk9Kl8Lm7Mn6No5Op4Pq3Qr2Rs1St0Tu1Uv2Vw3Wx4Xy5Yz6Z"
alll = "a1A[]b2B{}c3C/d4D/e5E-f6F_g7G=h8H@i9I#j0J$k9K%l8L^m7M&n6N*o5O'p4P'q3Q.r2R:s1S|t0T{u1U}v2V[w3W]x4X_y5Y-z6Z!"
alsy = "aA[]bB{}cC/dD/eE-fF_gG=hH@iI#jJ$kK%lL^mM&nN*oO'pP'qQ.rR:sS|tT{uU}vV[wW]xX_yY-zZ!"
# upper,lower
# lower,upper,num
# num
# aphanum
# alphasy
# numsym
lowup = lower + upper
alpha = lowup + numbers
num = numbers
nusy = numbers + symbols
all1 = lowup + alpha + num + alsy + nusy
print(Fore.CYAN + Style.BRIGHT + "\n           Hey Thanks for choosing Brainless's \"Pass_gen\"")
print(Fore.YELLOW + "\n  Its a Random password generator developed in Python 3 by parithipotter")

print(Fore.RED + Style.BRIGHT + "           ______________________________________________")
sleep(2)
length = 0
com = 0


# this is a main program
def main():
    global length, com
    print(f"{Style.BRIGHT}\n  !! The length of password should be within 50 !!")
    try:
        length = int(input(Fore.MAGENTA + '\tEnter the password length: '))
    except ValueError:
        print(f"{Fore.RED}{Style.BRIGHT}\n  !!!!! This should be in Numbers(integers) !!!!!")
        main()
        mat()
        loop()


def mat():
    global com
    if 4 <= length < 50:
        sleep(1)
        print("\n" + Back.BLACK + Style.BRIGHT + "\tCombinations :-")
        print(Fore.RED + Style.BRIGHT + "\t__________________")

        print(
            f"{Fore.BLUE}{Style.BRIGHT}\n	-> Alphabets[1]{Fore.MAGENTA}{Style.BRIGHT}\n	-> Alphanumeric[2]{Fore.YELLOW}{Style.BRIGHT}\n	-> Numbers[3]{Fore.WHITE}{Style.BRIGHT}\n	-> Alphabets_with_symbols[4]{Fore.GREEN}{Style.BRIGHT}\n	-> Numbers&Symbols[5]{Fore.LIGHTRED_EX}{Style.BRIGHT}\n	-> All[0]{Fore.RESET}")

        try:

            com = int(input(Fore.MAGENTA + "\nSelect the any one of the combinations Eg:1 : "))
        except ValueError:
            print(f"{Fore.RED}{Style.BRIGHT}\n!!!!!   Use above numeric options to select combinations   !!!!!")
            mat()
            loop()

        # Nested Function for generating animation
        def hi():
            print(f"{Fore.LIGHTRED_EX}\nGenerating Your Password  ", end='', flush=True)
            for x in range(5):
                for frame in r'-\|/-\|/':
                    print('\b', frame, sep='', end='', flush=True)
                    sleep(0.1)

        if com == 1:
            hi()
            lowup1 = "".join(random.sample(lowup, length))
            print(f"{Fore.RED}\n	Password : ", Fore.GREEN + Style.BRIGHT + lowup1)
            print(f"{Fore.YELLOW}\tNote it!! Highly Confidential!!")
        elif com == 2:
            hi()
            alphaum = "".join(random.sample(ap, length))
            print(f"{Fore.RED}\n	Password : ", Fore.GREEN + Style.BRIGHT + alphaum)
            print(f"{Fore.YELLOW}\tNote it!! and try to remember!!")
        elif com == 3:
            hi()
            num1 = "".join(random.sample(num, length))
            print(f"{Fore.RED}\n	Password : ", Fore.GREEN + Style.BRIGHT + num1)
            print(f"{Fore.YELLOW}\tNote it!! Don't Share!!")
        elif com == 4:
            hi()
            sy = "".join(random.sample(alsy, length))
            print(f"{Fore.RED}\n	Password : ", Fore.GREEN + Style.BRIGHT + sy)
            print(f"{Fore.YELLOW}\tNote it!! Don't show!!")
        elif com == 5:
            hi()
            nu = "".join(random.sample(nusy, length))
            print(f"{Fore.RED}\n	Password : ", Fore.GREEN + Style.BRIGHT + nu)
            print(f"{Fore.YELLOW}\tNote it!! I, didn't noted :-( !! ")
        elif com == 0:
            hi()
            ai = "".join(random.sample(alll, length))
            print(f"{Fore.RED}\n	Password : ", Fore.GREEN + Style.BRIGHT + ai)
            print(f"{Fore.YELLOW}\tNote it!! its secure!! ")
        else:

            print(f"{Fore.RED}{Style.BRIGHT}\n  !! Select the appropriate value. !!")
            mat()

    else:
        print(f"{Fore.RED}{Style.BRIGHT}\n  !! The Length should be 4 to 50!!")
        main()
        mat()
        loop()


# ____________________________________________
# this is resume looping
def loop():
    # noinspection PyGlobalUndefined
    con = input(f"{Fore.MAGENTA}\nAre you want to continue (yes/no) : ")
    # noinspection PyUnboundLocalVariable
    if con == 'yes':
        os.system('clear')
        main()
        mat()
        loop()

    elif con == 'no':
        print(f"\n{Fore.CYAN}{Back.BLACK}Thanks for Using :-) \"Pass_gen\" support \"Brainless\" ")
    else:
        print(f"{Fore.RED}\n!! Type 'yes'  for continue  and 'no' for quit. !!")
        loop()


main()
mat()
loop()

# thanks for using
