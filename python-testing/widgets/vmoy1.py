# #------------------ Display of average speed on trip1                                            ------------------------------#
# #------ Possible actions: none (you must reset Trip1 to reset)                                                   -----------------------------------#
# class vmoy1_widget(rb_widget):
#     def __init__(self,layout='1',widget=0):
#         rb_widget.__init__(self,layout,widget)
#     def update(self):
#         global vmoy1,chrono_time1
#         temps = time.time() - chrono_time1
#         if temps <= 2 :
#             vmoy1 = 0
#         else :
#             vmoy1 = distance1 * 3.6 / temps / 1000
#     def render(self,scr):
#         global angle
#         blit_text(scr,_(" Avg.Speed1"),(self.x+self.x1,self.y+self.y1), self.label_font,angle)
#         if self.selected:
#             blit_text(scr,'{:3.0f} '.format(vmoy1),(self.x+self.x2,self.y+self.y2),self.selected_font, angle)
#         else:
#             blit_text(scr,'{:3.0f} '.format(vmoy1),(self.x+self.x2,self.y+self.y2),self.value_font, angle)
#         blit_text(scr,'km/h',(self.x+self.x3,self.y+self.y3),self.unit_font,angle)
#         r = pygame.draw.rect(scr,GRIS,(self.x,self.y,self.w,self.h),1)
#         pygame.display.update(r)