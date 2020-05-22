'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
# global count

def count_th(word):
   
    

    if len(word) == 0: 
        return 0       
    
    else:
        zero = word[0]
       
        if zero == '0': 
            
            return len(word)
            
            
        else:
            th = word[0:2] 
            if th == 'th': 
                word = word + '0'
                print(word)
                # num = int(word[-1]) + 1
                # word + str(num)
                
             
            
    return count_th(word[1:])
        
