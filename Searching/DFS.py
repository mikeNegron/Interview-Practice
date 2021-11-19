class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        is_permu = False
        
        #First check if it is possible
        if len(s1) == 0 or len(s2) < len(s1):
            return is_permu
        
        else:
            #window sides (height assumed to be 1)
            left, right = 0, 0
            
            #Hashmaps, freq of each char
            s1_f, window = {}, {s2[left]: 1}
            
            #Adding all char fequencies to hashmap
            for i in s1:
                if i not in s1_f:
                    s1_f[i] = 0
                s1_f[i] += 1
                
            #Loop through string 2
            while right < len(s2):
                #Increase window size if condition is met
                if right - left + 1 < len(s1):
                    right += 1
                    
                    #Edge case: If we run out of string
                    if right >= len(s2):
                        return False

                    #Creating s2 hashmap
                    if s2[right] not in window:
                        window[s2[right]] = 0
                    window[s2[right]] += 1
                
                if right - left + 1 == len(s1):
                    #Since this would mean we're done
                    if s1_f == window:
                        return True
                    
                    else:
                        #Think of a window moving along an array, it must be reduced
                        window[s2[left]] -= 1
                        
                        #If amount is 0, remove
                        if window[s2[left]] == 0:
                            window.pop(s2[left])
                            
                        #One step to the right
                        left += 1
                        
		#If we never find a match, exit
        return False