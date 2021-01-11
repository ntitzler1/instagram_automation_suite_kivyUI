# import kivy module
import kivy  
# this restrict the kivy version below this kivy version you cannot
# use the app or software
kivy.require("1.9.1") 
 
# base Class of your App inherits from the App class.
# app:always refers to the instance of your application
from kivy.app import App  
# creates the button in kivy if not imported shows the error
from kivy.uix.button import Button 
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

import os



class MyApp(App):
# layout
    def build(self):
        layout = BoxLayout(padding=10, orientation='vertical')
        btn1 = Button(text="Run!",
          background_color =(1, 2, 3, 4))
        btn1.bind(on_press=self.buttonClicked)

        self.lbl1 = Label(text="test")
        layout.add_widget(self.lbl1)

        self.lb2  = Label(text="Client Name", font_size="20sp", pos=(100,100))
        self.clientName = TextInput(text='titzandfriends', multiline=False)
        layout.add_widget(self.lb2)
        layout.add_widget(self.clientName)

        self.lb3  = Label(text="User Name", font_size="20sp", pos=(100,100))
        self.userName = TextInput(text='titzandfriends', multiline=False)
        layout.add_widget(self.lb3)
        layout.add_widget(self.userName)


        self.lb4  = Label(text="Password", font_size="20sp", pos=(100,100))
        self.password = TextInput(text='77Kinder!', multiline=False)
        layout.add_widget(self.lb4)
        layout.add_widget(self.password)
        
        
        self.lb5  = Label(text="File Path", font_size="20sp", pos=(100,100))
        self.fileName = TextInput(text='/companyPages/sothebys.txt', multiline=False)
        layout.add_widget(self.lb5)
        layout.add_widget(self.fileName)
        

        self.lb6  = Label(text="Number to Process", font_size="20sp", pos=(100,100))
        self.numProcess = TextInput(text='100', multiline=False)
        layout.add_widget(self.lb6)
        layout.add_widget(self.numProcess)


        layout.add_widget(btn1)
        return layout

# button click function
    def buttonClicked(self,btn):
        #self.lbl1.text = "Now Running Automation for " + self.fileName.text

        argument = "python3 instaAutomation.py "+str(self.clientName.text) + " " + str(self.userName.text) + " " + str(self.password.text) + " " + str(self.fileName.text) + " " + str(self.numProcess.text) 
        os.system(argument)
        self.lbl1.text = argument



# run app
if __name__ == "__main__":
    MyApp().run()
 # join all items in a list into 1 big string