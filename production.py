ascii_art_dict = {
    'A': r"""
  X   
 X X  
XXXXX 
X   X 
X   X 
""",
    'B': r"""
XXXX  
X   X 
XXXX  
X   X 
XXXX  
""",
    'C': r"""
 XXX  
X     
X     
X     
 XXX  
""",
    'D': r"""
XXXX  
X   X 
X   X 
X   X 
XXXX  
""",
    'E': r"""
XXXXX 
X     
XXXXX 
X     
XXXXX 
""",
    'F': r"""
XXXXX 
X     
XXXX  
X     
X     
""",
    'G': r"""
 XXX  
X     
X  XX 
X   X 
 XXX  
""",
    'H': r"""
X   X 
X   X 
XXXXX 
X   X 
X   X 
""",
    'I': r"""
XXXXX 
  X   
  X   
  X   
XXXXX 
""",
    'J': r"""
 XXXX 
   X  
   X  
X  X  
 XX   
""",
    'K': r"""
X   X 
X  X  
XX    
X  X  
X   X 
""",
    'L': r"""
X     
X     
X     
X     
XXXXX 
""",
    'M': r"""
X   X 
XX XX 
X X X 
X   X 
X   X 
""",
    'N': r"""
X   X 
XX  X 
X X X 
X  XX 
X   X 
""",
    'O': r"""
 XXX  
X   X 
X   X 
X   X 
 XXX  
""",
    'P': r"""
XXXX  
X   X 
XXXX  
X     
X     
""",
    'Q': r"""
 XXX  
X   X 
X   X 
X  XX 
 XXXX 
    X
""",
    'R': r"""
XXXX  
X   X 
XXXX  
X  X  
X   X 
""",
    'S': r"""
 XXX  
X     
 XXX  
    X 
XXX   
""",
    'T': r"""
XXXXX 
  X   
  X   
  X   
  X   
""",
    'U': r"""
X   X 
X   X 
X   X 
X   X 
 XXX  
""",
    'V': r"""
X   X 
X   X 
X   X 
 X X  
  X   
""",
    'W': r"""
X   X 
X   X 
X X X 
XX XX 
X   X 
""",
    'X': r"""
X   X 
 X X  
  X   
 X X  
X   X 
""",
    'Y': r"""
X   X 
 X X  
  X   
  X  
  X   
""",
    'Z': r"""
XXXXX 
   X  
  X   
 X    
XXXXX 
""",
    '0': r"""
 XXX  
X   X 
X  XX 
X X X 
X   X 
 XXX  
""",
    '1': r"""
  X   
 XX   
  X   
  X   
XXXXX 
""",
    '2': r"""
 XXX  
X   X 
   X  
  X   
XXXXX 
""",
    '3': r"""
XXXX  
   X  
 XXX  
   X  
XXXX  
""",
    '4': r"""
  XX  
 X X  
XXXXX 
   X  
   X  
""", 
    '5': r"""
XXXXX 
X     
XXXX  
    X 
XXXX  
""",
    '6': r"""
 XXX  
X     
XXXX  
X   X 
 XXX  
""",
    '7': r"""
XXXXX 
   X  
  X   
 X    
X     
""",
    '8': r"""
 XXX  
X   X 
 XXX  
X   X 
 XXX  
""",
    '9': r"""
 XXX  
X   X 
 XXXX 
    X 
 XXX  
""",

    '/': r"""
    X 
   X  
  X   
 X    
X     
""",
    '*': r"""
X X X 
 X X  
X X X 
 X X  
X X X 
""",
    '!': r"""
  X   
  X   
  X   
      
  X   
""",


    ' ': r"""
      
      
      
      
      
"""

}

if __name__ == "__main__":
    user_input = input("Entrez le texte que vous souhaitez convertir en ASCII art : ").upper()
    char_1 = ''
    char_2 = ''
    char_3 = ''
    char_4 = ''
    char_5 = ''  
    for char in user_input:
        char_1 = char_1 + ascii_art_dict[char][1:7]
        char_2 = char_2 + ascii_art_dict[char][8:14]
        char_3 = char_3 + ascii_art_dict[char][15:21]
        char_4 = char_4 + ascii_art_dict[char][22:28]
        char_5 = char_5 + ascii_art_dict[char][29:35]
    print( char_1)
    print(char_2)
    print(char_3)
    print(char_4)
    print(char_5)
