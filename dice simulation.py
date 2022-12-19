import random
import matplotlib.pyplot as plt
import matplotlib.image as img


while True:

    print("Do you want to roll the dice(s)?")
    n=int(input("1.Yes         2.No\n"))
    if n==1:
        n2=int(input("How many dice do you want to roll?\n"))
        for a in range(0,n2):

            dice=random.randint(1,6)
            print(dice)
            if dice==1:

                image = img.imread("1.png")
                plt.imshow(image)
                plt.show()
            elif dice==2:
                image = img.imread("2.png")
                plt.imshow(image)
                plt.show()
            elif dice==3:
                image = img.imread("3.png")
                plt.imshow(image)
                plt.show()
            elif dice==4:
                image = img.imread("4.png")
                plt.imshow(image)
                plt.show()
            elif dice==5:
                image = img.imread("5.png")
                plt.imshow(image)
                plt.show()
            else:
                image = img.imread("6.png")
                plt.imshow(image)
                plt.show()
    else:
        print("Exiting the game")
        break
