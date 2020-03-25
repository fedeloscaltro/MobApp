import kivy
from kivy.app import App  # makes all the graphics

from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty


class MyGrid(Widget):
    name = ObjectProperty(None)
    email = ObjectProperty(None)

    def btn(self):
        print("Name: ", self.name.text, " Email: ", self.email.text)
        self.name.text = ""
        self.email.text = ""


class MyApp2(App):  # inheritance from App
    def build(self):
        return MyGrid()


if __name__ == '__main__':
    MyApp2().run()
