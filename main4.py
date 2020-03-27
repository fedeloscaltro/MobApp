import kivy
from kivy.app import App  # makes all the graphics
from kivy.uix.widget import Widget
# from kivy.properties import ObjectProperty
from kivy.graphics import Rectangle
from kivy.graphics import Color
from kivy.graphics import Line

from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


class MainWindow(Screen):
    pass


class SecondWindow(Screen):
    pass


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("my4.kv")


class Touch(Widget):
    # btn = ObjectProperty(None)
    def __init__(self, **kwargs):
        super(Touch, self).__init__(**kwargs)

        with self.canvas:
            Line(points=(20, 40, 400, 500, 60, 500))
            Color(1, 0, 0, .5, mode='rgba')
            self.rect = Rectangle(pos=(0, 0), size=(50, 50))

    def on_touch_down(self, touch):
        self.rect.pos = touch.pos
        print("Mouse down", touch)
        # self.btn.opacity = 0.5

    def on_touch_move(self, touch):
        self.rect.pos = touch.pos
        print("Mouse move", touch)

    # def on_touch_up(self, touch):
    #    print("Mouse up", touch)
    #    self.btn.opacity = 1


class MyApp4(App):  # inheritance from App
    def build(self):
        return kv


if __name__ == '__main__':
    MyApp4().run()
