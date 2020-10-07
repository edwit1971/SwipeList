##################################################
##################################################

from kivy.properties import StringProperty

from kivy.core.window import Window

from kivymd.app         import MDApp
from kivymd.uix.list    import MDList
from kivymd.uix.list    import OneLineListItem
from kivymd.uix.card    import MDCardSwipe
from kivymd.uix.card    import MDCardSwipeLayerBox
from kivymd.uix.card    import MDCardSwipeFrontBox
from kivymd.uix.button  import MDIconButton
from kivymd.uix.toolbar import MDToolbar
from kivymd.uix.floatlayout import MDFloatLayout

from kivy.uix.scrollview     import ScrollView
from kivy.uix.relativelayout import RelativeLayout

##################################################
##################################################

class SwipeToDeleteItem(MDCardSwipe):
    text = StringProperty()
    
    def __init__(self, pText='', pSelf=None, **kwargs):
        super(SwipeToDeleteItem, self).__init__(**kwargs)
        self.LayerBox = MDCardSwipeLayerBox()
        self.FrontBox = MDCardSwipeFrontBox()
        self.OneLItem = OneLineListItem()
        self.BIcon = MDIconButton(icon = 'trash-can')
        self.Str = pText
        self.TestCardSelf = pSelf
        return
        
    def Swipe_Init(self):
        ########################
        self.LayerBox.padding = 8
        if(self.LayerBox.parent == None):
            self.add_widget(self.LayerBox)
        ########################
        if(self.FrontBox.parent == None):
            self.add_widget(self.FrontBox)
        ########################
        self.OneLItem.text = self.Str
        self.OneLItem._no_ripple_effect = True
        if(self.OneLItem.parent == None):
            self.FrontBox.add_widget(self.OneLItem)
        ########################
        self.BIcon.pos_hint = {"center_y": .5}
        if(self.BIcon.parent == None):
            self.LayerBox.add_widget(self.BIcon)
        ########################
        self.size_hint_y = None
        self.height = self.OneLItem.height
        ########################
        self.BIcon.bind(on_release = self.Remove_Trash)
        ########################
        return
    
    def Remove_Trash(self, instance):
        TestCard.remove_item(self=self.TestCardSelf, instance=self)
        return

##################################################
##################################################

class TestCard(MDApp):
    
    #########################################
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        ########################
        self.ReLay_Scr1   = RelativeLayout()
        self.Scr_View1    = ScrollView()
        self.List_Scroll1 = MDList()
        ########################
        self.ToolBar1 = MDToolbar()
        self.Screen1  = MDFloatLayout()
        ########################
        
    #########################################
    def build(self):
        self.Build_MD_List()
        return self.Screen1

    #########################################
    def remove_item(self=None, instance=None):
        if(instance != None):
            self.List_Scroll1.remove_widget(instance)

    #########################################
    def Build_MD_List(self):
        #####################################
        self.ToolBar1.elevation = 10
        self.ToolBar1.title = 'MDCardSwipe'
        self.ToolBar1.y = int(Window.height * 0.9)
        #####################################
        Width35 = int(Window.width * 0.35)
        Width10 = int(Window.width * 0.10)
        Height1 = int(Window.height * 0.5)
        ######
        Scr1_Width  = Width35
        Scr1_Height = Height1
        Scr1_Xo     = Width10
        Scr1_Yo     = int(Window.height * 0.25)
        #####################################
        self.List_Scroll1.padding  = 10
        self.Scr_View1.scroll_type = ['content']
        self.ReLay_Scr1.size_hint  = (None, None)
        self.ReLay_Scr1.width      = Scr1_Width
        self.ReLay_Scr1.height     = Scr1_Height
        self.ReLay_Scr1.x          = Scr1_Xo
        self.ReLay_Scr1.y          = Scr1_Yo
        #####################################\
        for i in range(20):
            item_num = SwipeToDeleteItem(pText = f"One-line item {i}", \
                                         pSelf = self)
            item_num.Swipe_Init()
            self.List_Scroll1.add_widget(item_num)
        #####################################
        if(self.List_Scroll1.parent == None):
            self.Scr_View1.add_widget(self.List_Scroll1)
        if(self.Scr_View1.parent == None):
            self.ReLay_Scr1.add_widget(self.Scr_View1)
        if(self.ReLay_Scr1.parent == None):
            self.Screen1.add_widget(self.ReLay_Scr1)
        if(self.ToolBar1.parent == None):
            self.Screen1.add_widget(self.ToolBar1)
        #####################################
        return
    
TestCard().run()

##################################################
##################################################

