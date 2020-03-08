# #------------------ Countdown display  ------------------------------#
# #------ Possible actions: adding 30 seconds, resetting, starting the countdown   ----------------#
# class countdown_widget (rb_widget):
#     def __init__(self,layout='1',widget=0):
#         global decompte
#         rb_widget.__init__(self,layout,widget)
#         setup_alphabet(self.over_font)
#         setup_alphabet(self.inside_font)
#         self.originfont = self.value_font
#         self.originunitfont = self.unit_font
#     def up(self):
#         global decompte
#         if not start_decompte:
#             decompte += 30
#     def down(self):
#         global start_decompte,chrono_decompte,current_widget,default_widget
#         if not start_decompte:
#             start_decompte = True
#             chrono_decompte = time.time() + decompte
#             chronoconfig['Decompte']['start_decompte'] = str(start_decompte)
#             chronoconfig['Decompte']['chrono_decompte'] = str(chrono_decompte)
#             save_chronoconfig()
#             current_widget = default_widget
#             self.deselect()
#     def reset(self):
#         global decompte,start_decompte,chrono_decompte
#         global chronoconfig
#         decompte = 0
#         start_decompte = False
#         chrono_decompte = 0
#         chronoconfig['Decompte']['start_decompte'] = str(start_decompte)
#         chronoconfig['Decompte']['chrono_decompte'] = str(chrono_decompte)
#         save_chronoconfig()
#         self.value_font = self.originfont
#         self.unit_font = self.originunitfont
#     def render(self,scr):
#         global angle
#         if start_decompte:
#             t = chrono_decompte - time.time()
#             # when you have x minutes, you can point between x and x + 29 seconds
#             # There are less than 10s, we will soon be able to point
#             if t <= 10 :
#                 m,s = divmod(t,60)
#                 ts = math.floor(s*5)
#                 if ts % 2 == 0 :
#                     self.value_font = self.inside_font
#                 else:
#                     self.value_font = self.originfont
#             # All is well, we should point right now
#             if t >-20 and t <= 0 :
#                 self.value_font = self.inside_font
#             # between x + 20 seconds and x + 29, you should hurry to point
#             if t <= -20 and t > -30 :
#                 m,s = divmod (t,60)
#                 ts = math.floor(s*5)
#                 if ts % 2 == 0 :
#                     self.value_font = self.over_font
#                 else :
#                     self.value_font = self.inside_font
#             # We are late
#             if t < -30 :
#                 self.value_font =  self.over_font
#                 #self.unit_font = self.label_font
#             if t < 0 :
#                 t = -t
#         else:
#             t = decompte
#         m,s = divmod (t,60)
#         #ss = math.floor((s*10) % 10)
#         blit_text(scr,_(" Countdown"),(self.x+self.x1,self.y+self.y1), self.label_font,angle)
#         if self.selected:
#             blit_text(scr,'{:02.0f}:{:02.0f} '.format(m,s),(self.x+self.x2,self.y+self.y2),self.selected_font,angle)
#         else:
#             blit_text(scr,'{:02.0f}:{:02.0f} '.format(m,s),(self.x+self.x2,self.y+self.y2),self.value_font, angle)
#         #blit_text(scr,'.{:1.0f} '.format(ss),(self.x+self.x3,self.y+self.y3),self.unit_font,angle)
#         r = pygame.draw.rect(scr,GRIS,(self.x,self.y,self.w,self.h),1)
#         pygame.display.update(r)
#     def select(self):
#         global widget_iscountdown
#         rb_widget.select(self)
#         widget_iscountdown = True