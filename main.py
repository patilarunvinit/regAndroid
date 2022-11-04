from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty,StringProperty
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout





# class to call the popup function
class PopupWindow(Widget):
    def btn(self):
        popFun()


# class to build GUI for a popup window
class P(FloatLayout):
    pass


# function that displays the content
def popFun():
    show = P()
    window = Popup(title="popup", content=show,
                   size_hint=(None, None), size=(300, 300))
    window.open()




# class to accept sign up info
class signupWindow(Screen):
    name2 = ObjectProperty(None)
    day = ObjectProperty(None)
    month = ObjectProperty(None)
    year = ObjectProperty(None)
    email = ObjectProperty(None)
    def signupbtn(self):

        global name ,date, email1
        name = self.name2.text
        email1=self.email.text
        date = f"{self.day.text}/{self.month.text}/{self.year.text}"

        if self.email.text != "":
                sm.current = 'data'
                self.name2.text = ""
                self.day.text = ""
                self.month.text = ""
                self.year.text = ""
                self.email.text = ""
        else:
            # if values are empty or invalid show pop up
            popFun()


class dataWindow(Screen):
    def on_enter(self):
        name1=name
        date1=date
        email2=email1
        self.ids.name9.text = str(name1)
        self.ids.date9.text = str(date1)
        self.ids.email9.text = str(email2)





# class for managing screens
class windowManager(ScreenManager):
    pass


# kv file
kv = Builder.load_file('apps.kv')
sm = windowManager()

# reading all the data stored
#users = pd.read_csv('apps.csv')

# adding screens

sm.add_widget(signupWindow(name='signup'))
sm.add_widget(dataWindow(name='data'))



# class that builds gui
class loginMain(App):
    def build(self):
        return sm


# driver function
if __name__ == "__main__":
    loginMain().run()
