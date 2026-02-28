# Foi necessario baixar a biblioteca externa e a inicializar no codigo, antes de a usar.
import pygame
pygame.init()
# Inicializa os modulos internos da biblioteca
pygame.mixer.init()
# Garante que o som esteja pronto para sair.
pygame.mixer.music.load('ex21.mp3')
# Esta linha carrega o arquivo de áudio para a memória do programa.
pygame.mixer.music.play()
# Este é o comando de "Play". Ele inicia a reprodução do arquivo que foi carregado anteriormente
input('Tocando música... Aperte Enter para parar.')

