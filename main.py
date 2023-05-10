from sys import argv
# check if arguments are valid before loading everything else
if len(argv) != 3:
   print("Too little/many arguments")
   print("Usage: python3 pbrdr.py <flag> <angle>")
   exit(1)

try:
   angle = int(argv[2])
except:
   print("Angle argument is not an integer")
   exit(1)

if angle < -360 or angle > 360:
   print("Angle argument is out of range -360 to 360")
   exit(1)

from os import system
from subprocess import Popen

def createHyprGradient(colorlist, transparent, angle):
   buffer = []
   for item in colorlist:
      if transparent:
         buffer.append(f"rgba({item}CC) ")
      else:
         buffer.append(f"rgba({item}EE) ")
   buffer.append(f"{angle}deg")
   return buffer

def changeActiveBorder(color):
   buffer = "".join(color)
   Popen(f'hyprctl keyword general:col.active_border "{buffer}"', shell=True)

def changeInactiveBorder(color):
   buffer = "".join(color)
   Popen(f'hyprctl keyword general:col.active_border "{buffer}"', shell=True)

gay = {
   "rainbow": [
      'E50000',
      'FF8D00',
      'FFEE00',
      '028121',
      '004CFF',
      '770088'
      ],
   "transgender": [
      '55CDFD',
      'F6AAB7',
      'FFFFFF',
      'F6AAB7',
      '55CDFD'
   ],
   "nonbinary": [
      'FCF431',
      'FCFCFC',
      '9D59D2',
      '282828'
   ],
   "agender": [
      '000000',
      'BABABA',
      'FFFFFF',
      'BAF484',
      'FFFFFF',
      'BABABA',
      '000000'
   ],
   "queer": [
      'B57FDD',
      'FFFFFF',
      '49821E'
   ],
   "genderfluid": [
      'FE76A2',
      'FFFFFF',
      'BF12D7',
      '000000',
      '303CBE'
   ],
   "bisexual": [
      'D60270',
      '9B4F96',
      '0038A8'
   ],
   "pansexual": [
      'FF1C8D',
      'FFD700',
      '1AB3FF'
   ],
   "polysexual": [
      'F714BA',
      '01D66A',
      '1594F6',
   ],
   "omnisexual": [
      'FE9ACE',
      'FF53BF',
      '200044',
      '6760FE',
      '8EA6FF',
   ],
   "omniromantic": [
      'FEC8E4',
      'FDA1DB',
      '89739A',
      'ABA7FE',
      'BFCEFF',
   ],
   "mlm": [
      '078D70',
      '98E8C1',
      'FFFFFF',
      '7BADE2',
      '3D1A78'
   ],
   "wlw": [
      'D62800',
      'FF9B56',
      'FFFFFF',
      'D462A6',
      'A40062'
   ],
   "abrosexual": [
      '46D294',
      'A3E9CA',
      'FFFFFF',
      'F78BB3',
      'EE1766',
   ],
   "asexual": [
      '000000',
      'A4A4A4',
      'FFFFFF',
      '810081'
   ],
   "aromantic": [
      '3BA740',
      'A8D47A',
      'FFFFFF',
      'ABABAB',
      '000000'
   ],
   "aroace": [
      'E28C00',
      'ECCD00',
      'FFFFFF',
      '62AEDC',
      '203856'
   ],
   "aroace1": [
      '000000',
      '810081',
      'A4A4A4',
      'FFFFFF',
      'A8D47A',
      '3BA740'
   ],
   "aroace2": [
      '3BA740',
      'A8D47A',
      'FFFFFF',
      'ABABAB',
      '000000',
      'A4A4A4',
      'FFFFFF',
      '810081'
   ],
   "autosexual": [
      '99D9EA',
      '7F7F7F'
   ],
   "intergender": [
      '900DC2',
      '900DC2',
      'FFE54F',
      '900DC2',
      '900DC2',
   ],
   "greygender": [
      'B3B3B3',
      'B3B3B3',
      'FFFFFF',
      '062383',
      '062383',
      'FFFFFF',
      '535353',
      '535353',
   ],
   "akiosexual": [
      'F9485E',
      'FEA06A',
      'FEF44C',
      'FFFFFF',
      '000000',
   ],
   "bigender": [
      'C479A2',
      'EDA5CD',
      'D6C7E8',
      'FFFFFF',
      'D6C7E8',
      '9AC7E8',
      '6D82D1',
   ],
   "demigender": [
      '7F7F7F',
      'C4C4C4',
      'FBFF75',
      'FFFFFF',
      'FBFF75',
      'C4C4C4',
      '7F7F7F',
   ],
   "demiboy": [
      '7F7F7F',
      'C4C4C4',
      '9DD7EA',
      'FFFFFF',
      '9DD7EA',
      'C4C4C4',
      '7F7F7F',
   ],
   "demigirl": [
      '7F7F7F',
      'C4C4C4',
      'FDADC8',
      'FFFFFF',
      'FDADC8',
      'C4C4C4',
      '7F7F7F',
   ],
   "transmasc": [
      'FF8ABD',
      'CDF5FE',
      '9AEBFF',
      '74DFFF',
      '9AEBFF',
      'CDF5FE',
      'FF8ABD',
   ],
   "transfem": [
      '73DEFF',
      'FFE2EE',
      'FFB5D6',
      'FF8DC0',
      'FFB5D6',
      'FFE2EE',
      '73DEFF',
   ],
   "genderfaun": [
      'FCD689',
      'FFF09B',
      'FAF9CD',
      'FFFFFF',
      '8EDED9',
      '8CACDE',
      '9782EC'
   ],
   "demifaun": [
      '7F7F7F',
      '7F7F7F',
      'C6C6C6',
      'C6C6C6',
      'FCC688',
      'FFF19C',
      'FFFFFF',
      '8DE0D5',
      '9682EC',
      'C6C6C6',
      'C6C6C6',
      '7F7F7F',
      '7F7F7F',
   ],
   'neutrois':  [
      'FFFFFF',
      '1F9F00',
      '000000'
   ],

   'biromantic':  [
      '8869A5',
      'D8A7D8',
      'FFFFFF',
      'FDB18D',
      '151638',
   ],

   'biromantic1':  [
      '740194',
      'AEB1AA',
      'FFFFFF',
      'AEB1AA',
      '740194',
   ],

   'autoromantic':  [
      '99D9EA',
      '99D9EA',
      '99D9EA',
      '99D9EA',
      '99D9EA',
      '000000',
      '3DA542',
      '3DA542',
      '000000',
      '7F7F7F',
      '7F7F7F',
      '7F7F7F',
      '7F7F7F',
      '7F7F7F',
   ],


   'boyflux':  [
      'E48AE4',
      '9A81B4',
      '55BFAB',
      'FFFFFF',
      'A8A8A8',
      '81D5EF',
      '69ABE5',
      '69ABE5',
      '5276D4',
   ],

   "finsexual":  [
      "B18EDF",
      "D7B1E2",
      "F7CDE9",
      "F39FCE",
      "EA7BB3",
   ],

   'unlabeled':  [
      'EAF8E4',
      'FDFDFB',
      'E1EFF7',
      'F4E2C4'
   ],

   'unlabeled1': [
      '250548',
      'FFFFFF',
      'F7DCDA',
      'EC9BEE',
      '9541FA',
      '7D2557'
   ],

   'pangender':  [
      'FFF798',
      'FEDDCD',
      'FFEBFB',
      'FFFFFF',
      'FFEBFB',
      'FEDDCD',
      'FFF798',
   ],

   'gnc':  [
      '50284d',
      '96467b',
      '5c96f7',
      'ffe6f7',
      '5c96f7',
      '96467b',
      '50284d'
   ],

   'femboy':  [
      "d260a5",
      "e4afcd",
      "fefefe",
      "57cef8",
      "fefefe",
      "e4afcd",
      "d260a5"
   ],

   'tomboy': [
      "2f3fb9",
      "613a03",
      "fefefe",
      "f1a9b7",
      "fefefe",
      "613a03",
      "2f3fb9"
   ],

   'gendervoid' : [
      "081149",
      "4B484B",
      "000000",
      "4B484B",
      "081149"
   ],

   'voidgirl' :  [
      "180827",
      "7A5A8B",
      "E09BED",
      "7A5A8B",
      "180827"
   ],

   'voidboy' :  [
      "0B130C",
      "547655",
      "66B969",
      "547655",
      "0B130C"
   ]
}

if argv[1] not in gay:
   print(f"Flag {argv[1]} not in database")
   print("Flags include: ")
   for key in gay.keys():
      print(f"{key}, ", end="")
   exit(1)

changeActiveBorder(createHyprGradient(gay[argv[1]], False, angle))
changeInactiveBorder(createHyprGradient(gay[argv[1]], True, angle))
