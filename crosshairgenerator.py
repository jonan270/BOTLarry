import random

# Get crosshair according to msgContent input
def getCrosshair(msgContent):
    msg = msgContent.lower()
    nWords = len(msgContent.split());

    # msgContent = !crosshair
    if(nWords == 1):
        return _randCrosshair()
    # msgContent = !crosshair *nickname*
    elif(nWords == 2):
        nameFlag = msg.split()[1]
        return _specificCrosshair(nameFlag)
    # msgContent too long
    else:
        return "!crosshair följt av ett namn hade ju vart trevligt."


# Gap beroende på om man har dot
# Generate a random semi-reasonable crosshair
def _randCrosshair():
    useDot = _percentChance(30)

    # Use smaller gaps if no dot
    if(bool(useDot)):
        gap = random.randint(-5, 2)
    else:
        gap = random.randint(-5, -1)


    return (
    f"""{_crossHairComment()}\n\n"""
    f"""`"""
    f"""cl_crosshairalpha "{random.randint(128, 255)}"; """
    f"""cl_crosshaircolor "{random.randint(0, 4)}"; """
    f"""cl_crosshairdot "{useDot}"; """
    f"""cl_crosshairsize "{random.randint(1, 5)}"; """
    f"""cl_crosshairstyle "4"; """
    f"""cl_crosshairusealpha "1"; """
    f"""cl_crosshairthickness "{random.randint(1, 4) / 2.0}"; """
    f"""cl_crosshairgap "{gap}"; """
    f"""cl_fixedcrosshairgap "{gap}"; """
    f"""cl_crosshair_outlinethickness "{random.randint(1, 2) / 2.0}"; """
    f"""cl_crosshair_drawoutline "{_percentChance(30)}"; """
    f"""cl_crosshair_t "{_percentChance(10)}"; """
    f"""hud_showtargetid "{_percentChance(10)}"; """
    f"""`"""
    )

# Try to pick a specific crosshair according to provided name
def _specificCrosshair(name):
    if name in crosshairDictionary:
        return (
            f"""Har hört att {name} blev inspirerad """
            f"""av BOT Larry att köra med denna:\n\n`"""
            f"""{crosshairDictionary[name]}`"""
        )
    else:
        return(
            f"""Vet inte riktigt vem {name} är.. """
            f"""Någon avdankad 1.6 spelare eller?"""
        )

# Pick a random flair comment for top of message
def _crossHairComment():
    comments = [
        f'Det här har jag hittat på alldeles själv, genialiskt!',
        f'Tror aldrig jag träffat någon med det här... Med andra ord är det perfekt!',
        f'Vart ligger !crosshair ?? Oj vänta, hittade det här: ',
        f'Färger har aldrig vart min starka sida men det här är ju sjukt snyggt:',
        f'Den här kallar jag "Jolles special":',
        f'Denna brukar jag köra när jag lirar Negev:',
    ]
    return random.choice(comments)

# Return 1 with a percentage chance, else return 0
def _percentChance(percentage):
    return 1 if random.random() < percentage / 100 else 0


crosshairDictionary = {
    "dev1ce" : 
        f"""cl_crosshair_drawoutline 1; """
        f"""cl_crosshair_outlinethickness 1; """
        f"""cl_crosshaircolor 2; """
        f"""cl_crosshairdot 0; """
        f"""cl_crosshairgap -1; """
        f"""cl_crosshairsize 3; """
        f"""cl_crosshairstyle 4; """
        f"""cl_crosshairthickness 1 """,
    "dupreeh" : 
        f"""cl_crosshair_drawoutline 1; """
        f"""cl_crosshair_outlinethickness 1; """
        f"""cl_crosshaircolor 1; """
        f"""cl_crosshairdot 0; """
        f"""cl_crosshairgap -2; """
        f"""cl_crosshairsize 3; """
        f"""cl_crosshairstyle 4; """
        f"""cl_crosshairthickness 1 """,
    "gla1ve":
        f"""cl_crosshair_drawoutline 0; """
        f"""cl_crosshaircolor 1; """
        f"""cl_crosshairdot 0; """
        f"""cl_crosshairgap -2; """
        f"""cl_crosshairsize 3; """
        f"""cl_crosshairstyle 4; """
        f"""cl_crosshairthickness 1 """,
    "magisk":
        f"""cl_crosshair_drawoutline 1; """
        f"""cl_crosshaircolor 0; """
        f"""cl_crosshairdot 0; """
        f"""cl_crosshairgap -1; """
        f"""cl_crosshairsize 1; """
        f"""cl_crosshairstyle 4; """
        f"""cl_crosshairthickness 0 """,
    "xyp9x":
        f"""cl_crosshair_drawoutline 0; """
        f"""cl_crosshaircolor 1; """
        f"""cl_crosshairdot 0; """
        f"""cl_crosshairgap 0; """
        f"""cl_crosshairsize 5; """
        f"""cl_crosshairstyle 4; """
        f"""cl_crosshairthickness 0.5 """,
    "niko":
        f"""cl_crosshair_drawoutline 1; """
        f"""cl_crosshairalpha 255; """
        f"""cl_crosshaircolor 5; """
        f"""cl_crosshaircolor_b 255; """
        f"""cl_crosshaircolor_g 255; """
        f"""cl_crosshaircolor_r 255; """
        f"""cl_crosshairdot 1; """
        f"""cl_crosshairgap -4; """
        f"""cl_crosshairsize 0; """
        f"""cl_crosshairstyle 4; """
        f"""cl_crosshairthickness 1; """
        f"""cl_crosshair_sniper_width 1; """,
    "coldzera":
        f"""cl_crosshair_drawoutline 0; """
        f"""cl_crosshairalpha 255; """
        f"""cl_crosshaircolor 2; """
        f"""cl_crosshaircolor_b 165; """
        f"""cl_crosshaircolor_g 255; """
        f"""cl_crosshaircolor_r 0; """
        f"""cl_crosshairdot 1; """
        f"""cl_crosshairgap -3; """
        f"""cl_crosshairsize 2; """
        f"""cl_crosshairstyle 4; """
        f"""cl_crosshairthickness 1; """
        f"""cl_crosshair_sniper_width 1;""",
    "s1mple":
        f"""cl_crosshair_drawoutline 0; """
        f"""cl_crosshairalpha 255; """
        f"""cl_crosshaircolor 4; """
        f"""cl_crosshaircolor_b 255; """
        f"""cl_crosshaircolor_g 0; """
        f"""cl_crosshaircolor_r 255; """
        f"""cl_crosshairdot 1; """
        f"""cl_crosshairgap -2; """
        f"""cl_crosshairsize 1; """
        f"""cl_crosshairstyle 5; """
        f"""cl_crosshairthickness 0; """
        f"""cl_crosshair_sniper_width 1; """,
    "m0nesy":
        f"""cl_crosshair_drawoutline 0; """
        f"""cl_crosshairalpha 255; """
        f"""cl_crosshaircolor 4; """
        f"""cl_crosshaircolor_b 2; """
        f"""cl_crosshaircolor_g 255; """
        f"""cl_crosshaircolor_r 255; """
        f"""cl_crosshairdot 255; """
        f"""cl_crosshairgap -3; """
        f"""cl_crosshairsize 2; """
        f"""cl_crosshairstyle 4; """
        f"""cl_crosshairthickness 0; """
        f"""cl_crosshair_sniper_width 1; """,
    "b1t":
        f"""cl_crosshair_drawoutline 0; """
        f"""cl_crosshairalpha 255; """
        f"""cl_crosshaircolor 4; """
        f"""cl_crosshaircolor_b 144; """
        f"""cl_crosshaircolor_g 238; """
        f"""cl_crosshaircolor_r 0; """
        f"""cl_crosshairdot 0; """
        f"""cl_crosshairgap -3; """
        f"""cl_crosshairsize 2; """
        f"""cl_crosshairstyle 4; """
        f"""cl_crosshairthickness 0; """
        f"""cl_crosshair_sniper_width 1; """,
    "xantares":
        f"""cl_crosshair_drawoutline 0; """
        f"""cl_crosshairalpha 255; """
        f"""cl_crosshaircolor 1; """
        f"""cl_crosshaircolor_b 50; """
        f"""cl_crosshaircolor_g 250; """
        f"""cl_crosshaircolor_r 50; """
        f"""cl_crosshairdot 0; """
        f"""cl_crosshairgap 0; """
        f"""cl_crosshairsize 3; """
        f"""cl_crosshairstyle 4; """
        f"""cl_crosshairthickness 0.5; """
        f"""cl_crosshair_sniper_width 1; """,
    "zywoo":
        f"""cl_crosshair_drawoutline 0; """
        f"""cl_crosshairalpha 200; """
        f"""cl_crosshaircolor 1; """
        f"""cl_crosshaircolor_b 50; """
        f"""cl_crosshaircolor_g 250; """
        f"""cl_crosshaircolor_r 50; """
        f"""cl_crosshairdot 0; """
        f"""cl_crosshairgap -3; """
        f"""cl_crosshairsize 1; """
        f"""cl_crosshairstyle 4; """
        f"""cl_crosshairthickness 0; """
        f"""cl_crosshair_sniper_width 1; """,
    "twistzz":
        f"""cl_crosshair_drawoutline 0; """
        f"""cl_crosshairalpha 255; """
        f"""cl_crosshaircolor 4; """
        f"""cl_crosshaircolor_b 255; """
        f"""cl_crosshaircolor_g 255; """
        f"""cl_crosshaircolor_r 255; """
        f"""cl_crosshairdot 0; """
        f"""cl_crosshairgap -2; """
        f"""cl_crosshairsize 1.5; """
        f"""cl_crosshairstyle 4; """
        f"""cl_crosshairthickness 0; """
        f"""cl_crosshair_sniper_width 1; """,
    "ropz":
        f"""cl_crosshair_drawoutline 0; """
        f"""cl_crosshairalpha 255; """
        f"""cl_crosshaircolor 1; """
        f"""cl_crosshaircolor_b -1000; """
        f"""cl_crosshaircolor_g 0; """
        f"""cl_crosshaircolor_r -1000; """
        f"""cl_crosshairdot 0; """
        f"""cl_crosshairgap -3; """
        f"""cl_crosshairsize 2; """
        f"""cl_crosshairstyle 4; """
        f"""cl_crosshairthickness 0; """
        f"""cl_crosshair_sniper_width 1; """,
    
}