# #------------------ Instantaneous speed display                                            ------------------------------#
# #------ Possible actions: none                                           -----------------------------------#
# class speed_widget (rb_widget):
#     def __init__(self,layout='1',widget=0):
#         rb_widget.__init__(self,layout,widget)
#     def update(self):
#         global speed,save_t_moy,old_totalisateur
#         save_t = time.time()
#         if ( save_t - save_t_moy >= 1) : # Vitesse moyenne sur 1 seconde
#             speed = (totalisateur-old_totalisateur)*3.6/(save_t-save_t_moy)/1000;
#             save_t_moy = save_t
#             old_totalisateur = totalisateur
#     def render(self,scr):
#         global angle,speed
#         blit_text(scr,_(" Speed"),(self.x+self.x1,self.y+self.y1), self.label_font,angle)
#         if self.selected:
#             blit_text(scr,'{:3.0f} '.format(speed),(self.x+self.x2,self.y+self.y2),self.selected_font, angle)
#         else:
#             blit_text(scr,'{:3.0f} '.format(speed),(self.x+self.x2,self.y+self.y2),self.value_font, angle)
#         blit_text(scr,'km/h',(self.x+self.x3,self.y+self.y3),self.unit_font,angle)
#         r = pygame.draw.rect(scr,GRIS,(self.x,self.y,self.w,self.h),1)
#         pygame.display.update(r)