'''
s = pygame.Surface((400,100))  # the size of your rect
s.set_alpha(128)                # alpha level
s.fill((245,66,158))           # this fills the entire surface
scrn.blit(s, (440,110))    # (0,0) are the top-left coordinates

font = pygame.font.SysFont(None, 64)
img = font.render('Koteczki miłości', True, (255,255,255))
scrn.blit(img, (460, 140))
'''