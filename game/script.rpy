define Hiro = Character('Хиро', color="#00ff00")
define Minato = Character('минато', color='#0000ff')
define Aiko = Character('Aiko', color='#ff1a1a')
label start:
    scene new
    with fade
    #в этом диалоге должен быть минато, но спрайты отсутствуют.
    Hiro "Настало первое сентября и преход в одинацатый класс. Печально осозновать что только несколько моих однокласников продолжили учебу."
    Hiro "Кто-то радуется, кто-то нет, но наш классный руководитель как обычно озвучивает одну и туже речь. {w} Из года в год..."
    Minato "Хиро, что задумался? {w} Радоваться надо."
    Hiro "Не обращай внимание. А почему радоваться? Разве работы не прибавится? одинацатый клас как никак."
    Minato "С этим я согласен, работы прибавится. Всетаки последний год школы."
    Hiro "(И на этих словах я опять пересал кого либо слышать, уйдя в раздумия как пройдет этот год? Что с нами случится? И как наши пути разойдутся?)"

    #этот момент прозвенел звонок из-за чего Хиро уходит из раздумий
    #звук школьноко звонка(колокола)
    Hiro "(И вот прозвенел звонок и я снова ушел от своих раздумий {w} Учитель как всегда приходит вовремя)"

    #в этот момент должны быть спрайты учеников на заднем плане
    Hiro "(Все уроки проходят как это было и раньше. {w} И вот прозвенел доолгожданный звонок о завершении уроков на сегодня)
    {w} (Все начали собриться, обсуждать куда зайдут по пути домой, но предстоит добраться домой и отдохнуть от ежедневней рутины и окружающего мня шума)"

label street:
    scene street
    with fade

    Hiro "(Половина пути пройдена. {w} Может посетить кафе?)"

    #В этот момент перед игроком должен появится выбор (посетить кафе или нет) что запустит одну из сюжетных веток

    menu:
        "Посетить кафе?"

        "Посетить":
            jump cafe

        "Пройти":
            jump home


    return

    #Хиро удет домой и начнется другая ветка

label home:
    scene street
    Hiro "(Пожалуй заходить не буду, лучше поскорее прийти домой)"
    Hiro "(Я не сильный поклонник таких заведений {w} и бываю в них редко.)"
    jump home1

    return

    #Хиро удет домой

label home1:
    scene home 1
    Hiro "(Вот я и дома, нужно будет прибраться чтобы спокойно отдахнуть.)"
    jump room

    return

    #Хиро находится у себя в комнате
    #Есть хорошая идею написать о его сне который ему преснится, что позволит задействовать один из поворотов событий или пасхалка игроку

label room:
    scene room
    Hiro "(Уборка закончена. {w} Теперь я мошу получить свой честно заслуженный отдых.)"

    return

    #Хиро зайдет в кафе
    #тут должен быть спрайт Айко

label cafe:
    scene cafe
    Hiro "(Чашечка кофе поможет мне взбодриться за день и развеять усталость)"
    Hiro "(Вроде хорошое кафе, присяду возле окна.)"
    Aiko "Да, я скоро буду дома, только я не знаю как найти эту улицу. {w} Жить в новом городе будет не просто."
    Hiro "(За соседнем стольком девушка разговаривает по телефону, видно не местная.)"
    Hiro "(Посижу еще пару минут и пойду домой. Все таки чашечка кофе немного развеяла мою усталость.)"
    Aiko "Извини."
    Hiro "(Девушка которая разговаривала по телефону обратилась ко мне за помощью)"
    Hiro "Это была довольно красивая девушка с хорошой фигурой, приятным лицом и длинными светлыми волосами."
    Hiro "Чем могу помочь?"
    Aiko "Не подскажешь как добраться до района Сакай?"

    menu:
        "Помочь девушке?"

        "Провести её":
            jump not_in_cafe

        "Отказать и остаться в кафе":
            jump in_cafe

    return

    #Хиро поможет и они уйдут из кафе
    #помошь Айко +1 к её концовке

label not_in_cafe:
    scene cafe
    Hiro "Я точно рассказать как пройти в этот район не смогу{w}, но могу провести тебя мне по пути."
    Aiko "Я буду рада если тебя это не затруднит."
    Hiro "Не затруднит. Ты готова идти?"
    Aiko "Да."
    Hiro "Тогда в путь."
    jump not_cafe

    return

    #Хиро отказал в помоши и остался в кафе
label in_cafe:
    scene cafe
    Hiro "Извини ни чем помочь не смогу."
    Aiko "Ладно, извини за беспокойство."
    Hiro "(Не сильно хотелось жертвовать своим временем.)"
    Hiro "(Время пролетело быстро я даже и не заметил как прошло пол часа. {w} Пора идти.)"
    jump go_home


    #Хиро уже пришол домой после отказа
label go_home:
    scene home
    Hiro "(Вот я и дома.)"
    Hiro "(Все таки жалко что я не помг той девушке)"

    return

    #Хиро провожает Айко и начинает диалог
    #спрайт Айко
label not_cafe:
    scene street3
    Hiro "(С того момента как мы уушли от кафе так никто не начал диалог. {w} Возьму инициативу на себя.)"
    Hiro "Тебя как зовут? Даже имени своего не сказала."
    Aiko "А ой, извини. {w} Айко Сидзуне, можено просто Айко."
    Aiko "А тебя?"
    Hiro "Хиро Сато"
    Hiro "Ты не местная? Ты удевленно смотришь на окружение."
    Aiko "Можно сказать и так. {w} Я ученица по переводу, и теперь буду жить здесь."
    Hiro "(Значит ученица по переводу... Значит есть вероятность что она попадет в нашу школу Икадзава так как она находится ближе всего к району Сакай...)"
    Hiro "(Может спросить знает ли она дорогу до школы...)"
    Hiro "Ты в какой школе будешь обучаться?"
    Aiko "Вроде бы в Икадзаве. {w} Только я не знаю как пройти до неё. {w} А почему спрашиваешь."
    Hiro "Просто подумал что ты можешь и не найти её так как ты не местная."

    return
