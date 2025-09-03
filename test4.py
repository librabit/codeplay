import pygame
import sys
import time
import random

# Pygame 초기화
pygame.init()

# 화면 설정
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("카드 오브 제네시스: 잃어버린 예언")

# 게임 상태 초기화 (Pygame 초기화 코드 다음에 추가)
game_state = "prologue"  # 초기 게임 상태
story_text_index = 0     # 스토리 텍스트 인덱스

# 색상 정의
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)
GOLD = (255, 215, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# 폰트 설정
try:
    font = pygame.font.SysFont('malgungothic', 30)
    title_font = pygame.font.SysFont('malgungothic', 60)
except:
    font = pygame.font.Font(None, 30)
    title_font = pygame.font.Font(None, 60)

# 게임 데이터 (스토리)
story_data = {
    "prologue": [
        "프롤로그: 잊혀진 예언의 속삭임",
        "에테르나에서 가장 오래된 지식의 수호자인 대현자 리안의 서고...",
        "아론은 우연히 먼지 쌓인 책 한 권을 발견하고, 그 안에 잊혀진 예언을 읽게 됩니다.",
        "예언: '별이 가장 밝게 빛나는 밤, 잃어버린 힘이 깨어나리니, 용기 있는 자가 그 길을 따르리라'",
        "예언을 읽는 순간, 아론의 손에 있던 낡은 카드가 빛을 발하기 시작합니다.",
        "그것은 전설 속의 '시작의 카드: 운명'이었습니다.",
        "리안은 아론이 예언의 주인공임을 직감하고, 길에서 만나는 이들을 믿고 협력하라고 조언합니다."
    ],
    "journey_start": [
        "여정의 시작과 동료",
        "아론은 운명을 받아들이고 모험을 시작합니다. '시간의 시계탑' 근처에 다다랐을 때...",
        "몬스터의 습격을 받고 있는 고대 문명 연구자 엘레나와 그녀 옆에 있는 겁에 질린 어린 정령 루카를 발견합니다.",
        "아론은 용감하게 몬스터와 싸워 그들을 구합니다.",
        "엘레나는 아론의 카드를 보고 놀라워하며 동행을 제안하고, 아론은 그들을 동료로 받아들입니다."
    ],
    "first_test": [
        "첫 번째 시험: 시간의 제네시스 카드",
        "엘레나와 루카와 함께 시간의 시계탑에 도착한 아론은 첫 번째 제네시스 카드인 '시간의 제네시스 카드: 크로노스'를 발견합니다.",
        "카드는 아론의 진정한 의지를 시험하려는 듯 과거와 미래가 뒤섞인 혼란스러운 환영을 보여줍니다.",
        "엘레나의 지식과 루카의 용기 덕분에 아론은 시험을 통과하고 그들의 유대감은 더욱 깊어집니다."
    ],
    "tutorial": [
        "튜토리얼: 카드 배틀의 기본",
        "카드 배틀은 턴제로 진행됩니다. 몬스터를 필드에 소환하고, 마법/함정 카드를 세트하세요.",
        "공격력이 높은 몬스터로 상대 몬스터를 공격하여 LP를 깎을 수 있습니다.",
        "LP가 0이 되면 패배합니다. 상대의 LP를 0으로 만들어 승리하세요.",
        "본격적인 카드 배틀을 시작합니다..."
    ]
}

# 카드 데이터 (AI와 플레이어 덱에 사용)
CARD_DATABASE = {
    "gaia": {"name": "가이아 더 드래곤 나이트", "type": "monster", "level": 7, "atk": 2600, "def": 2100},
    "summoned_skull": {"name": "소환수 스컬", "type": "monster", "level": 6, "atk": 2500, "def": 1200},
    "kuriboh": {"name": "크리보", "type": "monster", "level": 1, "atk": 300, "def": 200},
    "battle_ox": {"name": "배틀 옥스", "type": "monster", "level": 4, "atk": 1700, "def": 1000},
    "blue_eyes": {"name": "푸른 눈의 백룡", "type": "monster", "level": 8, "atk": 3000, "def": 2500},
    "dark_magician": {"name": "블랙 매지션", "type": "monster", "level": 7, "atk": 2500, "def": 2100},
    "mystical_space_typhoon": {"name": "싸이크론", "type": "spell", "effect": "상대 필드의 마법/함정 카드 1장을 파괴한다."},
    "monster_reborn": {"name": "죽은 자의 소생", "type": "spell", "effect": "자신 또는 상대 묘지의 몬스터 1장을 특수 소환한다."},
    "mirror_force": {"name": "성스러운 방어막 거울의 힘", "type": "trap", "effect": "상대 필드 위에 앞면 공격 표시로 존재하는 모든 몬스터를 파괴한다."},
    "goblin_squad": {"name": "고블린 부대", "type": "monster", "level": 3, "atk": 1200, "def": 1000}
}

# --- 클래스 정의 ---
class Player:
    def __init__(self, is_ai=False, battle_deck=None):
        self.is_ai = is_ai
        self.lp = 8000
        self.hand = []
        self.deck = battle_deck if battle_deck else self.generate_deck()
        self.monster_field = [None] * 5
        self.spell_trap_field = [None] * 5
        self.graveyard = []
        self.normal_summoned_this_turn = False
        self.attacked_monsters = set()
        self.is_turn = False

    def generate_deck(self):
        deck = []
        cards_to_add = ["gaia", "summoned_skull", "kuriboh", "battle_ox", "monster_reborn", "mirror_force", "mystical_space_typhoon"]
        for _ in range(5):
            for key in cards_to_add:
                deck.append(Card(CARD_DATABASE[key]))
        random.shuffle(deck)
        return deck

    def draw_card(self, num=1):
        for _ in range(num):
            if self.deck:
                card = self.deck.pop(0)
                self.hand.append(card)
                return card
        return None


# Card 클래스 수정
class Card:
    def __init__(self, data):
        self.name = data.get('name', '')
        self.type = data.get('type', '')
        self.level = data.get('level', 0)
        self.atk = data.get('atk', 0)      # attack -> atk로 통일
        self.defense = data.get('def', 0)   # def 값 사용
        self.effect = data.get('effect', '')
        self.is_set = False
        self.position = 'attack'
    
    def __repr__(self):
        if self.type == "monster":
            return f"[{self.name} (ATK:{self.atk}/DEF:{self.defense}) - {self.position}]"
        else:
            return f"[{self.name} ({'세트' if self.is_set else '발동'})]"

# --- BattleManager 클래스 (추가) ---
class BattleManager:
    def __init__(self, player_deck, ai_deck):
        self.player = Player(battle_deck=player_deck)
        self.ai = Player(is_ai=True, battle_deck=ai_deck)
        self.current_turn = "player"
        self.turn_count = 1
        self.game_log = []
        self.selected_card = None
        self.attacking_monster = None

    def start_battle(self):
        self.player.draw_card(5)
        self.ai.draw_card(5)

    def draw_phase(self):
        if self.current_turn == "player":
            self.player.draw_card()
            self.game_log.append("플레이어 드로우 페이즈")
        else:
            self.ai.draw_card()
            self.game_log.append("AI 드로우 페이즈")

    def main_phase(self):
        self.game_log.append("메인 페이즈 1 시작")

    def battle_phase(self):
        self.game_log.append("배틀 페이즈 시작")

    def end_phase(self):
        self.game_log.append("엔드 페이즈 시작")
        self.player.normal_summoned_this_turn = False
        self.player.attacked_monsters.clear()
        self.turn_count += 1
        self.current_turn = "ai" if self.current_turn == "player" else "player"

    def attack(self, attacker_idx, target_idx):
        attacker = self.player.monster_field[attacker_idx]
        target = self.ai.monster_field[target_idx]
        
        if attacker.atk > target.atk:
            self.ai.lp -= (attacker.atk - target.atk)
            self.ai.monster_field[target_idx] = None
            self.game_log.append(f"{attacker.name}가 {target.name}를 파괴하고 {attacker.atk - target.atk}의 데미지를 주었다!")
        elif attacker.atk == target.atk:
            self.player.monster_field[attacker_idx] = None
            self.ai.monster_field[target_idx] = None
            self.game_log.append(f"{attacker.name}와 {target.name}가 서로 파괴되었다.")
        else:
            self.player.lp -= (target.atk - attacker.atk)
            self.player.monster_field[attacker_idx] = None
            self.game_log.append(f"{attacker.name}가 파괴되고, 플레이어가 {target.atk - attacker.atk}의 데미지를 입었다.")
        
        self.player.attacked_monsters.add(attacker)

    def is_game_over(self):
        if self.player.lp <= 0:
            return "패배"
        if self.ai.lp <= 0 or all(m is None for m in self.ai.monster_field):
            return "승리"
        return None

# --- Pygame GUI 함수 ---
def draw_text(text, font, color, x, y, center=False):
    text_surface = font.render(text, True, color)
    if center:
        text_rect = text_surface.get_rect(center=(x, y))
    else:
        text_rect = text_surface.get_rect(topleft=(x, y))
    screen.blit(text_surface, text_rect)
    return text_rect

def draw_card(card, x, y, width, height):
    pygame.draw.rect(screen, BLUE, (x, y, width, height), border_radius=10)
    pygame.draw.rect(screen, BLACK, (x + 5, y + 5, width - 10, height - 10), border_radius=5)
    
    draw_text(card.name, font, WHITE, x + width // 2, y + 20, center=True)
    draw_text(f"ATK: {card.atk}", font, WHITE, x + width // 2, y + 100, center=True)
    draw_text(f"DEF: {card.defense}", font, WHITE, x + width // 2, y + 130, center=True)

# --- 게임 상태 관리 및 렌더링 ---
def render_story_state(state):
    global story_text_index
    screen.fill(BLACK)
    
    current_texts = story_data[state]
    draw_text(current_texts[story_text_index], font, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, center=True)
    draw_text("마우스 왼쪽 버튼을 클릭하여 계속...", font, GRAY, SCREEN_WIDTH // 2, SCREEN_HEIGHT - 100, center=True)

def render_battle_state(battle_manager):
    screen.fill(BLACK)
    
    # LP 표시
    draw_text(f"플레이어 LP: {battle_manager.player.lp}", font, WHITE, 50, 50)
    draw_text(f"AI LP: {battle_manager.ai.lp}", font, WHITE, SCREEN_WIDTH - 200, 50)
    
    # 턴 정보
    draw_text(f"현재 턴: {battle_manager.current_turn.upper()}", font, GOLD, SCREEN_WIDTH // 2, 50, center=True)
    
    # AI 몬스터 필드
    for i in range(5):
        rect = pygame.Rect(300 + i * 120, 150, 100, 150)
        pygame.draw.rect(screen, GRAY, rect, 2, border_radius=10)
        if battle_manager.ai.monster_field[i]:
            draw_card(battle_manager.ai.monster_field[i], rect.x, rect.y, rect.width, rect.height)

    # 플레이어 몬스터 필드
    for i in range(5):
        rect = pygame.Rect(300 + i * 120, 500, 100, 150)
        pygame.draw.rect(screen, GRAY, rect, 2, border_radius=10)
        if battle_manager.player.monster_field[i]:
            draw_card(battle_manager.player.monster_field[i], rect.x, rect.y, rect.width, rect.height)
    
    # 플레이어 핸드
    for i, card in enumerate(battle_manager.player.hand):
        rect = pygame.Rect(50 + i * 120, 680, 100, 150)
        pygame.draw.rect(screen, GOLD, rect, 2, border_radius=10)
        draw_card(card, rect.x, rect.y, rect.width, rect.height)

    # 게임 로그
    for i, log in enumerate(battle_manager.game_log[-5:]):
        draw_text(log, font, GREEN, 50, SCREEN_HEIGHT - 150 + i * 30)

# --- 메인 게임 루프 ---
def main_game_loop():
    global game_state, story_text_index, battle_manager

    running = True
    battle_manager = None
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if game_state in story_data:
                        story_text_index += 1
                        if story_text_index >= len(story_data[game_state]):
                            if game_state == "prologue":
                                game_state = "journey_start"
                            elif game_state == "journey_start":
                                # 첫 번째 몬스터 배틀 시작
                                game_state = "battle_with_goblin"
                                ai_deck = [Card(CARD_DATABASE["goblin_squad"]) for _ in range(10)]
                                player_deck = Player().generate_deck()
                                battle_manager = BattleManager(player_deck, ai_deck)
                                battle_manager.start_battle()
                            elif game_state == "first_test":
                                game_state = "tutorial"
                            elif game_state == "tutorial":
                                # 다음 배틀 준비
                                game_state = "battle" 
                            story_text_index = 0
                    
                    elif game_state == "battle_with_goblin" and battle_manager.current_turn == "player":
                        # 플레이어 턴 로직
                        mouse_pos = event.pos
                        
                        # 카드 소환
                        for i, card in enumerate(battle_manager.player.hand):
                            card_rect = pygame.Rect(50 + i * 120, 680, 100, 150)
                            if card_rect.collidepoint(mouse_pos) and card.type == "monster":
                                for j, field_slot in enumerate(battle_manager.player.monster_field):
                                    if field_slot is None:
                                        battle_manager.player.monster_field[j] = card
                                        battle_manager.player.hand.remove(card)
                                        battle_manager.game_log.append(f"플레이어가 {card.name}를 소환했습니다.")
                                        break
                                break
                                
                        # 공격
                        for i, ai_monster in enumerate(battle_manager.ai.monster_field):
                            if ai_monster:
                                monster_rect = pygame.Rect(300 + i * 120, 150, 100, 150)
                                if monster_rect.collidepoint(mouse_pos):
                                    if battle_manager.player.monster_field[0]:
                                        battle_manager.attack(0, i)
                                        battle_manager.end_phase()
                                        break

        screen.fill(BLACK)
        
        if game_state in story_data:
            render_story_state(game_state)
        elif game_state == "battle_with_goblin":
            render_battle_state(battle_manager)
            if battle_manager.is_game_over():
                if battle_manager.is_game_over() == "승리":
                    game_state = "first_test"
                    story_text_index = 0
                else:
                    game_state = "game_over"
            # AI 턴 (매우 간단한 로직)
            elif battle_manager.current_turn == "ai":
                time.sleep(1) # AI 생각하는 시간
                if battle_manager.ai.hand:
                    card_to_summon = next((c for c in battle_manager.ai.hand if c.type == "monster"), None)
                    if card_to_summon:
                        for i, field_slot in enumerate(battle_manager.ai.monster_field):
                            if field_slot is None:
                                battle_manager.ai.monster_field[i] = card_to_summon
                                battle_manager.ai.hand.remove(card_to_summon)
                                battle_manager.game_log.append(f"AI가 {card_to_summon.name}를 소환했습니다.")
                                break
                
                # 공격
                if any(m is not None for m in battle_manager.player.monster_field) and any(m is not None for m in battle_manager.ai.monster_field):
                    ai_monster_idx = next((i for i, m in enumerate(battle_manager.ai.monster_field) if m is not None), -1)
                    if ai_monster_idx != -1:
                        target_idx = next((i for i, m in enumerate(battle_manager.player.monster_field) if m is not None), -1)
                        if target_idx != -1:
                            battle_manager.attack(ai_monster_idx, target_idx)
                
                battle_manager.end_phase()

        elif game_state == "game_over":
            draw_text("게임 오버", title_font, RED, SCREEN_WIDTH // 2, 300, center=True)
            draw_text("당신의 용기는 부족했습니다. 다시 도전하세요.", font, WHITE, SCREEN_WIDTH // 2, 400, center=True)
            draw_text("게임을 종료하려면 창을 닫아주세요.", font, GRAY, SCREEN_WIDTH // 2, SCREEN_HEIGHT - 100, center=True)

        elif game_state == "battle":
            # 이 부분에 카드 배틀 로직을 구현합니다.
            # 지금은 간단한 안내 메시지만 표시합니다.
            draw_text("카드 배틀 시작!", title_font, GOLD, SCREEN_WIDTH // 2, 300, center=True)
            draw_text("이곳에 플레이어와 AI의 턴제 배틀 로직이 들어갑니다.", font, WHITE, SCREEN_WIDTH // 2, 400, center=True)
            draw_text("게임 종료하려면 창을 닫아주세요.", font, GRAY, SCREEN_WIDTH // 2, SCREEN_HEIGHT - 100, center=True)

        pygame.display.flip()
        pygame.time.Clock().tick(30)

if __name__ == "__main__":
    main_game_loop()
