# #------------------ Trip1 display                                          ------------------------------#
# #------ Possible actions: reset, adjustment +/- 100m                  -----------------------------------#
# class trip1_widget (rb_widget):
#     def __init__(self,layout='1',widget=0):
#         rb_widget.__init__(self,layout,widget)
#     def upup(self):
#         global distance1,old_distance1
#         distance1+=1000000
#         old_distance1=distance1
#         odoconfig['Odometre']['Distance1'] = str(distance1)
#         save_odoconfig()
#     def up(self):
#         global distance1,old_distance1
#         distance1+=100000
#         old_distance1=distance1
#         odoconfig['Odometre']['Distance1'] = str(distance1)
#         save_odoconfig()
#     def down(self):
#         global distance1,old_distance1
#         distance1-=100000
#         if distance1<0:
#             distance1 = 0
#         old_distance1=distance1
#         odoconfig['Odometre']['Distance1'] = str(distance1)
#         save_odoconfig()
#     def downdown(self):
#         global distance1,old_distance1
#         distance1-=1000000
#         if distance1<0:
#             distance1 = 0
#         old_distance1=distance1
#         odoconfig['Odometre']['Distance1'] = str(distance1)
#         save_odoconfig()
#     def reset(self):
#         global distance1,old_distance1,vmoy1,speed,vmax1,chrono_delay1,chrono_time1
#         global odoconfig,chronoconfig
#         global save_t_moy,save_t_odo
#         distance1 = 0
#         old_distance1 = distance1
#         vmoy1 = 0
#         speed = 0
#         vmax1 = 0
#         chrono_delay1 = 5 * aimants
#         chrono_time1 = 0
#         odoconfig['Odometre']['Totalisateur'] = str(totalisateur)
#         odoconfig['Odometre']['Distance1'] = str(distance1)
#         chronoconfig['Chronometre1']['chrono_delay'] = str(chrono_delay1)
#         chronoconfig['Chronometre1']['chrono_time'] = str(chrono_time1)
#         chronoconfig['Chronometre1']['vmax'] = str(vmax1)
#         save_odoconfig()
#         save_chronoconfig()
#         save_t_moy = time.time()
#         save_t_odo = time.time()
#     def render(self,scr):
#         global angle
#         blit_text(scr,_(" Trip1"),(self.x+self.x1,self.y+self.y1), self.label_font,angle)
#         if self.selected:
#             blit_text(scr,'{:6.2f}   '.format(distance1/1000000),(self.x+self.x2,self.y+self.y2),self.selected_font,angle)
#         else:
#             blit_text(scr,'{:6.2f}   '.format(distance1/1000000),(self.x+self.x2,self.y+self.y2),self.value_font, angle)
#         blit_text(scr,'km',(self.x+self.x3,self.y+self.y3),self.unit_font,angle)
#         r = pygame.draw.rect(scr,GRIS,(self.x,self.y,self.w,self.h),1)
#         pygame.display.update(r)