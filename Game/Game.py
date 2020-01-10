import time
play = True
door = 0
print("Игра началась!")
print("Перед вами 10 дверей")
while play:
    print("Выберите дверь")
    if door == 0:
        try:
            door = int(input())
        except ValueError as e:
            print("Выберите дверь")
    if door == 1:
        print("За дверью была пустая комната")
        time.sleep(3)
        door = 0
    if door == 2:
        print("За дверью были сокровища! Вы их забирате")
        time.sleep(3)
        door = 0
    if door == 3:
        print("За дверью был огромный паук!\n"
              "Вы умираете")
        time.sleep(2)
        print("Игра окончена")
        play = False
    if door == 4:
        print("Вы увидели призрака и он вселился в вас и спрыгнул с крыши\n"
              "Вы умираете")
        time.sleep(2)
        print("Игра окончена")
        play = False
    if door == 5:
        print("Вы нашли комнату в которой стоит фонтан (зачем не понятно)\nВы попили из него воды(странно но ничего не произошло)")
        door = 0
    if door == 6:
        print("За дверью была пустая комната")
        time.sleep(3)
        door = 0
    if door == 7:
        print("Вы находите выход из этого страшного дома\n"
              "Вы выиграли!")
        time.sleep(3)
        door = 0
        play = False
    if door == 8:
        print("В комнате вы замечаете скелета лежащего на полу, пугаетесь и убегаете")
        time.sleep(2)
        door = 0
    if door == 9:
        print("Вы открываете дверь и в вас прилетает ядовитая стрела\n"
              "Вы умираете")
        time.sleep(2)
        play = False
    if door == 10:
        print("Вы находите огромнейшие запасы еды\n"
              "Через 20 минут вы обжираетесь и помираете\n"
              "Вы умираете")
        time.sleep(2)
        play = False
