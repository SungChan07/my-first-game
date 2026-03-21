import pygame
import sys

# 초기화
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Smooth Movement")

# 색상 및 설정
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

x = 400
y = 300
radius = 50
speed = 10  # 이동 속도 (매 프레임당 10픽셀)

clock = pygame.time.Clock()
running = True

# 메인 루프
while running:
    # 1. 이벤트 처리 (창 닫기 등 시스템 이벤트만 처리)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # 2. 키 상태 확인 (누르고 있으면 계속 True를 반환)
    keys = pygame.key.get_pressed()
    
    # 왼쪽 키를 누르고 있고, 왼쪽 벽을 넘지 않았을 때
    if keys[pygame.K_LEFT] and x - radius > 0:
        x -= speed
    # 오른쪽 키를 누르고 있고, 오른쪽 벽을 넘지 않았을 때
    if keys[pygame.K_RIGHT] and x + radius < 800:
        x += speed
    # 위쪽 키를 누르고 있고, 위쪽 벽을 넘지 않았을 때
    if keys[pygame.K_UP] and y - radius > 0:
        y -= speed
    # 아래쪽 키를 누르고 있고, 아래쪽 벽을 넘지 않았을 때
    if keys[pygame.K_DOWN] and y + radius < 600:
        y += speed

    # 3. 화면 그리기
    screen.fill(WHITE)
    pygame.draw.circle(screen, BLUE, (x, y), radius)
    
    # 4. 화면 업데이트
    pygame.display.flip()
    
    # 5. 프레임 제한 (초당 60번 실행)
    clock.tick(60)

pygame.quit()
sys.exit()