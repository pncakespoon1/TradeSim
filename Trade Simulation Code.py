import random
import csv
# chests simulated
chests_simulated=9
# trade requirements
obsidian_requirement=20
pearl_requirement=16
explosive_requirement=5
potion_requirement=1
bed_requirement=1
with open('tradesim_H9.csv', mode='x') as tradesim_H9:
    data_writer = csv.writer(tradesim_H9, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for i in range(100000):
        # chests looted
        chests_looted=chests_simulated
        # items from trades
        obsidian_trades=0
        crying_obsidian_trades=0
        string_trades=0
        glowstone_dust_trades=0
        potion_trades=0
        pearl_trades=0
        # items from chests
        obsidian_chests=0
        crying_obsidian_chests=0
        string_chests=0
        # trade count
        trades=0
        for i in range(chests_simulated):
            rolls=(random.randrange(3,6))
            while rolls > 0:
                choose_item=(random.randrange(1,12))
                if choose_item == 1:
                    obsidian_chests += (random.randrange(4,7))
                if choose_item == 2:
                    crying_obsidian_chests += (random.randrange(1,6))
                if choose_item == 3:
                    string_chests += (random.randrange(4,7))
                rolls -= 1
        while pearl_trades < pearl_requirement or potion_trades < potion_requirement or (obsidian_trades + obsidian_chests) < obsidian_requirement or (glowstone_dust_trades // 16) < (explosive_requirement - ((string_trades + string_chests) // 12)) or ((crying_obsidian_trades + crying_obsidian_chests) // 6) < (explosive_requirement - ((string_trades + string_chests) // 12)) or ((string_trades + string_chests) // 12) < bed_requirement:
            choose_trade=(random.randrange(1,424))
            if choose_trade >= 1 and choose_trade < 21:
                pearl_trades += (random.randrange(4,9))
            if choose_trade >= 21 and choose_trade < 41:
                potion_trades += 1
            if choose_trade >= 41 and choose_trade < 61:
                string_trades += (random.randrange(8,25))
            if choose_trade >= 61 and choose_trade < 81:
                glowstone_dust_trades += (random.randrange(5,13))
            if choose_trade >= 81 and choose_trade < 121:
                obsidian_trades += 1
            if choose_trade >= 121 and choose_trade < 161:
                crying_obsidian_trades += (random.randrange(1,4))
            trades += 1
        data_writer.writerow([trades])