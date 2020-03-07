import widgets
from widgets import clock, widget
from clock import time_widget
from widget import rb_widget

def widget_dispatch(st,layout,widget, default_widget):
    # if st == 'Totalisateur' :
    #     return odo_widget(layout,widget)
    # elif st == 'Trip1' :
    #     default_widget = widget
    #     return trip1_widget(layout,widget)
    # elif st == 'Trip2' :
    #     if default_widget == 7 :
    #         default_widget = widget
    #     return trip2_widget(layout,widget)
    # elif st == 'Vitesse' :
    #     return speed_widget(layout,widget)
    # elif st == 'Vmoy1' :
    #     return vmoy1_widget(layout,widget)
    # elif st == 'Vmoy2' :
    #     return vmoy2_widget(layout,widget)
    # elif st == 'Vmax1' :
    #     return vmax1_widget(layout,widget)
    # elif st == 'Vmax2' :
    #     return vmax2_widget(layout,widget)
    # elif st == 'Chrono1' :
    #     return chrono1_widget(layout,widget)
    # elif st == 'Chrono2' :
    #     return chrono2_widget(layout,widget)
    # elif st == 'Decompte' :
    #     return countdown_widget(layout,widget)
    if st == 'Heure' :
        return time_widget(layout,widget)
    else :
        return rb_widget(layout,widget)