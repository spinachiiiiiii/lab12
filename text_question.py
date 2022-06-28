from question import Question

Question1 = Question("Яка з бібліотек для написання телеграм-ботів використовує asyncio?",
                     ["python-telegram-bot", "Aiogram", "PyTelegramBotApi", "telebot"])
Question2 = Question("Яка функція використовується для перетворення Jinja2 шаблону в html-сторінку у Flask-додатках?",
                     ["render_html()", "print_template()", "app.route()", "render_template()"])
Question3 = Question("В якому об’єкті зберігаються значення між запитами окремого користувача до Flask-додатку?",
                     ["request", "route", "current_app", "session"])
Question4 = Question(
    "Яка інструкція в шаблонізаторі Jinja2 використовується для вказування на батьківський шаблон при успадкуванні?",
    ["extends", "set", "render", "import"])
Question5 = Question("Який об'єкт відслідковує стани і керує хендлерами в aiogram?",
                     ["Broker", "Mayor", "Dispatcher", "Master"])
Question6 = Question(
    "Який шлях (route) за замовчуванням завжди додається до списку шляхів, що містяться в атрибуті url_map примірнику Flask?",
    ["'app.py'", "'main.py'", "'/templates/index.html'", "'/static/<filename>'"])
Question7 = Question(
    "В якому каталозі за замовчуванням зберігаються CSS, JavaScript та файли шрифтів в Flask-додатках?",
    ["static", "css", "app", "flask_app"])
Question8 = Question("Який шаблонізатор за замовчуванням використовується веб-фреймворком Flask?",
                     ["Genshi", "Jinja2", "Handelbars", "Smarty"])
Question9 = Question("Якою конструкцією визначаються вирази в шаблонізаторі Jinja2 ?",
                     ["{{ }}", "{%  %}", "# #", "{# #}"])
Question10 = Question(
    "Стандарт, що визначає API Python для доступу до баз даних різного типу і використовуєтсья у SQLALchemy називається:",
    ["SQLite", "PyAPI", "SQLAlchemyAPI", "DBAPI"])

questions = [Question1, Question2, Question3, Question4, Question5, Question6, Question7, Question8, Question9,
             Question10]
answers = ["Aiogram",
           "render_template()",
           "session",
           "extends",
           "Dispatcher",
           "'/static/<filename>'",
           "static",
           "Jinja2",
           "{{ }}",
           "DBAPI"]
patter_for_true = ["Right answer\u2714", "Wowww,you good today!", "Good.Continue on the same way!\u2705",
                   "Niceeeeeee,strong knowledge\u2714"]
patter_for_false = ["False", "Try again\u2716", "Not today", "It is not correct"]
