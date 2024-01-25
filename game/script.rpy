# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mascoooot = Character("mascoooot", color="#80b0ff")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene background

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show sleepy face

    # These display lines of dialogue.

    mascoooot "UAAHHHH Que sono..."

    mascoooot "Tomar uma agua e dar uma olhada no meu email e o linkedisney."

    hide sleepy face    
    
    mascoooot "Que empresa é essa? Oppai-man?"

    show neutral face

    mascoooot "Não é aquela que faz jogos que da pra jogar ate com uma mão só?"

    mascoooot "Ah, é ela mesmo, sabia que eu tinha reconhecido esse nome..."

    mascoooot "Vamos ver os requisitos da vaga, sera que meus quase 3 anos de experiencia como dev eu tenho alguma chance?"

    scene background requisitos

    mascoooot "hmmmm"

    show happy face

    mascoooot "Eu pareco encaixar muitos dos requisitos..."

    mascoooot "Trabalhei 1 ano e meio desenvolvendo chatbots complexos pra grandes empresas utilizando javascript e .NET para o desenvolvimento das APIs."

    mascoooot "Isto demandava constantes consumos de Rest APIs como descrito na vaga..."

    mascoooot "Hoje trabalho numa fintech americana como desenvolvedor .NET"    

    mascoooot "E claro... tendo sempre que estar dentro das boas práticas de programaçao."

    mascoooot "E ainda tem um fato curioso sobre mim que joguei LoL profissionalmente por um tempo..."

    mascoooot "Tudo isso desenvolveu minhas habilidades de comunicação e trabalho em equipe com muitos erros e acertos durante esses anos."

    mascoooot "Mas tem um problema..."

    hide happy face

    mascoooot "Esta vaga é pra python :( :( :("
    
    mascoooot "E pra piorar"

    scene background over100

    show neutral face

    mascoooot "Essa vaga ja tem 5 dias e mais de 100 pessoas"

    menu actionChoice:
        "O que fazer?"
        "Easy Apply":
            jump easyApply
        "Pensar em algo":
            jump solution
        
    # This ends the game.

    return

label solution:

    scene background
    
    show neutral face

    mascoooot "Será que eu consiga fazer algo pra me destacar dos demais candidatos? Vamos olhar nos requisitos denovo..."

    scene background requisitos

    mascoooot "Aqui fala que os jogos são feitos usando essa engine Ren'Py que eu nunca ouvi falar."

    mascoooot "E também que é um conhecimento desejável porém não obrigatório para a vaga."

    mascoooot "Talvez eu consiga aprender o básico da engine bem rápido e desenvolva algo pra mostrar pra eles ja que meu curriculo ja está perdendo por nao ter python"

    scene background tutorial

    mascoooot "Vamos la..."

    hide neutral face

    scene background

    show happy face

    mascoooot "É isso!"

    mascoooot "Vou inventar alguma coisa bem simples pra mostar que eu aprendi o básico para a vaga e que estou demonstrando interesse, é melhor do que simplesmente dar easy apply"

    hide happy face

    narrator "Enfim foi criada uma simples visual novel..."

    scene background freshwomen
    mascoooot "Agora vou jogar alguma coisa pra relaxar e torcer"

label easyApply:

    scene background

    show neutral face

    mascoooot "A quer saber... vou mandar o easy apply aqui mesmo. Provavelmente não vou ser chamado por ser python, mas vai que..."

    hide neutral face

    narrator "Alguns dias depois..."

    show sleepy face

    mascoooot "Chegou um email aqui da Oppai-man"

    hide sleepy face

    scene background negado

    show neutral face

    mascoooot "..."

    hide neutral face

    show sleepy face

    mascoooot "Isso ja era esperado... vou dormir mais um pouco pois ainda estou com sono"

