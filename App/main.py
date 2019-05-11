from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.event import EventDispatcher
kv_text = '''

<MyScreenManager>:
    HomeScreen:

<HomeScreen>:
    BoxLayout:
        orientation: "vertical"
        BoxLayout:
            size_hint: 1,.1
            orientation: "horizontal"
            Button:
                text:"2"
            Button:
                text:"3"
        ScrollView:
            GridLayout:
                orientation: "vertical"
                size_hint_y: None
                height: self.minimum_height 
                row_default_height: 60
                cols:1
                
                Label:
                    text: "hello angie"
                Label:
                    text: "hello angie"
                Label:
                    text: "hello angie"
                Label:
                    text: "hello angie"
                Label:
                    text: "hello angie"
                Label:
                    text: "hello angie"
                Label:
                    text: "hello angie"
                Label:
                    text: "hello angie"
                Label:
                    text: "hello angie"
                Label:
                    text: "hello angie"
                Label:
                    text: "hello angie"
                Label:
                    text: "hello angie"
                Label:
                    text: "Attribute a:"
                Label:
                    text: "Ingredients"
                Label:
                    text: root.data_model.a

                
'''


class DataModel(EventDispatcher):
    a = StringProperty('')
    b = StringProperty('')
    c = StringProperty('')

    def __init__(self, *args, **kwargs):
        super(DataModel, self).__init__(*args, **kwargs)
        self.a = 'Ingredient A'
        self.b ='This is b'

class MyScreenManager(ScreenManager):
    pass

class HomeScreen(Screen):
    data_model = ObjectProperty(DataModel())
    dog = StringProperty("dog")

class MyApp(App):
    def build(self):
        return HomeScreen()

def main():
    Builder.load_string(kv_text)
    app = MyApp()
    app.run()

if __name__ == '__main__':
    main()