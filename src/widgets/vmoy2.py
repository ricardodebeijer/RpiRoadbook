# class vmoy2_widget(rb_widget):
#     def __init__(self,layout='1',widget=0):
#         rb_widget.__init__(self,layout,widget)
#     def update(self):
#         global vmoy2,chrono_time2
#         temps = time.time() - chrono_time2
#         if temps <= 2 :
#             vmoy2 = 0
#         else :
#             vmoy2 = distance2 * 3.6 / temps /1000
#     def render(self,scr):
#         global angle
#         blit_text(scr,_(" Avg.Speed2"),(self.x+self.x1,self.y+self.y1), self.label_font,angle)
#         if self.selected:
#             blit_text(scr,'{:03.0f} '.format(vmoy2),(self.x+self.x2,self.y+self.y2),self.selected_font, angle)
#         else:
#             blit_text(scr,'{:03.0f} '.format(vmoy2),(self.x+self.x2,self.y+self.y2),self.value_font, angle)
#         blit_text(scr,'km/h',(self.x+self.x3,self.y+self.y3),self.unit_font,angle)
#         r = pygame.draw.rect(scr,GRIS,(self.x,self.y,self.w,self.h),1)
#         pygame.display.update(r)