import unittest                    
import filecmp                     
from concordance import *          
                                   
                                   
class TestList(unittest.TestCase): 

    def test_dict(self):                                            
        """running the stop file should be an empty file"""         
        conc = Concordance()                                        
        conc.load_stop_table("stop_words.txt")                      
        conc.load_concordance_table("dict.txt")                     
        conc.write_concordance("dict_con.txt")                      


                                      
if __name__ == '__main__':            
    unittest.main()                   
                                      




