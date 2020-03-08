# #------------------ Display of time, cpu load and rpi temperature ------------------------------#
# #------  Possible actions: change of personalized display on long press ok (reset)-----------------------------------#
# class status_widget (rb_widget):
#     def __init__(self,layout='0',widget=0):
#         global angle
#         rb_widget.__init__(self,layout,widget)
#     def reset(self):
#         global widgets,current_screen,screenconfig,nb_widgets,ncases,sprites,old_sprites,mode_jour,force_refresh,rbconfig,default_widget

#         # We load the current mode, the current roadbook and its box
#         candidates = ['/home/rpi/RpiRoadbook/RpiRoadbook.cfg','/mnt/piusb/.conf/RpiRoadbook.cfg']
#         rbconfig.read(candidates)
#         rallye = rbconfig['Mode']['mode']

#         current_screen += 1
#         if current_screen > nb_screens :
#             current_screen = 1
#         rbconfig['Ecran']['ecran'] = str(current_screen)
#         save_rbconfig()

#         form =  screenconfig['Affichage{}'.format(current_screen)]['layout']
#         mode_j = screenconfig['Affichage{}'.format(current_screen)]['jour_nuit'] == 'Jour'
#         if mode_j != mode_jour :
#             mode_jour = mode_j
#             alphabet = {}
#         t = 'pa' if orientation == 'Paysage' else 'po'
#         t += 'j' if mode_jour else 'n'
#         if rallye == 'Rallye' :
#             t += 'ra'
#             t += form
#         elif rallye == 'Zoom':
#             t += 'zz'
#         else:
#             t += 'ro1'
#         preset = widget_presets[t]
#         layout = preset['layout']
#         nb_widgets = widget_sizes [layout]
#         if layout in ('00','8','9','10'):
#             ncases = 4
#         else:
#             ncases = 3
#         widgets = {}
#         sprites = {}
#         force_refresh = True
#         #old_sprites = {}

#         default_widget = 7
#         widgets[(0)] = status_widget(layout,0)
#         for i in range(1,nb_widgets+1) :
#             widgets[(i)] = widget_dispatch(screenconfig['Affichage{}'.format(current_screen)]['ligne{}'.format(i)],layout,i)
#         if default_widget == 7 :
#             default_widget = 0
#         if mode_jour :
#             pygame.display.get_surface().fill(BLANC)
#         else :
#             pygame.display.get_surface().fill(NOIR)
#         pygame.display.update()
#         for j in list(widgets.keys()):
#             widgets[j].update()
#     def update(self):
#         self.now = time.localtime()
#     def render(self,scr):
#         global angle,temperature,cpu
#         blit_text(scr,'{:3.0f}C  '.format(temperature),(self.x+self.x1,self.y+self.y1), self.label_font,angle)
#         if self.selected:
#             blit_text(scr,'{:02d}:{:02d}:{:02d}'.format(self.now.tm_hour,self.now.tm_min,self.now.tm_sec),(self.x+self.x2,self.y+self.y2),self.selected_font, angle)
#         else:
#             blit_text(scr,'{:02d}:{:02d}:{:02d}'.format(self.now.tm_hour,self.now.tm_min,self.now.tm_sec),(self.x+self.x2,self.y+self.y2),self.value_font, angle)
#         blit_text(scr,'{:02.0f}%  '.format(cpu),(self.x+self.x3,self.y+self.y3),self.unit_font,angle)
#         r = pygame.draw.rect(scr,GRIS,(self.x,self.y,self.w,self.h),1)
#         pygame.display.update(r)