def transcribe(c):
        """Converts a string c from the function
           nucleotide to its complementary RNA nucleotide
        """
        # dictionary with each conversion
        conversion = { 'A':'U', 'C':'G', 'G':'C', 'T':'A' }
        #
        # check if the index, c[0], is a key in the dictionary
        if c[0] in conversion:        # if c[0] is in the dictionary
            new = conversion[c[0]]
            
            return conversion[c[0]]+ transcribe(c[1:])   # if so, return its value
        else:                      # otherwise
            return ''     # return the empty string and check other index
        
        
              
print( "transcribe('ACGTTGCA')  should be  'UGCAACGU' :",  transcribe('ACGTTGCA') )

