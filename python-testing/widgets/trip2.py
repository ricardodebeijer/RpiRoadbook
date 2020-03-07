# class trip2_widget (rb_widget):
#     def __init__(self,layout='1',widget=0):
#         rb_widget.__init__(self,layout,widget)
#     def upup(self):
#         global distance2,old_distance2
#         distance2+=1000000
#         old_distance2=distance2
#         odoconfig['Odometre']['Distance2'] = str(distance2)
#         save_odoconfig()
#     def up(self):
#         global distance2,old_distance2
#         distance2+=100000
#         old_distance2=distance2
#         odoconfig['Odometre']['Distance2'] = str(distance2)
#         save_odoconfig()
#     def down(self):
#         global distance2,old_distance2
#         distance2-=100000
#         if distance2<0:
#             distance2 = 0
#         old_distance2=distance2
#         odoconfig['Odometre']['Distance2'] = str(distance2)
#         save_odoconfig()
#     def downdown(self):
#         global distance2,old_distance2
#         distance2-=1000000
#         if distance2<0:
#             distance2 = 0
#         old_distance2=distance2
#         odoconfig['Odometre']['Distance2'] = str(distance2)
#         save_odoconfig()
#     def reset(self):
#         global distance2,old_distance2,vmoy2,speed,vmax2,chrono_delay2,chrono_time2
#         global odoconfig,chronoconfig
#         global save_t_moy,save_t_odo
#         distance2 = 0
#         old_distance2 = distance2
#         vmoy2 = 0
#         speed = 0
#         vmax2 = 0
#         chrono_delay2 = 5 * aimants
#         chrono_time2 = 0
#         odoconfig['Odometre']['Totalisateur'] = str(totalisateur)
#         odoconfig['Odometre']['Distance2'] = str(distance2)
#         chronoconfig['Chronometre2']['chrono_delay'] = str(chrono_delay2)
#         chronoconfig['Chronometre2']['chrono_time'] = str(chrono_time2)
#         chronoconfig['Chronometre2']['vmax'] = str(vmax2)
#         save_odoconfig()
#         save_chronoconfig()
#         save_t_moy = time.time()
#         save_t_odo = time.time()
#     def render(self,scr):
#         global angle
#         blit_text(scr,_(" Trip2"),(self.x+self.x1,self.y+self.y1), self.label_font,angle)
#         if self.selected:
#             blit_text(scr,'{:6.2f} '.format(distance2/1000000),(self.x+self.x2,self.y+self.y2),self.selected_font,angle)
#         else:
#             blit_text(scr,'{:6.2f} '.format(distance2/1000000),(self.x+self.x2,self.y+self.y2),self.value_font, angle)
#         blit_text(scr,'km',(self.x+self.x3,self.y+self.y3),self.unit_font,angle)
#         r = pygame.draw.rect(scr,GRIS,(self.x,self.y,self.w,self.h),1)
#         pygame.display.update(r)