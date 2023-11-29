#  importing modules
import math
import random
import time
from pprint import pprint
from art1 import logo, logo2, enemy_list
from hero_class import Hero
from enemy_class import Enemy, Boss, enemygen, enemy_attack, first_enemies
import os
from functions_for_the_game import level_generator, gen_character, createClass, typing, clear_screen, battle, game_over, is_dead

def branch_1_decision1():
    typing("You approach Ben...")
    print("")
    print("PREPARE")
    typing("As you were going to touch Ben, he hits you")
    print("")
    gen_character.setHealth(gen_character.getHealth() - 10)
    pprint(vars(gen_character))
    typing("You've been hit by Ben")
    typing("You don't really know what's going on, but you're not on the mood to find out; your nose is bleeding")
    ben = first_enemies("Ben")
    who_died_battle1 = battle(chapter=1, enemygen=ben, gen_character=gen_character)
    game_over(who_died_battle1)
    if who_died_battle1 == True:
        time.sleep(3)
        typing("You're hitting Ben, really hard, you see that he's crying, his face is red, you stop")
        typing("Ben: Why did you do that, you fucking maniac, I always knew you were crazy, you piece of shit")
        typing(
            f"{gen_character.getName()}: Ben, listen, you were acting strange, you were the first one to\nhit me, my nose is bleeding as well...")
        typing(
            f"Ben: You know I work for the guards, you can keep rumbling all you want, you fucker, I will take\nyou where you belong")
        decision_1 = int(input(typing("Continue for chapter 2 (1) / I'm done with the game (2): ")))
        while decision_1 != 1 and decision_1 != 2:
            typing("You need to type '1' or '2', is it that hard?")
            decision_1 = int(input(typing("Continue for chapter 2 (1) / I'm done with the game (2): ")))
        if decision_1 == 1:
            time.sleep(3)
            typing("There's no chapter 2, be grateful I even got this much done...")
        if decision_1 == 2:
            time.sleep(3)
            typing("It's a shame... Game Over")
            exit()

def branch_1_decision2():
    typing("Ben: Ever since I joined the guards, I knew something was wrong")
    typing("Ben: I know I'm not making any sense, but who is this days?")
    typing(f"Ben: You know {gen_character.getName()}, I've been drinking a lot lately, I think I'm really depressed")
    typing("Ben: Wendy is banging a teenage, I've been following her, kinky bitch...")
    typing(f"{gen_character.getName()}: Ben... Why are you saying this?")
    typing("Ben: I'd rather enjoy talking with people at the tavern than having to deal with my problems")
    typing(f"Ben: People like to embrace blindly whatever you put in front of them and I'm not different\nthings like: communism, healthy food trends, catholicism, ballet, driving\ndiets, self-developing, orgies... People gotta\nkeep themselves busy while awaiting dead {gen_character.getName()}...\nI guess we would be better if didn't have free will, that\nway we wouldn't regret our choices.")
    typing(f"Ben: I'm really tired {gen_character.getName()}")
    typing(f"Ben: I'm really tired {gen_character.getName()}")
    typing(f"Ben: I'm planning on killing myself... but I just need to this disease to pass away so that\nI know while I'm gone, I know my family is okay")
    typing(f"You're fucking tired of listening Ben's tragic nonsense, you can't help but hit him...")
    ben = first_enemies("Ben")
    who_died_battle1 = battle(chapter=1, enemygen=ben, gen_character=gen_character)
    game_over(who_died_battle1)
    if who_died_battle1 == True:
        time.sleep(3)
        typing("You're hitting Ben, really hard, you see that he's crying, his face is red, you stop")
        typing(f"{gen_character.getName()}: You're saying nonsense Ben, you know I don't tolerate like that shit")
        typing(f"Ben: Just start cooking something you asshole, I'm starving and sad")
        decision_1 = int(input(typing("Continue for chapter 2 (1) / I'm done with the game (2): ")))
        while decision_1 != 1 and decision_1 != 2:
            typing("You need to type '1' or '2', is it that hard?")
            decision_1 = int(input(typing("Continue for chapter 2 (1) / I'm done with the game (2): ")))
        if decision_1 == 1:
            time.sleep(3)
            typing("There's no chapter 2, be grateful I even got this much done...")
        if decision_1 == 2:
            time.sleep(3)
            typing("It's a shame... Game Over")
            exit()

def branch_1_decision3():
    typing("You start noticing that Ben is still talking, you start panicking because you feel like you're not there")
    typing("You approach Ben...")
    print("PREPARE")
    typing("As you were going to touch Ben, he hits you")
    gen_character.setHealth(gen_character.getHealth() - 10)
    pprint(vars(gen_character))
    typing("You've been hit by Ben")
    typing("You don't really know what's going on, but you're not on the mood to find out; your nose is bleeding")
    ben = first_enemies("Ben")
    who_died_battle1 = battle(chapter=1, enemygen=ben, gen_character=gen_character)
    game_over(who_died_battle1)
    if who_died_battle1  == True:
        time.sleep(3)
        typing("You're hitting Ben, really hard, you see that he's crying, his face is red, you stop")
        typing("Ben: Why did you do that, you fucking maniac, I always knew you were crazy, you piece of shit")
        typing(f"{gen_character.getName()}: Ben, listen, you were acting strange, you were the first one to\nhit me, my nose is bleeding as well...")
        typing(f"Ben: You know I work for the guards, you can keep rumbling all you want, you fucker, I will take\nyou where you belong")
        decision_1 = int(input(typing("Continue for chapter 2 (1) / I'm done with the game (2): ")))
        while decision_1 != 1 and decision_1 != 2:
            typing("You need to type '1' or '2', is it that hard?")
            decision_1 = int(input(typing("Continue for chapter 2 (1) / I'm done with the game (2): ")))
        if decision_1 == 1:
            time.sleep(3)
            typing("There's no chapter 2, be grateful I even got this much done...")
        if decision_1 == 2:
            time.sleep(3)
            typing("It's a shame... Game Over")
            exit()
    
def branch_2():
    typing("You attempt to sleep in more, however a sudden loud knocking on the door wakes you up")
    typing("Pissed off, you wake up and see that someone is knocking on your door")
    typing("You go and check to see who's knocking")
    time.sleep(2.1)
    typing(f"Ben: Hey {gen_character.getName()}, I just wanted to check if you're okay, I heard noises, are you okay?")
    decision_1 = int(input(typing("Yeah, I was snoring(1) / No, I'm not okay(2): ")))
    while decision_1 != 1 and decision_1 != 2:
        typing("You need to type '1' or '2', is it that hard?")
        decision_1 = int(input(typing("Yeah, I was snoring(1) / No, I'm not okay(2): ")))

    if decision_1 == 1:
        # decision if you were snoring
        typing(
            "Ben: I'm pretty sure those were not snoring noises, but anyways, see you man, let me know if there's anything I can help")
        typing(f"{gen_character.getName()}: (Thinking) Sure, fuck off")
        typing(f"You go back to your bed again, you feel tired")
        time.sleep(2)
        typing("Before you touch your bed, you hear someone knocking again")
        typing("You go and see who is this time, and it's again Ben")
        typing(
            f"Ben: Sorry man, I just wanted to see if you still have the honey you borrowed from last\nweek; actually that's why I came, and then I start listening noises")
        typing(f"{gen_character.getName()}: Sure, I think I have it, come in")
        typing("As you let him enter, Ben is a talker, he starts immediately rumbling about some nonsense")
        time.sleep(1.5)
        typing(
            "Ben: You know, the other day in the tavern, I heard a guy talking that all of this world was created for a single person")
        typing(f"{gen_character.getName()}: What do you mean for a single person? Lol")
        time.sleep(1.5)
        typing("Ben: Yes, all of this world is for a single person to grow and mature, that we're all one and the same")
        typing(f"{gen_character.getName()}: I don't follow, but its fine dude, look, I found the honey")
        time.sleep(1.5)
        typing(
            f"Ben: It's quite perturbing actually, for example, let's say for instance, that you die right now, \nthis guy was saying that after you die, you encounter this random dude that makes you live countless lives,\nand the only reason is for you to grow and mature")
        typing(
            f"{gen_character.getName()}: Oh, yeah that way we can all grow and mature, I mean living a lot of lives would make you wiser, don't you think Ben?")
        time.sleep(2)
        typing(
            f"Ben: No, {gen_character.getName()} is only you, there's no one else... is only for you to grow and mature...")
        typing(f"{gen_character.getName()}: That's pretty deep Ben, you should stop going to that tavern dude, Lol")
        time.sleep(2.1)
        typing(f"Ben: You know I like to drink... seeing too many people dying lately just makes me want to drink more")
        typing(f"{gen_character.getName()}: Yeah, I heard... that disease is killing everyone, isn't it?")
        time.sleep(2.1)
        typing(f"Ben: Yeah, I don't know what's happening actually, just seems like a year ago everything was fine...")
        print("\n")
        print("PREPARE...")
        typing("As Ben was talking, you hear someone screaming")
        time.sleep(2.1)
        typing(f"{gen_character.getName()}: Did you hear that?")
        print("\n")
        print("PREPARE...")
        typing(
            f"Ben: Everything was fine... One of the children that died because of the disease, she was friend of my son")
        time.sleep(2.1)
        typing(f"{gen_character.getName()}: Ben, are you not listening?")
        typing(
            f"Ben: My son cried for weeks scared that the disease would kill him as well, dude, even I am scared,\nmy wife told me to calm him down, but dude, I'm fucking scared as well")
        decision_2 = int(
            input(typing("You start to panic, something seems odd(1) / You continue listening to Ben(2): ")))
        while decision_2 != 1 and decision_2 != 2:
            typing(
                f"{decision_2} is not either '1' or '2'... is it that hard to type '1' or '2' {gen_character.getName()}?")
            decision_2 = int(
                input(typing("You start to panic, something seems odd(1)/ You continue listening to Ben(2): ")))
        if decision_2 == 1:
            branch_1_decision3()
        if decision_2 == 2:
            branch_1_decision2()

def branch_1():
    clear_screen()
    typing("You wake up, you see that someone is knocking on your door")
    typing("You go and check to see who's knocking")
    time.sleep(2.1)
    typing(f"Ben: Hey {gen_character.getName()}, I just wanted to check if you're okay, I heard noises, are you okay?")
    decision_1 = int(input(typing("Yeah, I was snoring(1) / No, I'm not okay(2): ")))
    while decision_1 != 1 and decision_1 != 2:
        typing("You need to type '1' or '2', is it that hard?")
        decision_1 = int(input(typing("Yeah, I was snoring(1) / No, I'm not okay(2): ")))

    if decision_1 == 1:
        # decision if you were snoring
        typing("Ben: I'm pretty sure those were not snoring noises, but anyways, see you man, let me know if there's anything I can help")
        typing(f"{gen_character.getName()}: (Thinking) Sure, fuck off")
        typing(f"You go back to your bed again, you feel tired")
        time.sleep(2.1)
        typing("Before you touch your bed, you hear someone knocking again")
        typing("You go and see who is this time, and it's again Ben")
        typing(f"Ben: Sorry man, I just wanted to see if you still have the honey you borrowed from last\nweek; actually that's why I came, and then I start listening noises")
        typing(f"{gen_character.getName()}: Sure, I think I have it, come in")
        typing("As you let him enter, Ben is a talker, he starts immediately rumbling about some nonsense")
        time.sleep(1.5)
        typing("Ben: You know, the other day in the tavern, I heard a guy talking that all of this world was created for a single person")
        typing(f"{gen_character.getName()}: What do you mean for a single person? Lol")
        time.sleep(1.5)
        typing("Ben: Yes, all of this world is for a single person to grow and mature, that we're all one and the same")
        typing(f"{gen_character.getName()}: I don't follow, but its fine dude, look, I found the honey")
        time.sleep(1.5)
        typing(f"Ben: It's quite perturbing actually, for example, let's say for instance, that you die right now, \nthis guy was saying that after you die, you encounter this random dude that makes you live countless lives,\nand the only reason is for you to grow and mature")
        typing(f"{gen_character.getName()}: Oh, yeah that way we can all grow and mature, I mean living a lot of lives would make you wiser, don't you think Ben?")
        time.sleep(2.3)
        typing(f"Ben: No, {gen_character.getName()} is only you, there's no one else... is only for you to grow and mature...")
        typing(f"{gen_character.getName()}: That's pretty deep Ben, you should stop going to that tavern dude, Lol")
        time.sleep(2.1)
        typing(f"Ben: You know I like to drink... seeing too many people dying lately just makes me want to drink more")
        typing(f"{gen_character.getName()}: Yeah, I heard... that disease is killing everyone, isn't it?")
        time.sleep(1.5)
        typing(f"Ben: Yeah, I don't know what's happening actually, just seems like a year ago everything was fine...")
        print("\n")
        print("PREPARE...")
        typing("As Ben was talking, you hear someone screaming")
        time.sleep(2)
        typing(f"{gen_character.getName()}: Did you hear that?")
        print("\n")
        print("PREPARE...")
        typing(f"Ben: Everything was fine... One of the children that died because of the disease, she was friend of my son")
        time.sleep(3)
        typing(f"{gen_character.getName()}: Ben, are you not listening?")
        typing(f"Ben: My son cried for weeks scared that the disease would kill him as well, dude, even I am scared,\nmy wife told me to calm him down, but dude, I'm fucking scared as well")
        decision_2 = int(input(typing("You start to panic, something seems odd(1) / You continue listening to Ben(2): ")))
        while decision_2 != 1 and decision_2 != 2:
            typing(f"{decision_2} is not either '1' or '2'... is it that hard to type '1' or '2' {gen_character.getName()}?")
            decision_2 = int(input(typing("You start to panic, something seems odd(1)/ You continue listening to Ben(2): ")))
        if decision_2 == 1:
            branch_1_decision3()

    else:
        # decision if you're not okay
        typing("Ben: Do you want me to call the guards? The town is not safe lately")
        typing(f"{gen_character.getName()}: Nah I just feel dizzy man, want to come in and grab a bite?")
        time.sleep(3)
        typing("Ben: Sure, I'm starving")
        typing("As you let him enter, Ben is a talker, he starts immediately rumbling about some nonsense")
        time.sleep(2)
        typing("Ben: You know, the other day in the tavern, I heard a guy talking that all of this world was created for a single person")
        typing(f"{gen_character.getName()}: What do you mean for a single person? Lol")
        time.sleep(2)
        typing("Ben: Yes, all of this world is for a single person to grow and mature, that we're all one and the same")
        typing(f"{gen_character.getName()}: I don't follow, but its fine dude, what'd you like to eat?")
        time.sleep(2)
        typing(f"Ben: It's quite perturbing actually, for example, let's say for instance, that you die right now, \nthis guy was saying that after you die, you encounter this random dude that makes you live countless lives,\nAnd the only reason is for you to grow and mature")
        typing(f"{gen_character.getName()}: Oh, yeah that way we can all grow and mature, I mean living a lot of lives would make you wiser, don't you think Ben?")
        time.sleep(4)
        typing(f"Ben: No, {gen_character.getName()} is only you, there's no one else... is only for you to grow and mature...")
        typing(f"{gen_character.getName()}: That's pretty deep Ben, you should stop going to that tavern dude, Lol")
        time.sleep(3)
        typing(f"Ben: You know I like to drink... seeing too many people dying lately just makes me want to drink more")
        typing(f"{gen_character.getName()}: Yeah, I heard... that disease is killing everyone, isn't it?")
        time.sleep(3)
        typing(f"Ben: Yeah, I don't know what's happening actually, just seems like a year ago everything was fine...")
        print("\n")
        print("PREPARE...")
        typing("As Ben was talking, you hear someone screaming")
        time.sleep(3)
        typing(f"{gen_character.getName()}: Did you hear that?")
        print("\n")
        print("PREPARE...")
        typing(f"Ben: Everything was fine... One of the children that died because of the disease, she was friend of my son")
        time.sleep(3)
        typing(f"{gen_character.getName()}: Ben, are you not listening?")
        typing(f"Ben: My son cried for weeks scared that the disease would kill him as well, dude, even I am scared,\nmy wife told me to calm him down, but dude, I'm fucking scared as well")
        decision_2 = int(input(typing("You shake Ben, because he's acting odd(1) / You continue listening to Ben(2): ")))
        while decision_2 != 1 and decision_2 != 2:
            typing(
                f"{decision_2} is not either '1' or '2'... is it that hard to type '1' or '2' {gen_character.getName()}?")
            decision_2 = int(input(typing("You shake Ben, because he's acting odd(1) / You continue listening to Ben(2): ")))

        if decision_2 == 1:
            branch_1_decision1()
        else:
            branch_1_decision2()
        
def chapter1():
    print(enemy_list["chapter1"])
    time.sleep(10)
    clear_screen()
    print(enemy_list["woods"])
    time.sleep(5)
    clear_screen()
    typing("Chapter 1: Woods")
    typing(f"{gen_character.getName()}, this is just the beginning, but remember, it's just you")
    time.sleep(3)
    clear_screen()
    typing("You wake up crying, you don't really know what is going on, you're dizzy, what do you do?")
    decision_1 = int(input(typing("You wake up(1) or do you want to sleep a little bit more(2): ")))
    while decision_1 != 1 and decision_1 != 2:
        typing(f"{decision_1} is not either '1' or '2'... is it that hard to type '1' or '2' {gen_character.getName()}?")
        decision_1 = int(input(typing("You wake up(1) or do you want ot sleep a little bit more(2): ")))

    if decision_1 == 1:
        #follow the plot of the story with 1 when you're waking up
        time.sleep(2)
        branch_1()

    else:
        #follow the plot of the story with 2 if you slept a little bit more
        branch_2()