import random

k1=['Привет, подскажи, пожалуйста, где здесь можно вкусно покушать?.. '
    'Окей, хотя на самом деле это был просто адекватный повод с тобой познакомиться!) '
    'Сказал первое, что пришло в голову)',
    'Слушай, как лучше всего проехать на станцию метро «Золотая Роща» (несуществующая станция) … '
    'Нет такой? Да шучу, просто ты показалась мне интересной, решил с тобой пообщаться!',
    'Привет, есть разменять 500 рублей? В киоске не принимают карты, как они живут вообще…',
    'Ты чего так холодно оделась, совсем здоровье не бережешь (если холодно, зима)',
    'Привет! Парня ждешь? .. Он не придет :) (девушки, стоящей и ожидающей кого-то)',
    'Думаю не стоит мокнуть под дождем… (подходишь с зонтом)',
    'Привет, подскажи где здесь метро? (ее ответ) На самом деле мне туда не надо) '
    'Просто не знал, как с тобой заговорить)',
    'Подскажи, пожалуйста, где здесь фонтан с девушкой - это место, где обычно встречи назначают? ... '
    'Просто ко мне друг приехал, он тут в последний раз 10 лет назад был, говорит, что стоит у фонтана с девушкой…'
    'Кстати, ты хорошо выглядешь, как тебя зовут!',
    'Привет, во, погоди минутку, нужен твой женский совет! '
    'Я сейчас прохожу тренинг по стилю, и мне нужно узнать у незнакомых людей, '
    'что мне можно улучшить в своем внешнем виде! Ты довольно приятно выглядишь, '
    'поэтому можешь что-то дельное посетововать!...',
    'Привет, а где здесь бургерная? (ее ответ) Спасибо. Слушай, будет глупо, если ты вот так уйдешь, '
    'хотя мы бы могли с тобой познакомиться.',
    'О, подскажи, пожалуйста, это что за улица?... Советская?! И ты не боишься, '
    'что к тебе на улице Советской подойдет незнакомый молодой человек и вот так с тобой познакомиться? '
    'Нет? Ну тогда будем знакомы;)',
    'Привет, я подумал ты мне можешь посоветовать… где тут в округе можно попить хорошего кофе?... '
    'А то мой друг задерживается, погода, как видишь, пасмурная. А как тебя зовут?... '
    'Очень приятно – у тебя будет полчаса, чтобы я угостил тебя кофе в этом кафе? Соглашайся, ничего не знаю…)',
    'Подскажи, где тут вход в метро? … А ты в ту сторону идешь, будет здорово, если ты меня проводишь! ',
    'Привет, слушай, не знаешь, где здесь кормят вкусной и здоровой пищей? Что-нибудь вегитарианское? ;) '
    'Кстати, я предлагаю не упускать такого прекрасного момента и прямо сейчас познакомиться!',
    'Ой, помоги, пожалуйста. Я только что уронил свой телефон, у тебя есть телефон, проверим как он работает теперь?',
    'Девушка, подскажите, пожалуйста, где здесь новая «Чашка кофе» открылась?… (ее ответ) '
    'И разве я найду там такую же милую девушку, как ты?;)',
    'Привет. Слушай, посоветуй, пожалуйста! Может быть, ты знаешь здесь какое-нибудь оригинальное кафе? '
    'Для свидания с девушкой;)  …  А что именно там интересного? … Это отлично! Наконец-то я нашел кафе, '
    'где мы с тобой можем замечательно провести время!',
    'Если толпа, то подойди как можно ближе и наступи ей на ногу. Или не ей, но извинись перед ней:)',
    'Привет, подскажи, как пройти к парку? (ее ответ)А не знаешь, там есть такие же милые девушки как ты?;)',
    'Привет, слушай, у меня новый номер, но я его не знаю. '
    'Ты можешь мне помочь – набери себе, чтобы мой номер высветился. '
    '(Потом говоришь, что отлично, я тебе наберу...)',
]

k2=['Клевая вечеринка!.. Как настроение? Как семья, как дети, как внуки?)',
    'Привет) вы чего так рано в клуб пришли? Я смотрю еще народу маловато…',
    'Видела, как те парни подрались!? Наверное, из-за девушки?',
    'Привет! Где тут чиллаут?',
    'Слушай, что за парень только что к тебе подходил? Мне кажется он маньяк! '
    '(ты заметил неудачный подход другого парня)',
    'Что за DJ? Клево играет =D',
    'Не знаешь, здесь можно будет по карте рассчитаться?',
    'Девушка, выручите, пожалуйста, мне срочно нужна одна вещь… возможно у вас найдется… '
    'Вообщем… есть тампон или прокладка? ;) … Нда, да ладно, я просто так решил проверить твое чувство юмора! '
    'Как настроение)',
    'Ай, зачем ты это сделала? (она случайно наступила тебе на ногу или толкнула, кстати, скорее всего неслучайно;))',
    'Привет! Мы тут снимаем девушек! Поможешь!?)',
    'Привет! У тебя меню? Давай, посоветуй мне чего взять выпить?',
    'Подход Горо (подходишь, прячясь за друга и из-за него начинаешь лапать девушку, типа у него 4 руки)',
    'Ты такая хорошенькая! (и обнимаешь)',
    'Девушка тыкает в телефон - подходишь и начинаешь делать тоже самое, тыкая своим телефоном в нее. '
    'Прикалываешься: «Самое время полистать инстаграмм…)»',
    'Что пьешь? Что взять?',
    'Ты - клевая! (показать это невербально, затем подойти и проговорить, взять за руку!)',
    'Эй! Я тебя раньше не видел! Ты что под конец вечеринки пришла? Уже все на авте-пати уехали!',
    'Я сейчас познакомлю тебя с этим парнем! (толкаешь в плечо дрочера, который прошел мимо, '
    'хотя мог бы с ней заговорить)',
    'Ооооооу, тут всегда бармены такие медлительные?',
]

k3=['Не знаешь кто это поет? У меня без названия (если слушаешь музыку в наушниках)',
    'Попросить помочь написать смс, показать на экране «Привет. Еду сейчас в метро, '
    'рядом сидит довольно милая девушка. Как думаешь, стоит ли познакомиться с ней или подождать, '
    'пока она сама?)». И дал телефон ей.',
    'Послушай, а если я сяду в первый вагон, я доеду до станции "Березовая роща"? '
    'А если сяду в последний? А если вместе с тобой?;)',
    'Просто выйди с ней на ее остановке и открой любой фразой для знакомств на улице',
    'Как ты считаешь, в каком вагоне поезда лучше ехать?... ;) '
    'Ну… в центральном меньше народу, в первом – едешь ты… Я прям разрываюсь ;)',
    'Показать текст на экране телефона – «Привет, слушай, заметил тебя и точно знаю, '
    'что уснуть не смогу, если сейчас ВОТ ТАК с тобой не познакомлюсь :)»',
    'Слушай, а это какой автобус?.. Там будет остановка «Площадь Ленина»? '
    'Кстати, ты довольно доброжилательная, хорошо что есть такие люди)',
    'Что там такое слушаешь?:) (она слушает музыку в наушниках, невербально показываешь «сними»)',
]

k4=['Привет, слушай, у меня новый номер, но я его не знаю. '
    'Ты можешь мне помочь – набери себе, чтобы мой номер высветился. (Потом говоришь, что отлично, я тебе наберу)',
    'Слушай, можно минуту твоего внимания, совет нужен! Понимаешь, у меня есть лучший друг, у него есть девушка. '
    'Так вот я узнал, что она ему недавно изменила и теперь я не знаю – стоит ли рассказывать ему про это? '
    'Все-таки это их личные отношения…',
    'Привет, девчонки, нужен ваш совет! Вот мы тут с друзьями спорим по поводу такой ситуации… '
    'Вообщем, как думаете, если у девушки есть парень, но она ходит в клубы и целуется там с другими парнями – '
    'это считается за измену или нет? При этом она говорит, что это просто развлечение и ничего такого… '
    'А если она целуется там с девушками?)',
    'Привет! Девчонки, выручайте! Смотрите, мы вон там сидим с моим другом, и на него постоянно поглядывает '
    'вон та девушка. Мы ее не знаем. Видите она с парнем сидит, у них похоже свидание! Что бы это значило?',
    'Слушай, не подскажешь - почему все девушки в тайне мечтают взять гамбургер, но в итоге заказывают салатик?',
    'Ой, помоги, пожалуйста. Я только что уронил свой телефон, у тебя есть телефон, проверим как он работает теперь?',
    'Привет, девушки! Слушайте прикол, видите вот ту парочку, которая сидит за тем столиком? '
    'Дело в том, что тот парень постоянно на вас смотрит, а его девушка это видит и нервничает! '
    'Поэтому мы решили вот что – мы сейчас сделаем вид, что мы ваши парни ;) По-моему это очень хорошее дело!;)',
    'Привет, разрешите минуту вашего внимания ;) Не знаешь где тут мне найти красивых девушек?) … '
    'Да шучу, это просто проверка, насколько ты интересная ;) Как тебя зовут?;)',
    'Привет, скажите, не от вашего столика так вкусно пирожками пахнет?',
    'Мне нужно женское мнение. Мой друг встречается с девушкой всего месяц, и она сама звонит ему каждый вечер. '
    'Как ты думаешь, должна девушка проявлять инициативу?',
    'Привет-привет, вот вы то мне и нужны! ;) Как вас зовут?... Отлично, ну и как вам это заведение? … '
    'Почему вы сюда ходите, а не в другое? … Мне тоже тут нравится…;)',
    'Я рекомендую заказать салат с рукколой (девушка листает меню)',
    'Привет. Слушай, моему другу понравилась подруга, как бы нам их познакомить?)',
    'Записка через официанта или самому проходя мимо: На самом деле ты мне показалась интересной, '
    'и мы могли бы вот так познакомиться. Напиши свое согласие или несогласие, выбрав один из этих вариантов: '
    '«Да, давай познакомимся», «Нет, извини, я занята», «Пошел нафиг» или '
    '«Напиши ниже свой вариант идеального знакомства» :)',
]

k5=[
    'Я выбираю подарок для своей сестры, не могла бы ты меня проконсультировать?',
    'Сделай вид, что интересуешься тем же товаром, что и она, затем прокомментируй.',
    'Привет, слушай, у меня новый номер, но я его не знаю. Ты можешь мне помочь – '
    'набери себе, чтобы мой номер высветился. (Потом говоришь, что отлично, я тебе наберу)',
    'Вот это продается значительно дешевле в другом магазине (девушка выбирает вещь в уличном лотке или магазине)',
    'Девушка, я тоже люблю фрукты и за здоровый образ жизни. Думаю у нас много общего, '
    'давай познакомимся! (Девушка покупает фрукты)',
    'В очереди прокомментируй ее выбор или спроси ее мнение о выбранном тобой товаре.',
    'Привет, во, погоди минутку, нужен твой женский совет! Я сейчас прохожу тренинг по стилю, и мне нужно '
    'узнать у незнакомых людей, что мне можно улучшить в своем внешнем виде! Ты довольно приятно выглядишь, '
    'поэтому можешь что-то дельное посетововать!...',
]

k6=['Слушай, а что это за музыканты? (в парке танцуют уличные мызыканты, собралась толпа)',
    'Так, стоять! Служба контроля качества девушек города Москвы.',
    'Привет… Как ваше замечательное настроение?',
    'Слушай, объясни, пожалуйста, моему другу, где я сейчас нахожусь… » - '
    'даешь ей трубку. На другом конце тренер или твой друг говорят ей, чтобы она бежала от '
    'тебя, что ты маньяк и просто разводишь ее ;) Фан, всем весело!',
    'Привет! А вы чего так поздно гуляете по парку?',
    'Привет! Можешь сфотографировать меня? (возле достопримечательности, далее можно сфоткать ее)',
    'У вас свободно? (подсаживаемся на лавочку) Как настроение в столь чудный летний денек?)',
]

k7=['У тебя такой загар, как давно здесь?',
    'Привет, а есть у тебя крем для загара? кстати как правильно - крем от загара или для загара?…',
    'Как водичка? (она выходит на берег после купания)',
    'Ой, девчонки, а посторожите мое полотенце, пока я купаюсь! Только внимательнее с ним, это мне бабушка подарила;)',
    'Привет, я заметил у тебя прикольный купальник, хорошо фигуру подчеркивает, '
    'как такая модель называется? (Клевый купальник, это что за модель? Назад в 90-е?)',
    'Лови! (кидаешь мяч)',
    'Слушай, ты так плавала сейчас, я думал ты тонешь! Или ты придумала новый стиль плавания?)',
]

k8=['Привет, мне стало интересно как ты отреагируешь на искренний комплимент от незнакомого парня? (Окей, ты первая))',
    'Привет! Не мог пройти мимо и не сказать, что… черт, ты классно выглядишь ;) '
    'Тебе, наверное, парни проходу не дают? ;)',
    'Привет! ну и где??? Где сотни твоих поклонников, которые должны облепить тебя со всех сторон))',
    'Привет. Слушай, мне стало интересно, а в душе ты такая же привлекательная как снаружи?)',
    'Привет, я тебя заметил и хочу сказать, что у тебя очень классная прическа (кудряшки, косички)…',
    'Привет. Возможно тебя это удивит, но я посмотрел вокруг и понял, что ты единственная девушка в этом кафе, '
    'с кем мне стоит познакомиться (единственные девушки в этом кафе, с кем нам стоит познакомиться).',
    'Привет, увидел тебя и решил, что нам с тобой нужно обязательно познакомиться. '
    'Представь, мы бы прошли мимо друг друга и так бы больше никогда не встретились)',
    'Привет… ммм… я просто хотел сказать тебе ... (пауза), что ты действительно сногсшибательная девушка. '
    'Я хочу с тобой познакомиться ;)',
    'Привет. Заметил, у тебя очень красивые ресницы, ты, наверное, очень дорогой тушью пользуешься... ;)',
    'Слушай, случайно заметил тебя на выходе, и просто не смог пройти мимо. '
    'Хочу сказать, что ты отличаешься от остальных девушек, поэтому предлагаю познакомиться',
    'Привет, не могу пройти мимо и не сказать тебе, что эта твоя сумка (твой шарф) классно тебе подходит… '
    'Это не как обычно девушки носят…',
    'Привет… ммм… я просто хотел сказать тебе ... (пауза), что ты действительно сногсшибательная девушка. '
    'Я хочу с тобой познакомиться ;)',
]

k9=['Привет, слушай, у меня новый номер, но я его не знаю. '
    'Ты можешь мне помочь – набери себе, чтобы мой номер высветился. '
    '(Потом говоришь, что отлично, я тебе наберу...)',
    'Эй, скажите, это не у вас из сумочки так вкусно пирожками пахнет?',
]


def answer(kat):
    match kat:
        case "Улица":
            return random.choice(k1)
        case "Клуб":
            return random.choice(k2)
        case "Транспорт":
            return random.choice(k3)
        case "Кафе":
            return random.choice(k4)
        case "ТЦ":
            return random.choice(k5)
        case "Парк":
            return random.choice(k6)
        case "Пляж":
            return random.choice(k7)
        case "Директ":
            return random.choice(k8)
        case "Разное":
            return random.choice(k9)