# #------------------ Chrono1 display                                          ------------------------------#
# #------ Possible actions: none                                                -----------------------------------#
# class chrono1_widget(rb_widget):
#     def __init__(self,layout='1',widget=0):
#         rb_widget.__init__(self,layout,widget)
#     def reset(self):
#         global distance1,chrono_delay1,chrono_time1,vmax1
#         global odoconfig,chronoconfig
#         distance1 = 0
#         chrono_delay1 = 5 * aimants
#         chrono_time1 = 0
#         vmax1 = 0
#         odoconfig['Odometre']['Totalisateur'] = str(totalisateur)
#         odoconfig['Odometre']['Distance1'] = str(distance1)
#         chronoconfig['Chronometre1']['chrono_delay'] = str(chrono_delay1)
#         chronoconfig['Chronometre1']['chrono_time'] = str(chrono_time1)
#         chronoconfig['Chronometre1']['vmax'] = str(vmax1)
#         save_odoconfig()
#         save_chronoconfig()
#     def render(self,scr):
#         global angle,chrono_time1
#         if chrono_time1 != 0:
#              t = time.time() - chrono_time1
#         else:
#              t = 0
#         m,s = divmod (t,60)
#         if m >= 60 :
#             h,m = divmod (m,60)
#         ss = (s*100) % 100
#         blit_text(scr,_(" Stopwatch1"),(self.x+self.x1,self.y+self.y1), self.label_font,angle)
#         if self.selected:
#             blit_text(scr,'{:02.0f}:{:02.0f}'.format(m,s),(self.x+self.x2,self.y+self.y2),self.selected_font,angle)
#         else:
#             blit_text(scr,'{:02.0f}:{:02.0f}'.format(m,s),(self.x+self.x2,self.y+self.y2),self.value_font, angle)
#         blit_text(scr,'.{:02.0f}  '.format(ss),(self.x+self.x3,self.y+self.y3),self.unit_font,angle)
#         r = pygame.draw.rect(scr,GRIS,(self.x,self.y,self.w,self.h),1)
#         pygame.display.update(r)