import random

# Generate a random semi-reasonable crosshair
def getCrosshair():
    return (
    f"""{_crossHairComment()}\n\n"""
    f"""`"""
    f"""cl_crosshairalpha "{random.randint(128, 255)}"; """
    f"""cl_crosshaircolor "{random.randint(0, 4)}"; """
    f"""cl_crosshairdot "{_percentChance(30)}"; """
    f"""cl_crosshairsize "{random.randint(1, 5)}"; """
    f"""cl_crosshairstyle "4"; """
    f"""cl_crosshairusealpha "1"; """
    f"""cl_crosshairthickness "{random.randint(1, 4) / 2.0}"; """
    f"""cl_fixedcrosshairgap "{random.randint(-5, 2)}"; """
    f"""cl_crosshair_outlinethickness "{random.randint(1, 2) / 2.0}"; """
    f"""cl_crosshair_drawoutline "{_percentChance(30)}"; """
    f"""cl_crosshair_t "{_percentChance(10)}"; """
    f"""hud_showtargetid "{_percentChance(10)}"; """
    f"""`"""
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