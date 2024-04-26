s: str = "Amo Roma"

def is_palindrome(s: str) -> bool:

#Restituisce True se s è palindroma; altrimenti restituisce False:
#Ad esempio "Amo Roma" è una stringa palindroma,
# "Ciao come stai?" non è una stringa palindroma.

#Sarebbe return s== s[::-1]

    s: str = s.lower().replace(" ","")

    i: int = 0
    while i < len(s) // 2:
       j = len(s) - (i + 1)
    if s[i] != s[j]:
     return False
    i += 1 
    
    return True

#Oppure:
def is_palindrome2(s: str) -> bool:
    s1: str = ""
    for i in range(len(s)-1,0,-1):
        s1 += s[i]

    for i in range(len(s)):
        if s[i] != s1[i]:
          return False
    return True

