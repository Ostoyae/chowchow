from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import models
import api

kv_text = '''
<CustLabel@Label>
    color: 0, 3, 0, 1
    hint_size_x: .5
    text_size: self.size
    paddings: 10
    spacings: 10
    height: self.texture_size[1]

<MyScreenManager>:
    HomeScreen:

<HomeScreen>:
    on_enter: root.callback()
    BoxLayout:
        orientation: "vertical"
        sizing: 10
        padding: 40
        BoxLayout:
            size_hint: 1,.1
            orientation: "horizontal"
            Button:
                text:"Hate it"
            Button:
                text:"Love it"
        ScrollView:
            GridLayout:
                orientation: "vertical"
                size_hint_y: None
                height: self.minimum_height 
                row_default_height: 60
                cols:1
                Label:
                    text: root.recipe.title
                    bold:True
                    font_size:18
                Label:
                    text: "Cook in:" + " " + str(root.recipe.cook_in_min)
                    bold:True
                    font_size:18
                Label:
                    text: "Type of dish:" + " " + root.recipe.dish_type[0]
                    bold:True
                    font_size:18
                Label:
                    text: root.recipe.image_url
                    bold:True
                    font_size:18
                Label:
                    text: "Summary: " + "    " + root.recipe.description
                    bold:True
                    font_size:18
                    text_size: self.width, None
                    size_hint: 1, None
                    height: self.texture_size[1]
                Button:
                    text : "Next"
                    on_press: root.next_recipe()
'''


class MyScreenManager(ScreenManager):
    pass

class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)
    recipes = [value for value in models.storage.all().values()]
    recipe = recipes[0]
    print(recipe)


    def next_recipe(self):
        try:
            del self.recipes[0]
            self.recipe = self.recipes[0]
            HomeScreen.do_layout(self)
            print("hello")
            print(self.recipe)
        except Exception as e:
            print(e)
            print("fails")
            self.recipe = self.recipes[0]

class MyApp(App):
    def build(self):
        return HomeScreen()

def main():
    Builder.load_string(kv_text)
    app = MyApp()
    app.run()

if __name__ == '__main__':
    main()