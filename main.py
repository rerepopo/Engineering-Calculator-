import kivy


from kivy.app import App
from kivy.uix.gridlayout import GridLayout

import re

#user_data='(12305+0b0101)*3+3&3|0x4'

def parseandrun(user_data):
   parsed_data=re.split("(\+)|(\-)|(\*)|(\/)|(\()|(\))|(\|)|(\&)",user_data)
   parsed_data=list(filter(None,parsed_data))
   #print (parsed_data)
   
   converted_data=''
   #print (converted_data)
   
   for item in parsed_data:
      if item in ["+","-","*","/","(",")","&","|"]:
         converted_data+=item 
         #print ('operation')
      elif item[:2]=="0b":
          try:
              qq=int(item,2)
              converted_data+=str(qq)
              #print ('binary: '+str(qq))  
          except Exception:
              ##print ('Exception in binary: '+item)
              converted_data='Exception in binary: '+item
              break
      elif item[:2]=="0x":
          try:
              qq=int(item,16)
              converted_data+=str(qq)
              #print ('Hex: '+str(qq))  
          except Exception:
              ##print ('Exception in Hex: '+item)
              converted_data='Exception in Hex: '+item
              break
      else:
          if item.isnumeric():
             #print ('Dec:'+str(item.isnumeric()) )
             converted_data+=item
          else:
             #print ('Dec:'+str(item.isnumeric()) )
             converted_data='Exception in Dec: '+item
   
   #print (user_data)
   #print (converted_data)
   return converted_data

class CalcGridLayout(GridLayout):
 
    # Function called when equals is pressed
    def calculate(self, calculation):
        if calculation:
            try:
                # Solve formula and display it
                temp=parseandrun(calculation)
                if temp.startswith('Exception in binary') or temp.startswith('Exception in Hex') or temp.startswith('Exception in Dec'):
                   self.displaybin.text = temp
                   self.displayhex.text = temp
                   self.displaydec.text = temp
                else:
                   temp=eval(temp)
                   self.displaybin.text = str(bin(temp))
                   self.displayhex.text = '0x'+str(hex(temp).upper())[2:]
                   self.displaydec.text = str(temp)
            except Exception:
                self.display.text = "fail at eval"
    '''def printit(self, message): ############################Learn it
        print (str(message))
    '''

        
class CalculatorApp(App):
    #title = 'CalculatorApp'
    #icon = 'icon.png'
    def build(self):
        return CalcGridLayout()
    
if __name__ == '__main__':
    CalculatorApp().run()
