# def bark (name, weight):
#     if weight > 20:
#         print(name, 'ГАВ')
#     else:
#         print(name, 'гав')
# bark('aa', -50)
# def get_attribute(query, default):
#     question = query + default + '?'
#     answer = input(question)
#     if answer == '':
#         answer = default
#     print('Вы выбрали', answer)
#     return answer
#
#
# hair = get_attribute('Цвет волос', ' темные')

def drink(param):
    msg = 'Выпиваем ' + param + ' Стакан'
    print(msg)
    param = 'пустой'


glass = 'полный'
drink(glass)
print(glass)
