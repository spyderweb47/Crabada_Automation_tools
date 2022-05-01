#!/usr/bin/env python3

#headers / Library
import requests
import json
import sys


#Input Variable
mineno=sys.argv[1]


#Global Variables

attackersReinforcement1InfoHasPrinted=False
attackersReinforcement2InfoHasPrinted=False
defendersReinforcement1InfoHasPrinted=False
defendersReinforcement2InfoHasPrinted=False

token = "" # your bot token
chat_id = "" #your id

#Functions
def telegramPrint (msg):
  url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={msg}"
  requests.get(url)
  print(msg)
  print("Message Sent Successfully")

def MineInfo(mineid):
  mine=requests.get(f"https://idle-api.crabada.com/public/idle/mine/{mineid}")
  mine = json.loads(mine.text)
  return mine

def CrabInfo(crabid):
  crab = requests.get(f"https://api.crabada.com/public/crabada/info/{crabid}")
  crab = json.loads(crab.text)
  return crab

def MineAlert(mineid):

  global attackersReinforcement1InfoHasPrinted
  global attackersReinforcement2InfoHasPrinted
  global defendersReinforcement1InfoHasPrinted
  global defendersReinforcement2InfoHasPrinted

  mineCrabs=MineInfo(mineid)
  defenceTeamMembers=mineCrabs["result"]["defense_team_info"]
  attackTeamMembers=mineCrabs["result"]["attack_team_info"]
  winnerteam = mineCrabs["result"]["winner_team_id"]
  # print(len(mineCrabs))

  #defence desicion making
  if len(defenceTeamMembers)== 4:
    if defendersReinforcement1InfoHasPrinted == False:
      telegramPrint (f"{mineno} ::  Defence Reinforced 1")
      defendersReinforcement1InfoHasPrinted = True
    else:
      pass

  elif len(defenceTeamMembers) == 5:
    if defendersReinforcement2InfoHasPrinted == False:
      telegramPrint (f"{mineno} ::  Defence Reinforced 2")
      defendersReinforcement2InfoHasPrinted = True
  else:
    pass


  #attack desicion making
  if len(attackTeamMembers)== 4:
    if attackersReinforcement1InfoHasPrinted == False:
      telegramPrint (f"{mineno} ::  Attack Reinforced 1")
      attackersReinforcement1InfoHasPrinted = True
    else:
      pass
  elif len(defenceTeamMembers) == 5:
    if attackersReinforcement2InfoHasPrinted == False:
      telegramPrint (f"{mineno} ::  Attack Reinforced 2")
      attackersReinforcement2InfoHasPrinted = True
    else:
      pass
  else:
    pass

  # print(type(winnerteam))
  if winnerteam is not None:
    return winnerteam
  else:
    return 0


#Main

# time loop
i=1
while(i==1):
  win=MineAlert(mineno)
  if win != 0:
    telegramPrint(win)
    i=0

