# #------------------ Totalizer display                                          ------------------------------#
# #------ Possible actions: none                                                 -----------------------------------#
# class odo_widget (rb_widget):
#     def __init__(self,layout='1',widget=0):
#         rb_widget.__init__(self,layout,widget)
#     def render(self,scr):
#         global angle
#         blit_text(scr,_(" Distance"),(self.x+self.x1,self.y+self.y1), self.label_font,angle)
#         if self.selected:
#             blit_text(scr,'{:05.0f} '.format(totalisateur/1000000),(self.x+self.x2,self.y+self.y2),self.selected_font, angle)
#         else:
#             blit_text(scr,'{:05.0f} '.format(totalisateur/1000000),(self.x+self.x2,self.y+self.y2),self.value_font, angle)
#         blit_text(scr,'km',(self.x+self.x3,self.y+self.y3),self.unit_font,angle)
#         r = pygame.draw.rect(scr,GRIS,(self.x,self.y,self.w,self.h),1)
#         pygame.display.update(r)