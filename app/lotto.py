import random


class Card:
    def __init__(self, name):
        self.card = self.generate_card()
        self.name = name

    @staticmethod
    def generate_card():
        card_numbers = random.sample(range(1, 91), 15)
        rows = [card_numbers[i:i + 5] for i in range(0, len(card_numbers), 5)]
        for row in rows:
            row.sort()
            for i in range(4):
                row.insert(random.randint(0, len(row)), ' ')
        return rows

    def get_index_number(self, barrel):
        for row in self.card:
            for number in row:
                if number == barrel:
                    inner_index = row.index(number)
                    outer_index = self.card.index(row)
                    return outer_index, inner_index

    def cross_out(self, barrel):
        index = self.get_index_number(barrel)
        if index:
            self.card[index[0]][index[1]] = '-'

    def has_number_in_card(self, barrel):
        if self.get_index_number(barrel):
            return True
        return False

    def __str__(self):
        return '{:-^25}'.format(self.name) + '\n' + \
               f'{self.card[0][0]} {self.card[0][1]} {self.card[0][2]} {self.card[0][3]} {self.card[0][4]} ' \
               f'{self.card[0][5]} {self.card[0][6]} {self.card[0][7]} {self.card[0][8]}\n' \
               f'{self.card[1][0]} {self.card[1][1]} {self.card[1][2]} {self.card[1][3]} {self.card[1][4]} ' \
               f'{self.card[1][5]} {self.card[1][6]} {self.card[1][7]} {self.card[1][8]}\n' \
               f'{self.card[2][0]} {self.card[2][1]} {self.card[2][2]} {self.card[2][3]} {self.card[2][4]} ' \
               f'{self.card[2][5]} {self.card[2][6]} {self.card[2][7]} {self.card[2][8]}\n' + \
               '{:-^25}'.format('-')


class Bag:
    def __init__(self):
        self.bag = [x for x in range(1, 91)]

    def get_barrel(self):
        random.shuffle(self.bag)
        barrel = self.bag.pop()
        print(f'Номер бочонка - {barrel}. Осталось бочонков - {len(self.bag)}')
        return barrel


class Player:
    def __init__(self, name, is_human: bool):
        self.name = name
        self.is_human = is_human
        self.card = Card(name)
        self.score = 0
        self.is_dead = False

    def __str__(self):
        return str(self.card)

    def check_barrel(self, barrel):
        if not self.is_human:
            if self.card.has_number_in_card(barrel):
                self.card.cross_out(barrel)
                self.score += 1
                return
            return
        answer = input_text(f'Зачеркнуть число {barrel}?', check_choose_is_valid, 'д', 'н')
        if answer == 'д' and self.card.has_number_in_card(barrel):
            self.card.cross_out(barrel)
            self.score += 1
            return
        elif answer == 'н' and not self.card.has_number_in_card(barrel):
            return
        else:
            print(f'Некорректное действие. Игрок {self.name} выбывает из игры!')
            self.is_dead = True


def add_players():
    count_players = int(input_text('Введите количество игроков', check_answer_is_integer))
    players = []
    for player in range(1, count_players + 1):
        players.append(create_player(player))
    return players


def check_answer_is_integer(answer):
    try:
        if int(answer) > 0:
            return True
    except ValueError:
        pass
    print('Введите целое положительное число')
    return False


def check_field_is_not_empty(answer):
    if not answer.strip():
        print('Поле не может быть пустым')
        return False
    return True


def check_choose_is_valid(first, second, answer):
    if not answer.lower() in (first, second):
        print(f'Выберите {first} или {second}')
        return False
    return True


def input_text(question, method_check, first=None, second=None):
    while True:
        if first:
            answer = input(f'{question} ({first}/{second}): ')
            if method_check(first, second, answer):
                return answer
        else:
            answer = input(f'{question}: ')
            if method_check(answer):
                return answer


def create_player(count_player):
    player_type = input_text(f'Выберите тип игрока {count_player}.', check_choose_is_valid, 'человек', 'компьютер')
    if player_type.lower() == 'человек':
        is_human = True
        name = input_text(f'Выберите имя игрока {count_player}', check_field_is_not_empty)
    else:
        is_human = False
        name = f'Игрок {count_player} (компьютер)'
    return Player(name, is_human)


def main():
    players = add_players()
    bag = Bag()
    for i in range(90):
        if len(players) == 0:
            print('Игра окончена! Все игроки выбыли!')
            break
        barrel = bag.get_barrel()
        for player in players[:]:
            print(player)
            player.check_barrel(barrel)
            if player.is_dead:
                players.remove(player)
            if player.score == 15:
                print(f'Игра окончена! Победитель -  {player.name}!!!')
                print(player)
                return


if __name__ == '__main__':
    main()
