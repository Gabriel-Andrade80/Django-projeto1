# from inspect import signature
from random import randint

# from faker import Faker

title = [
'Frango Assado com Batatas e Vegetais', 'Salmão Grelhado com Molho de Ervas', 'Spaghetti Carbonara', 'Ratatouille', 'Guacamole', 'Risoto de Cogumelos', 'Tacos de Camarão', 'Mousse de Chocolate', 'Salada de Quinoa com Legumes Assados', 'Pudim de Leite Condensado'
]

description = [
'Uma refeição reconfortante que combina peitos de frango suculentos, batatas macias e uma variedade de vegetais caramelizados, tudo temperado com ervas frescas e assado até a perfeição.',
'Um prato clássico da culinária italiana, este spaghetti é preparado com um molho cremoso de ovos, queijo parmesão, bacon crocante e pimenta-do-reino, resultando em um sabor irresistível e reconfortante.',
'Salmão fresco grelhado e coberto com um molho fresco de ervas, proporcionando um equilíbrio delicioso entre o sabor suave do peixe e a vibrante mistura de ervas.',
'Uma tradicional receita francesa, este prato apresenta uma harmoniosa combinação de berinjela, abobrinha, pimentões, tomates e cebolas assados lentamente até ficarem macios e cheios de sabor.',
'Um clássico da culinária mexicana, esta pasta de abacate é fresca, cremosa e levemente picante, perfeita para servir como acompanhamento ou para mergulhar tortilhas crocantes.',
'Um prato italiano rico e reconfortante, este risoto é preparado com cogumelos variados, resultando em uma mistura cremosa e saborosa de arroz e sabores terrosos.',
'Uma deliciosa interpretação mexicana dos tacos, estes são recheados com camarões grelhados, abacate cremoso, coentro fresco e um toque de pimenta, proporcionando uma explosão de sabor em cada mordida.',
'Uma sobremesa indulgente e luxuosa, esta mousse é feita com chocolate meio amargo derretido, claras em neve e creme de leite, resultando em uma textura aerada e um sabor intenso de chocolate.',
'Uma opção saudável e deliciosa, esta salada apresenta quinoa leve e nutritiva, acompanhada de legumes assados dourados, resultando em uma combinação de sabores e texturas que satisfazem.',
'Uma sobremesa clássica e irresistível, este pudim é cremoso, suave e levemente doce, com uma deliciosa calda de caramelo que o torna ainda mais decadente e delicioso.'
]

preparation_time = [
'01','02','03','04','05',
'06','07','08','09','10'
]

servings = [
'01','02','03','04','05',
'06','07','08','09','10'
]

preparation_steps = [
'''Pré-aqueça o forno a 200°C.
Tempere os peitos de frango com sal, pimenta e ervas frescas.
Em uma assadeira grande, coloque as batatas, cenouras, cebola e alho. Regue com azeite de oliva, tempere com sal e pimenta, e misture bem.
Coloque os peitos de frango sobre os vegetais na assadeira.
Asse por cerca de 40-45 minutos, ou até que o frango esteja cozido e os vegetais estejam macios, dourados e caramelizados.
Sirva quente e aproveite!''',
'''Tempere os filés de salmão com sal, pimenta e suco de limão.
Em uma tigela pequena, misture a salsa, cebolinha, estragão e endro.
Aqueça o azeite de oliva em uma frigideira grande em fogo médio-alto.
Grelhe os filés de salmão por cerca de 4-5 minutos de cada lado, ou até que estejam cozidos ao seu gosto.
Retire os filés de salmão da frigideira e reserve.
Na mesma frigideira, adicione a manteiga e deixe derreter.
Adicione as ervas picadas à manteiga derretida na frigideira e cozinhe por 1-2 minutos.
Regue o molho de ervas sobre os filés de salmão grelhados.
Sirva imediatamente, acompanhado de arroz ou legumes, se desejar.''',
'''Corte todos os vegetais em rodelas finas ou cubos pequenos.
Pré-aqueça o forno a 200°C.
Em uma assadeira grande, distribua os vegetais em camadas, intercalando-os.
Regue os vegetais com azeite de oliva e tempere com sal, pimenta e ervas frescas.
Asse no forno por cerca de 45-50 minutos, ou até que os vegetais estejam macios e levemente dourados.
Sirva quente, como acompanhamento ou como prato principal, acompanhado de pão crustoso.''',
'''Pré-aqueça o forno a 200°C.
Tempere os peitos de frango com sal, pimenta e ervas frescas.
Em uma assadeira grande, coloque as batatas, cenouras, cebola e alho. Regue com azeite de oliva, tempere com sal e pimenta, e misture bem.
Coloque os peitos de frango sobre os vegetais na assadeira.
Asse por cerca de 40-45 minutos, ou até que o frango esteja cozido e os vegetais estejam macios, dourados e caramelizados.
Sirva quente e aproveite!''',
'''Em uma panela, aqueça o caldo de legumes e mantenha-o aquecido em fogo baixo.
Em outra panela grande, derreta 1 colher de sopa de manteiga em fogo médio-alto.
Refogue a cebola e o alho até ficarem macios e levemente dourados.
Adicione os cogumelos fatiados e refogue até que estejam macios e dourados.
Adicione o arroz arbóreo à panela e mexa por cerca de 1 minuto, até que esteja revestido com a manteiga e os cogumelos.
Despeje o vinho branco na panela e mexa até que o líquido seja absorvido pelo arroz.
Comece a adicionar o caldo de legumes, uma concha de cada vez, mexendo sempre e esperando que o líquido seja absorvido antes de adicionar mais caldo.
Continue esse processo até que o arroz esteja cozido, mas ainda al dente, cerca de 18-20 minutos.
Retire a panela do fogo e misture o queijo parmesão ralado e a manteiga restante.
Tempere com sal e pimenta a gosto e sirva imediatamente, polvilhado com salsinha fresca picada.''',
'''Em uma tigela, tempere os camarões com azeite de oliva, páprica, cominho em pó, alho em pó, pimenta caiena, sal e pimenta.
Aqueça uma frigideira grande em fogo médio-alto.
Adicione os camarões temperados à frigideira e cozinhe por cerca de 2-3 minutos de cada lado, até que fiquem rosados e cozidos.
Aqueça as tortilhas em uma frigideira seca até ficarem levemente douradas e flexíveis.
Monte os tacos colocando os camarões grelhados no centro de cada tortilha.
Adicione fatias de abacate, coentro fresco picado e molho de pimenta a gosto.
Sirva com quartos de limão para espremer sobre os tacos antes de comer.''',
'''Derreta o chocolate em banho-maria ou no micro-ondas, mexendo ocasionalmente até ficar completamente derretido e liso.
Em uma tigela grande, misture o chocolate derretido com o creme de leite até ficar homogêneo.
Em outra tigela, bata as claras de ovo em neve.
Adicione o açúcar às claras de ovo e continue batendo até formar picos firmes.
Com cuidado, incorpore as claras em neve à mistura de chocolate, mexendo delicadamente até que estejam completamente incorporadas.
Adicione a essência de baunilha e misture suavemente.
Divida a mousse entre taças individuais e leve à geladeira para firmar por pelo menos 2 horas.
Antes de servir, decore com raspas de chocolate.
Sirva gelado e aproveite!''',
'''Pré-aqueça o forno a 200°C.
Enxágue a quinoa em água corrente e escorra.
Em uma panela, leve a quinoa e a água ou caldo de legumes para ferver.
Reduza o fogo, tampe a panela e cozinhe por cerca de 15 minutos, ou até que a quinoa esteja macia e os líquidos tenham sido absorvidos.
Enquanto a quinoa cozinha, espalhe os legumes cortados em uma assadeira grande.
Regue os legumes com azeite''',
'''Preaqueça o forno a 180°C.
Comece preparando a calda: em uma forma de pudim, derreta o açúcar em fogo baixo, mexendo sempre, até que ele se dissolva e forme um caramelo dourado.
Com cuidado, espalhe o caramelo por toda a forma, girando-a para cobrir o fundo e as laterais.
Em seguida, prepare o pudim: no liquidificador, bata o leite condensado, o leite e os ovos até obter uma mistura homogênea.
Despeje a mistura do pudim na forma caramelizada.
Cubra a forma com papel alumínio e coloque-a em uma assadeira maior.
Leve ao forno em banho-maria, assando por cerca de 1 hora ou até que o pudim esteja firme, mas ainda ligeiramente tremeluzente no centro.
Retire o papel alumínio e deixe esfriar completamente antes de refrigerar por pelo menos 4 horas ou durante a noite.
Para desenformar, passe uma faca ao redor das bordas do pudim e vire-o sobre um prato grande.
Sirva gelado e delicie-se com esta sobremesa clássica.''',
'''Cozinhe o spaghetti em água fervente salgada de acordo com as instruções da embalagem, até ficar al dente.
Enquanto o spaghetti cozinha, frite o bacon em uma frigideira grande até ficar crocante.
Em uma tigela, bata as gemas de ovo com o queijo parmesão ralado e uma pitada de pimenta-do-reino.
Quando o spaghetti estiver pronto, escorra e reserve um pouco da água do cozimento.
Adicione o spaghetti à frigideira com o bacon e o azeite de oliva. Mexa bem.
Retire a frigideira do fogo e rapidamente adicione a mistura de gemas e queijo, mexendo vigorosamente para que o calor da massa cozinhe os ovos sem formar grumos.
Se necessário, adicione um pouco da água do cozimento reservada para obter uma consistência cremosa.
Tempere com sal e mais pimenta-do-reino, se desejar.
Sirva imediatamente, polvilhado com salsinha picada.'''
]

created_at = [
['12:14','22:45','13:07','14:54','55:23',
'06:19','07:25','08:15','17:59','19:08'
],
['24/12/2023','22/11/2023','12/10/2023','02/03/2023',
'03/02/2024','17/08/2023','18/09/2023','07/02/2024','29/01/2024','30/07/2023'
]
]

author = [
{'first_name': 'Sofia',
'last_name': 'Martins'},

{'first_name': 'Lucas',
'last_name': 'Pereira'},

{'first_name': 'Beatriz',
'last_name': 'Almeida'},

{'first_name': 'Pedro',
'last_name': 'Oliveira'},

{'first_name': 'Laura',
'last_name0': 'Costa'},

{'first_name': 'Gabriel',
'last_name': 'Santos'},

{'first_name': 'Isabela',
'last_name': 'Fernandes'},

{'first_name': 'Matheus',
'last_name': 'Silva'},

{'first_name': 'Mariana',
'last_name': 'Carvalho'},

{'first_name': 'Enzo',
'last_name': 'Rodrigues'}

]

category = [
    {'name': 'Italiana'},

    {'name': 'Mexicana'},
    
    {'name': 'Japonesa'},
    
    {'name': 'Indiana'},
    
    {'name': 'Chinesa'},
    
    {'name': 'Francesa'},
    
    {'name': 'Mediterrânea'},
    
    {'name': 'Brasileira'},
    
    {'name': 'Tailandesa'},
    
    {'name': 'Árabe'}
]

meal = [
    'Café da manhã','Almoço','Janta','Sobremesa','Lanche da tarde'
]

def rand_ratio():
    return f'{randint(840,900)}/{randint(473,573)}'

# fake = Faker('pt_BR')
# print(signature(fake.random_number))

def make_recipe():
    return {
        'title': title[randint(0,9)],
        'description': description[randint(0,9)],
        'preparation_time': preparation_time[randint(0,9)],
        'preparation_time_unit': 'Minutos',
        'servings': servings[randint(0,9)],
        'servings_unit': 'Porção',
        'preparation_steps': preparation_steps[randint(0,9)],
        'created_at': {
            'hour': created_at[0][randint(0,9)],
            'date': created_at[1][randint(0,9)]
        },
        'author': {
            'first_name': author[randint(0,9)].get('first_name'),
            'last_name': author[randint(0,9)].get('last_name')
        },
        # 'category': {
        #     'name': category[randint(0,9)]['name']
        # },
        'meal': meal[randint(0,4)],
        'cover': {
            'url': f'https://loremflickr.com/{rand_ratio()}/food,cook'
        }
    }
