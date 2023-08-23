# Hana Engineers and Consultants
# Hana Maintenance Checklist App 


from kivy.app import App
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.properties import StringProperty
from kivy.uix.slider import Slider 
from kivy.base import runTouchApp

from fpdf import FPDF

from functools import partial

class SayHello(App):
    def build(self):
        
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (.51,.61)
        self.window.pos_hint = {"center_x": 1, "center_y":1}

        #Scrollable View

        # Hana logo widget
        self.window.add_widget(Image(source = "HanaLogo.png"))
    
        

        # Label widgets 1-10

        # 1. Conduction Date of Inspection ***FIRST***
        self.L_date = Label(
                                text="Conducted on",
                                font_size = 18,
                                color = '#f6b26b'
                              )
        self.window.add_widget(self.L_date)

            #text input widget
        self.T_date = TextInput(
                                multiline = False,
                                size_hint = (1, 0.5)
                            )
        self.window.add_widget(self.T_date)


        # 2. Inspection Location
        self.L_location = Label(
                                text="Location",
                                font_size = 18,
                                color = '#f6b26b'
                              )
        self.window.add_widget(self.L_location)

            #text input widget
        self.T_location = TextInput(
                                multiline = False,
                                size_hint = (1, 0.5)
                            )
        self.window.add_widget(self.T_location)

        # 2. Office                                                           **MODIFY (Dropdown Selection) 
        self.L_office = Label(
                                text="Office Name",
                                font_size = 18,
                                color = '#f6b26b'
                              )
        self.window.add_widget(self.L_office)

            #text input widget
        self.T_office = TextInput(
                                multiline = False,
                                size_hint = (1, 0.5)
                            )
        self.window.add_widget(self.T_office)

        # 3. Truck Number                                                           **MODIFY (Dropdown Selection) 
        self.L_truck = Label(
                                text="Truck Number",
                                font_size = 18,
                                color = '#f6b26b'
                              )
        self.window.add_widget(self.L_truck)
                #text input widget
        self.T_truck = TextInput(
                                multiline = False,
                                size_hint = (1, 0.5)
                            )
        self.window.add_widget(self.T_truck)

        # 4. Engine Oil Level                                                        **MODIFY (Dropdown Selection) 
        self.L_oil = Label(
                                text="Engine Oil Level",
                                font_size = 18,
                                color = '#f6b26b'
                              )
        self.window.add_widget(self.L_oil)

            #text input widget
        self.T_oil = TextInput(
                                multiline = False,
                                size_hint = (1, 0.5)
                            )
        self.window.add_widget(self.T_oil)


        self.L_user = Label(
                                text = "Conducted by",
                                font_size = 18,
                                color = '#f6b26b'
                            )
        self.window.add_widget(self.L_user)

        self.T_user = TextInput(
                                multiline = False,
                                size_hint = (1,0.5)
                             )   
        self.window.add_widget(self.T_user)     

        self.button = Button(
                                text = "ENTER",
                                size_hint = (1,0.5),
                                bold = True,
                                background_color = '#f6b26b',
                                background_normal = ""
                            )
        self.button.bind(on_press = self.callback)
        self.window.add_widget(self.button)

        root = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
        root.add_widget(self.window)

        return root    

    def callback(self, event):
        #1.

        self.L_date.text = "Inspection conducted by " + self.T_user.text + " on " + self.T_date.text
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial","B", 12)
        pdf.write(4,self.L_date.text)
        pdf.write(4,self.T_oil.text + "\n"+ self.T_truck.text + "\n" + self.T_office.text)
        pdf.output("file.pdf")

       
        

# run the App

if __name__ == "__main__":
    SayHello().run()