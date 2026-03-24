from database import SessionLocal, engine, Base
from models import Product

Base.metadata.create_all(bind=engine)


def seed_products():
    db = SessionLocal()

    # Очистити таблицю перед новим заповненням
    db.query(Product).delete()
    db.commit()

    products = [
        # =========================
        # ОСНОВНЕ МЕНЮ -> ХОЛОДНІ ЗАКУСКИ
        # =========================
        Product(name="Овочеве асорті", description="огірки, помідори, перець", weight="200 г", price=200, category="Основне меню", subcategory="Холодні закуски"),
        Product(name="М'ясне асорті", description="шинка, ковбаса домашня, салямі", weight="250 г", price=300, category="Основне меню", subcategory="Холодні закуски"),
        Product(name="Сирне асорті", description="", weight="200 г", price=400, category="Основне меню", subcategory="Холодні закуски"),
        Product(name="Гостре асорті", description="мариновані огірки, помідори, гриби", weight="250 г", price=250, category="Основне меню", subcategory="Холодні закуски"),
        Product(name="Огірки мариновані", description="квашені", weight="150 г", price=120, category="Основне меню", subcategory="Холодні закуски"),
        Product(name="Язик з хріном", description="", weight="100 г", price=300, category="Основне меню", subcategory="Холодні закуски"),
        Product(name="Закуска з печінки", description="", weight="150 г", price=180, category="Основне меню", subcategory="Холодні закуски"),
        Product(name="Роли з лососем", description="", weight="250 г", price=280, category="Основне меню", subcategory="Холодні закуски"),
        Product(name="Рибна тарілка", description="", weight="200 г", price=500, category="Основне меню", subcategory="Холодні закуски"),
        Product(name="Сало по-домашньому", description="", weight="100 г", price=130, category="Основне меню", subcategory="Холодні закуски"),
        Product(name="Сир в фритюрі", description="", weight="150 г", price=200, category="Основне меню", subcategory="Холодні закуски"),
        Product(name="Закуска козацька", description="", weight="100 г", price=150, category="Основне меню", subcategory="Холодні закуски"),
        Product(name="Оселедець", description="", weight="200 г", price=180, category="Основне меню", subcategory="Холодні закуски"),
        Product(name="Оливки", description="", weight="100 г", price=100, category="Основне меню", subcategory="Холодні закуски"),
        Product(name="Хліб", description="", weight="40 г", price=4, category="Основне меню", subcategory="Холодні закуски"),
        Product(name="Грінки", description="", weight="6 шт", price=80, category="Основне меню", subcategory="Холодні закуски"),

        # =========================
        # ОСНОВНЕ МЕНЮ -> САЛАТИ
        # =========================
        Product(name="Салат Королівський", description="курка, ананас, кукурудза, яйце, перець, арахіс, цибуля пориста, майонез", weight="250 г", price=160, category="Основне меню", subcategory="Салати"),
        Product(name="Салат Марта", description="курка, виноград, сир твердий, гриби, перець, майонез", weight="230 г", price=160, category="Основне меню", subcategory="Салати"),
        Product(name="Салат Фірмовий", description="курка, гриби, квасоля, цибуля, майонез", weight="250 г", price=150, category="Основне меню", subcategory="Салати"),
        Product(name="Салат Грецький", description="помідори, огірки, сир фета, оливки, перець, цибуля, олія", weight="250 г", price=180, category="Основне меню", subcategory="Салати"),
        Product(name="Салат Шопський", description="огірки, помідори, перець, сир твердий, цибуля, майонез", weight="150 г", price=160, category="Основне меню", subcategory="Салати"),
        Product(name="Салат з блакитним сиром та апельсином", description="", weight="350 г", price=300, category="Основне меню", subcategory="Салати"),
        Product(name="Салат з креветками та авокадо", description="", weight="250 г", price=320, category="Основне меню", subcategory="Салати"),
        Product(name="Салат теплий з печінки", description="", weight="250 г", price=240, category="Основне меню", subcategory="Салати"),
        Product(name="Буряк & Фета", description="", weight="200 г", price=150, category="Основне меню", subcategory="Салати"),
        Product(name="Буряковий настрій", description="чорнослив, горішки", weight="200 г", price=130, category="Основне меню", subcategory="Салати"),
        Product(name="Салат Цезар з куркою", description="", weight="350 г", price=290, category="Основне меню", subcategory="Салати"),
        Product(name="Салат Цезар з лососем", description="", weight="350 г", price=320, category="Основне меню", subcategory="Салати"),
        Product(name="Салат Капрезе", description="моцарелла, помідори, базилік", weight="200 г", price=250, category="Основне меню", subcategory="Салати"),
        Product(name="Салат з тунцем", description="салатний мікс, тунець, огірок, кукурудза", weight="250 г", price=280, category="Основне меню", subcategory="Салати"),
        Product(name="Салат з свіжої капусти", description="", weight="150 г", price=100, category="Основне меню", subcategory="Салати"),
        Product(name="Салат з квашеної капусти", description="", weight="200 г", price=100, category="Основне меню", subcategory="Салати"),
        Product(name="Салат Вінігрет", description="", weight="250 г", price=180, category="Основне меню", subcategory="Салати"),
        Product(name="Салат Олів'є", description="", weight="200 г", price=180, category="Основне меню", subcategory="Салати"),
        Product(name="Салат з телятини", description="теплий / холодний", weight="250 г", price=280, category="Основне меню", subcategory="Салати"),
        Product(name="Салат овочевий", description="", weight="200 г", price=150, category="Основне меню", subcategory="Салати"),
        Product(name="Оселедець під шубою", description="", weight="200 г", price=200, category="Основне меню", subcategory="Салати"),
        Product(name="Салат по-домашньому", description="", weight="100 г", price=130, category="Основне меню", subcategory="Салати"),

        # =========================
        # ОСНОВНЕ МЕНЮ -> ПЕРШІ СТРАВИ
        # =========================
        Product(name="Солянка", description="", weight="300 г", price=150, category="Основне меню", subcategory="Перші страви"),
        Product(name="Борщ український", description="", weight="300 г", price=110, category="Основне меню", subcategory="Перші страви"),
        Product(name="Юшка грибна", description="", weight="300 г", price=150, category="Основне меню", subcategory="Перші страви"),
        Product(name="Суп з фрикадельками", description="", weight="300 г", price=100, category="Основне меню", subcategory="Перші страви"),
        Product(name="Уха з трьох риб", description="", weight="500 г", price=160, category="Основне меню", subcategory="Перші страви"),
        Product(name="Бограч", description="", weight="500 г", price=190, category="Основне меню", subcategory="Перші страви"),
        Product(name="Бульйон курячий", description="", weight="300 г", price=100, category="Основне меню", subcategory="Перші страви"),

        # =========================
        # ОСНОВНЕ МЕНЮ -> ГАРЯЧІ СТРАВИ
        # =========================
        Product(name="Деруни по-галицьки", description="деруни, м'ясна підлива", weight="350 г", price=170, category="Основне меню", subcategory="Гарячі страви"),
        Product(name="Деруни по-гоцульськи", description="деруни, грибна підлива", weight="350 г", price=150, category="Основне меню", subcategory="Гарячі страви"),
        Product(name="Дерун колобок", description="", weight="350 г", price=180, category="Основне меню", subcategory="Гарячі страви"),
        Product(name="Дерун смачна кишенька", description="", weight="350 г", price=200, category="Основне меню", subcategory="Гарячі страви"),
        Product(name="Деруни з грибами", description="", weight="240/40 г", price=150, category="Основне меню", subcategory="Гарячі страви"),
        Product(name="Деруни з сметаною", description="", weight="240/40 г", price=140, category="Основне меню", subcategory="Гарячі страви"),
        Product(name="Банош", description="", weight="350 г", price=170, category="Основне меню", subcategory="Гарячі страви"),
        Product(name="Телятина на подушці з грибів", description="", weight="200 г", price=280, category="Основне меню", subcategory="Гарячі страви"),
        Product(name="Чанахи", description="м'ясо, картопля, квасоля, морква, цибуля", weight="500 г", price=200, category="Основне меню", subcategory="Гарячі страви"),
        Product(name="Печінка тушкована", description="", weight="200 г", price=180, category="Основне меню", subcategory="Гарячі страви"),
        Product(name="Короп в сметані", description="", weight="1 кг", price=700, category="Основне меню", subcategory="Гарячі страви"),
        Product(name="М'ясо з ананасами", description="на вагу", weight="100/50/5 г", price=100, category="Основне меню", subcategory="Гарячі страви"),
        Product(name="М'ясо по-французьки", description="на вагу", weight="100/10/5 г", price=100, category="Основне меню", subcategory="Гарячі страви"),
        Product(name="Відбивна свинна", description="на вагу", weight="100 г", price=100, category="Основне меню", subcategory="Гарячі страви"),
        Product(name="Відбивна куряча", description="на вагу", weight="100 г", price=100, category="Основне меню", subcategory="Гарячі страви"),
        Product(name="Відбивна теляча", description="на вагу", weight="100 г", price=150, category="Основне меню", subcategory="Гарячі страви"),
        Product(name="Нагетси", description="", weight="180 г", price=150, category="Основне меню", subcategory="Гарячі страви"),
        Product(name="Крученик по-галицьки", description="свинний / курячий", weight="200 г", price=200, category="Основне меню", subcategory="Гарячі страви"),
        Product(name="Жульєн по-домашньому", description="", weight="210 г", price=120, category="Основне меню", subcategory="Гарячі страви"),
        Product(name="Жульєн з білими грибами", description="", weight="210 г", price=180, category="Основне меню", subcategory="Гарячі страви"),
        Product(name="Форель фарширована овочами", description="", weight="100 г", price=110, category="Основне меню", subcategory="Гарячі страви"),
        Product(name="Риба дорадо / сібас", description="", weight="100 г", price=110, category="Основне меню", subcategory="Гарячі страви"),
        Product(name="Стейк лосося", description="", weight="100 г", price=180, category="Основне меню", subcategory="Гарячі страви"),
        Product(name="Стейк з коропа", description="", weight="100 г", price=120, category="Основне меню", subcategory="Гарячі страви"),
        Product(name="Рибне філе з овочами", description="", weight="100 г", price=120, category="Основне меню", subcategory="Гарячі страви"),
        Product(name="Мисливські ковбаски", description="", weight="100 г", price=140, category="Основне меню", subcategory="Гарячі страви"),
        Product(name="Курячі крильця в меді", description="", weight="100 г", price=100, category="Основне меню", subcategory="Гарячі страви"),
        Product(name="Куряча грудка з базиліком", description="", weight="100 г", price=150, category="Основне меню", subcategory="Гарячі страви"),
        Product(name="Картопля по-селянськи", description="", weight="200 г", price=100, category="Основне меню", subcategory="Гарячі страви"),
        Product(name="Картопля фрі", description="", weight="200 г", price=90, category="Основне меню", subcategory="Гарячі страви"),
        Product(name="Картопля відварна", description="", weight="200 г", price=80, category="Основне меню", subcategory="Гарячі страви"),
        Product(name="Рис з овочами", description="", weight="200 г", price=110, category="Основне меню", subcategory="Гарячі страви"),
        Product(name="Рулька в пиві", description="", weight="1 кг", price=600, category="Основне меню", subcategory="Гарячі страви"),
        Product(name="Пельмені", description="", weight="200/10 г", price=180, category="Основне меню", subcategory="Гарячі страви"),
        Product(name="Вареники з капустою", description="", weight="200/50 г", price=130, category="Основне меню", subcategory="Гарячі страви"),
        Product(name="Вареники з картоплею зі сметаною", description="", weight="200/50 г", price=120, category="Основне меню", subcategory="Гарячі страви"),
        Product(name="Вареники з картоплею та грибною підливою", description="", weight="200/50 г", price=130, category="Основне меню", subcategory="Гарячі страви"),
        Product(name="Омлет з шинкою", description="", weight="150 г", price=120, category="Основне меню", subcategory="Гарячі страви"),
        Product(name="Омлет звичайний", description="", weight="120 г", price=90, category="Основне меню", subcategory="Гарячі страви"),
        Product(name="Омлет мозаїка", description="", weight="150 г", price=100, category="Основне меню", subcategory="Гарячі страви"),
        Product(name="Налисники з сиром та варенням", description="", weight="150 г", price=120, category="Основне меню", subcategory="Гарячі страви"),
        Product(name="Налисники з яблуком", description="", weight="180 г", price=100, category="Основне меню", subcategory="Гарячі страви"),
        Product(name="Налисники з м'ясом та грибною підливою", description="", weight="180 г", price=170, category="Основне меню", subcategory="Гарячі страви"),
        Product(name="Налисники з капустою та грибною підливою", description="", weight="180 г", price=140, category="Основне меню", subcategory="Гарячі страви"),
        Product(name="Сирники", description="", weight="180 г", price=150, category="Основне меню", subcategory="Гарячі страви"),
        Product(name="Соус до шашлика", description="", weight="70 г", price=40, category="Основне меню", subcategory="Гарячі страви"),
        Product(name="Кетчуп", description="", weight="50 г", price=40, category="Основне меню", subcategory="Гарячі страви"),

        # =========================
        # ОСНОВНЕ МЕНЮ -> СТРАВИ НА МАНГАЛІ
        # =========================
        Product(name="Шашлик свинний з філе", description="", weight="100 г", price=130, category="Основне меню", subcategory="Страви на мангалі"),
        Product(name="Шашлик свинний", description="", weight="100 г", price=100, category="Основне меню", subcategory="Страви на мангалі"),
        Product(name="Шашлик курячий", description="", weight="100 г", price=100, category="Основне меню", subcategory="Страви на мангалі"),
        Product(name="Стейк свинний", description="", weight="100 г", price=95, category="Основне меню", subcategory="Страви на мангалі"),
        Product(name="Ребра свинні", description="", weight="100 г", price=85, category="Основне меню", subcategory="Страви на мангалі"),

        # =========================
        # ОСНОВНЕ МЕНЮ -> ОВОЧІ ГРИЛЬ
        # =========================
        Product(name="Перець болгарський", description="", weight="100 г", price=60, category="Основне меню", subcategory="Овочі гриль"),
        Product(name="Помідор", description="", weight="100 г", price=60, category="Основне меню", subcategory="Овочі гриль"),
        Product(name="Баклажан", description="", weight="100 г", price=60, category="Основне меню", subcategory="Овочі гриль"),
        Product(name="Кабачок", description="", weight="100 г", price=60, category="Основне меню", subcategory="Овочі гриль"),
        Product(name="Печериці", description="", weight="100 г", price=70, category="Основне меню", subcategory="Овочі гриль"),
        Product(name="Асорті гриль", description="", weight="300 г", price=200, category="Основне меню", subcategory="Овочі гриль"),

        # =========================
        # ДЕСЕРТИ
        # =========================
        Product(name="Штрудель яблучний", description="", weight="150 г", price=120, category="Десерти", subcategory="Без підкатегорії"),
        Product(name="Панакота", description="", weight="250 г", price=100, category="Десерти", subcategory="Без підкатегорії"),
        Product(name="Спартак", description="", weight="100 г", price=100, category="Десерти", subcategory="Без підкатегорії"),
        Product(name="Пташине молоко", description="", weight="100 г", price=100, category="Десерти", subcategory="Без підкатегорії"),
        Product(name="Сирник", description="", weight="100 г", price=120, category="Десерти", subcategory="Без підкатегорії"),
        Product(name="Чізкейк", description="", weight="100 г", price=120, category="Десерти", subcategory="Без підкатегорії"),
        Product(name="Фруктовий салат", description="", weight="150 г", price=120, category="Десерти", subcategory="Без підкатегорії"),
        Product(name="Морозиво фірмове", description="морозиво, фрукти, лісовий горіх, ананас, вершки", weight="100/130/5 г", price=100, category="Десерти", subcategory="Без підкатегорії"),
        Product(name="Морозиво Raffaello", description="морозиво, мигдаль, raffaello, вершки", weight="100/75/5 г", price=100, category="Десерти", subcategory="Без підкатегорії"),
        Product(name="Морозиво Вишенька", description="", weight="100/25/50 г", price=100, category="Десерти", subcategory="Без підкатегорії"),
        Product(name="Морозиво з фруктами", description="", weight="180 г", price=100, category="Десерти", subcategory="Без підкатегорії"),
        Product(name="Морозиво Асорті", description="", weight="150 г", price=100, category="Десерти", subcategory="Без підкатегорії"),
        Product(name="Фруктова тарілка", description="", weight="300 г", price=250, category="Десерти", subcategory="Без підкатегорії"),
        Product(name="Тістечко до кави", description="", weight="1 шт", price=100, category="Десерти", subcategory="Без підкатегорії"),
        Product(name="Апельсин", description="", weight="100 г", price=50, category="Десерти", subcategory="Без підкатегорії"),
        Product(name="Лимон", description="", weight="100 г", price=50, category="Десерти", subcategory="Без підкатегорії"),

        # =========================
        # ПІЦА
        # =========================
        Product(name="Цезаріні", description="соус вершковий, моцарела, куряче філе, бекон, помідор чері, листя салату, соус цезар, пармезан", weight="600 г", price=200, category="Піца", subcategory="Без підкатегорії"),
        Product(name="Діабола", description="гостра / не гостра. Соус пелаті, моцарела, салямі чарізо, помідор, соус табаско", weight="550 г", price=200, category="Піца", subcategory="Без підкатегорії"),
        Product(name="Берлусконі", description='соус "берлусконі", моцарела, печериці, вершки, цибуля кримська, спеції, олія трюфельна', weight="550 г", price=200, category="Піца", subcategory="Без підкатегорії"),
        Product(name="Марта", description="соус вершковий, моцарела, куряче філе, ананас, кукурудза, шинка, дорблю", weight="650 г", price=200, category="Піца", subcategory="Без підкатегорії"),
        Product(name="Баварська", description="соус пелаті, салямі, помідор чері, моцарела, базилік", weight="500 г", price=180, category="Піца", subcategory="Без підкатегорії"),
        Product(name="Парма", description="соус вершковий, моцарела, пармезан, прошуто, рукола, соус парма", weight="650 г", price=200, category="Піца", subcategory="Без підкатегорії"),
        Product(name="Корида", description="соус пелаті, моцарела, салямі черізо, сир чедр, цибуля кримська", weight="550 г", price=200, category="Піца", subcategory="Без підкатегорії"),
        Product(name="Чотири сири", description="соус вершковий, моцарела, дорблю, пармезан, чедр", weight="650 г", price=200, category="Піца", subcategory="Без підкатегорії"),
        Product(name="Чотири сири королівська", description="соус вершковий, моцарела, дорблю, пармезан, чедр, волоський горіх, груша", weight="670 г", price=210, category="Піца", subcategory="Без підкатегорії"),
        Product(name="Чотири м'яса", description="соус пелаті, бекон, куряче філе, телятина, прошуто, рукола", weight="580 г", price=200, category="Піца", subcategory="Без підкатегорії"),
        Product(name="З лососем", description="соус вершковий, лосось, селера, оливки, помідор чері, рукола, пармезан", weight="550 г", price=200, category="Піца", subcategory="Без підкатегорії"),
        Product(name="Капрічіоза", description="соус пелаті, моцарела, прошуто, салямі, печериці", weight="600 г", price=200, category="Піца", subcategory="Без підкатегорії"),
        Product(name="Тонно", description="соус пелаті, моцарела, пармезан, цибуля, тунець, оливки", weight="550 г", price=200, category="Піца", subcategory="Без підкатегорії"),
        Product(name="Карбонара", description="соус вершковий, моцарела, пармезан, бекон, жовток курячий, часник, базилік свіжий", weight="550 г", price=200, category="Піца", subcategory="Без підкатегорії"),
        Product(name="Гавайська", description="соус вершковий, моцарела, курка, ананас, кукурудза", weight="550 г", price=200, category="Піца", subcategory="Без підкатегорії"),
        Product(name="Амерікана", description="соус пелаті, моцарела, сосиски, картопля фрі, печериці, квашений огірок", weight="600 г", price=210, category="Піца", subcategory="Без підкатегорії"),
        Product(name="Кальцоне", description="соус пелаті, моцарела, печериці, шинка, помідор чері, базилік", weight="500 г", price=190, category="Піца", subcategory="Без підкатегорії"),
        Product(name="Маргарита", description="соус пелаті, моцарела, базилік", weight="400 г", price=160, category="Піца", subcategory="Без підкатегорії"),
        Product(name="Сицилія", description="соус пелаті, моцарела, бекон, горгонзола, перець, помідор, рукола", weight="550 г", price=200, category="Піца", subcategory="Без підкатегорії"),

        # =========================
        # АЛКОГОЛЬНІ НАПОЇ -> АЛКОГОЛЬНІ
        # =========================
        Product(name="Martini Bianco", description="100 г — 120 грн • 0,5 — 600 грн", weight="50 г", price=60, category="Алкогольні напої", subcategory="Алкогольні напої"),
        Product(name="Абсент Xenta", description="100 г — 160 грн • 0,5 — 800 грн", weight="50 г", price=80, category="Алкогольні напої", subcategory="Алкогольні напої"),
        Product(name="Текіла Sauza", description="100 г — 140 грн • 0,5 — 700 грн", weight="50 г", price=70, category="Алкогольні напої", subcategory="Алкогольні напої"),
        Product(name="Коньяк 5* Закарпатський", description="100 г — 140 грн • 0,5 — 700 грн", weight="50 г", price=70, category="Алкогольні напої", subcategory="Алкогольні напої"),
        Product(name="Коньяк 4* Закарпатський", description="100 г — 120 грн • 0,5 — 600 грн", weight="50 г", price=60, category="Алкогольні напої", subcategory="Алкогольні напої"),
        Product(name="Коньяк 3* Закарпатський", description="100 г — 100 грн • 0,5 — 500 грн", weight="50 г", price=50, category="Алкогольні напої", subcategory="Алкогольні напої"),
        Product(name='Коньяк "Азнаурі" 3*', description="100 г — 80 грн • 0,5 — 400 грн", weight="50 г", price=40, category="Алкогольні напої", subcategory="Алкогольні напої"),
        Product(name='Коньяк "Азнаурі" 5*', description="100 г — 120 грн • 0,5 — 600 грн", weight="50 г", price=60, category="Алкогольні напої", subcategory="Алкогольні напої"),
        Product(name='Коньяк "Клінков" S-клас', description="100 г — 120 грн • 0,5 — 600 грн", weight="50 г", price=60, category="Алкогольні напої", subcategory="Алкогольні напої"),
        Product(name="Горілка Green Day в асортименті", description="100 г — 56 грн • 0,5 — 280 грн", weight="50 г", price=28, category="Алкогольні напої", subcategory="Алкогольні напої"),
        Product(name="Горілка Львівська в асортименті", description="100 г — 56 грн • 0,5 — 280 грн", weight="50 г", price=28, category="Алкогольні напої", subcategory="Алкогольні напої"),
        Product(name="Горілка Гетьман", description="100 г — 70 грн • 0,5 — 350 грн", weight="50 г", price=35, category="Алкогольні напої", subcategory="Алкогольні напої"),
        Product(name="Горілка Зубрівка в асортименті", description="100 г — 70 грн • 0,5 — 350 грн", weight="50 г", price=35, category="Алкогольні напої", subcategory="Алкогольні напої"),
        Product(name="Горілка Finlandia", description="100 г — 80 грн • 0,5 — 400 грн", weight="50 г", price=40, category="Алкогольні напої", subcategory="Алкогольні напої"),
        Product(name="Горілка Nemiroff медова з перцем", description="100 г — 60 грн • 0,5 — 300 грн", weight="50 г", price=30, category="Алкогольні напої", subcategory="Алкогольні напої"),
        Product(name="Калганівка, Медовуха, Хреновуха, Вишнівка, Кропива", description="100 г — 50 грн • 0,5 — 250 грн", weight="50 г", price=25, category="Алкогольні напої", subcategory="Алкогольні напої"),
        Product(name="Дика роза, Клюква, Сливовиця, З перцем", description="100 г — 50 грн • 0,5 — 250 грн", weight="50 г", price=25, category="Алкогольні напої", subcategory="Алкогольні напої"),
        Product(name="Ром Capitan Morgan", description="100 г — 140 грн • 0,5 — 700 грн", weight="50 г", price=70, category="Алкогольні напої", subcategory="Алкогольні напої"),
        Product(name="Ром Bacardi", description="100 г — 140 грн • 0,5 — 700 грн", weight="50 г", price=70, category="Алкогольні напої", subcategory="Алкогольні напої"),
        Product(name="Ром Oakheart", description="100 г — 120 грн • 0,5 — 600 грн", weight="50 г", price=60, category="Алкогольні напої", subcategory="Алкогольні напої"),
        Product(name="Лікер Jagermeister", description="100 г — 150 грн • 0,5 — 750 грн", weight="50 г", price=75, category="Алкогольні напої", subcategory="Алкогольні напої"),
        Product(name="Лікер Sambuca", description="100 г — 150 грн • 0,5 — 750 грн", weight="50 г", price=75, category="Алкогольні напої", subcategory="Алкогольні напої"),
        Product(name="Лікер Becherovka", description="100 г — 150 грн • 0,5 — 750 грн", weight="50 г", price=75, category="Алкогольні напої", subcategory="Алкогольні напої"),
        Product(name="Лікер Старий ринок", description="100 г — 50 грн • 0,5 — 250 грн", weight="50 г", price=25, category="Алкогольні напої", subcategory="Алкогольні напої"),
        Product(name="Лікер лимонний", description="100 г — 50 грн • 0,5 — 250 грн", weight="50 г", price=25, category="Алкогольні напої", subcategory="Алкогольні напої"),
        Product(name="Лікер вишневий", description="100 г — 50 грн • 0,5 — 250 грн", weight="50 г", price=25, category="Алкогольні напої", subcategory="Алкогольні напої"),
        Product(name="Лікер шоколадний", description="100 г — 50 грн • 0,5 — 250 грн", weight="50 г", price=25, category="Алкогольні напої", subcategory="Алкогольні напої"),
        Product(name="Джин Finsbury", description="100 г — 140 грн • 0,5 — 700 грн", weight="50 г", price=70, category="Алкогольні напої", subcategory="Алкогольні напої"),
        Product(name="Віскі в асортименті", description="100 г — 140 грн • 0,5 — 700 грн", weight="50 г", price=70, category="Алкогольні напої", subcategory="Алкогольні напої"),
        Product(name="Віскі Red Label", description="100 г — 180 грн • 0,5 — 900 грн", weight="50 г", price=90, category="Алкогольні напої", subcategory="Алкогольні напої"),
        Product(name="Віскі Hankey Bannister", description="100 г — 160 грн • 0,5 — 800 грн", weight="50 г", price=90, category="Алкогольні напої", subcategory="Алкогольні напої"),
        Product(name="Віскі Jameson, Jack Daniels, Ballantine’s", description="100 г — 180 грн • 0,5 — 900 грн", weight="50 г", price=90, category="Алкогольні напої", subcategory="Алкогольні напої"),
        Product(name="Вино грузинське в асортименті", description="0,75 — 300 грн", weight="100 г", price=40, category="Алкогольні напої", subcategory="Алкогольні напої"),
        Product(name="Вино Франція, Іспанія, Італія", description="0,75 — 300 грн", weight="100 г", price=40, category="Алкогольні напої", subcategory="Алкогольні напої"),
        Product(name="Шампанське Asti", description="", weight="0,7 л", price=400, category="Алкогольні напої", subcategory="Алкогольні напої"),
        Product(name="Шампанське Артемівське", description="напівсолодке / напівсухе", weight="0,7 л", price=400, category="Алкогольні напої", subcategory="Алкогольні напої"),
        Product(name="Шампанське Prosecco", description="", weight="0,7 л", price=500, category="Алкогольні напої", subcategory="Алкогольні напої"),
        Product(name="Шампанське Prosecco на розлив", description="", weight="200 мл", price=110, category="Алкогольні напої", subcategory="Алкогольні напої"),
        Product(name="Глінтвейн", description="вино, гвоздика, кориця, мед", weight="200 г", price=140, category="Алкогольні напої", subcategory="Алкогольні напої"),

        # =========================
        # АЛКОГОЛЬНІ НАПОЇ -> СЛАБОАЛКОГОЛЬНІ
        # =========================
        Product(name="Пиво Львівське розливне", description="0,5 — 60 грн", weight="0,33 л", price=50, category="Алкогольні напої", subcategory="Слабоалкогольні напої"),
        Product(name='Пиво Львівське 1715 "0"', description="", weight="0,48 л", price=60, category="Алкогольні напої", subcategory="Слабоалкогольні напої"),
        Product(name="Пиво Gambrinus (Чехія)", description="ж/б", weight="0,5 л", price=80, category="Алкогольні напої", subcategory="Слабоалкогольні напої"),
        Product(name="Пиво Stella Artois розливне", description="0,5 — 70 грн", weight="0,33 л", price=60, category="Алкогольні напої", subcategory="Слабоалкогольні напої"),
        Product(name="Пиво Kronenbourg Blanc нефільтроване", description="0,5 — 70 грн", weight="0,33 л", price=60, category="Алкогольні напої", subcategory="Слабоалкогольні напої"),
        Product(name="Пиво баночне в асортименті", description="", weight="0,5 л", price=70, category="Алкогольні напої", subcategory="Слабоалкогольні напої"),

        # =========================
        # АЛКОГОЛЬНІ НАПОЇ -> ДО ПИВА
        # =========================
        Product(name="Пивна дошка", description="бастурма, сир копчений, ковбаски мисливські, фрі", weight="310 г", price=350, category="Алкогольні напої", subcategory="До пива"),
        Product(name="Бастурма", description="", weight="50 г", price=120, category="Алкогольні напої", subcategory="До пива"),
        Product(name="Сир копчений", description="", weight="100 г", price=80, category="Алкогольні напої", subcategory="До пива"),
        Product(name="Чіпси в асортименті", description="120 г — 100 грн", weight="60 г", price=80, category="Алкогольні напої", subcategory="До пива"),
        Product(name="Фісташки", description="", weight="45 г", price=120, category="Алкогольні напої", subcategory="До пива"),
        Product(name="Арахіс солений", description="60 г — 60 грн", weight="30 г", price=30, category="Алкогольні напої", subcategory="До пива"),
        Product(name="Кальмари", description="35 г — 70 грн", weight="18 г", price=50, category="Алкогольні напої", subcategory="До пива"),
        Product(name="Анчоуси", description="35 г — 70 грн", weight="18 г", price=50, category="Алкогольні напої", subcategory="До пива"),
        Product(name="Сухарики в асортименті", description="", weight="70 г", price=50, category="Алкогольні напої", subcategory="До пива"),

        # =========================
        # БЕЗАЛКОГОЛЬНІ НАПОЇ -> ГАРЯЧІ
        # =========================
        Product(name="Кава Espresso", description="з кофеїном / без кофеїну", weight="50 г", price=40, category="Безалкогольні напої", subcategory="Гарячі напої"),
        Product(name="Кава Americano", description="", weight="150 г", price=50, category="Безалкогольні напої", subcategory="Гарячі напої"),
        Product(name="Кава Americano з молоком", description="", weight="150 г", price=60, category="Безалкогольні напої", subcategory="Гарячі напої"),
        Product(name="Кава Latte", description="", weight="200 г", price=70, category="Безалкогольні напої", subcategory="Гарячі напої"),
        Product(name="Капучіно натуральне", description="", weight="150 г", price=60, category="Безалкогольні напої", subcategory="Гарячі напої"),
        Product(name="Какао", description="", weight="200 г", price=70, category="Безалкогольні напої", subcategory="Гарячі напої"),
        Product(name="Чай заварний", description="чорний / зелений", weight="300 г", price=70, category="Безалкогольні напої", subcategory="Гарячі напої"),
        Product(name="Чай заварний карпатський", description="", weight="300 г", price=70, category="Безалкогольні напої", subcategory="Гарячі напої"),
        Product(name="Чай з імбиром та м'ятою", description="", weight="300 г", price=80, category="Безалкогольні напої", subcategory="Гарячі напої"),
        Product(name="Чай зелений заварний з ананасом", description="", weight="300 г", price=70, category="Безалкогольні напої", subcategory="Гарячі напої"),
        Product(name="Чай зелений Саупсет", description="", weight="300 г", price=70, category="Безалкогольні напої", subcategory="Гарячі напої"),
        Product(name="Чай з обліпихи", description="", weight="300 г", price=80, category="Безалкогольні напої", subcategory="Гарячі напої"),
        Product(name="Гарячий шоколад", description="", weight="100 г", price=70, category="Безалкогольні напої", subcategory="Гарячі напої"),

        # =========================
        # БЕЗАЛКОГОЛЬНІ НАПОЇ -> ХОЛОДНІ
        # =========================
        Product(name="Фреш апельсиновий", description="", weight="200 г", price=130, category="Безалкогольні напої", subcategory="Холодні напої"),
        Product(name="Сік в асортименті", description="1 л — 150 грн", weight="200 г", price=30, category="Безалкогольні напої", subcategory="Холодні напої"),
        Product(name="Узвар / компот", description="1 л — 125 грн", weight="200 г", price=25, category="Безалкогольні напої", subcategory="Холодні напої"),
        Product(name="Coca-Cola / Pepsi / Fanta", description="1 л — 80 грн", weight="0,5 л", price=50, category="Безалкогольні напої", subcategory="Холодні напої"),
        Product(name="Мінеральна вода Трускавецька", description="", weight="0,5 л", price=30, category="Безалкогольні напої", subcategory="Холодні напої"),
        Product(name="Мінеральна вода Трускавецька (скло)", description="0,75 л — 60 грн", weight="0,33 л", price=40, category="Безалкогольні напої", subcategory="Холодні напої"),
        Product(name="Мінеральна вода Трускавецька (газ / не газ)", description="", weight="1,5 л", price=40, category="Безалкогольні напої", subcategory="Холодні напої"),
        Product(name="Мінеральна вода Поляна квасова", description="", weight="0,5 л", price=80, category="Безалкогольні напої", subcategory="Холодні напої"),
        Product(name="Мінеральна вода Borjomi", description="", weight="300 г", price=100, category="Безалкогольні напої", subcategory="Холодні напої"),
        Product(name="Мінеральна вода Моршинська н/г", description="", weight="0,5 л", price=30, category="Безалкогольні напої", subcategory="Холодні напої"),
        Product(name="Мінеральна вода Моршинська (газ / не газ)", description="", weight="0,5 л", price=30, category="Безалкогольні напої", subcategory="Холодні напої"),

        # =========================
        # КОКТЕЙЛІ -> АЛКОГОЛЬНІ
        # =========================
        Product(name="Aperol Spritz", description="Aperol, шампанське Prosecco, мінеральна вода, апельсин, м'ята, лід", weight="300 г", price=140, category="Коктейлі", subcategory="Коктейлі алкогольні"),
        Product(name="Інгалятор (Самбука)", description="самбука", weight="50 г", price=85, category="Коктейлі", subcategory="Коктейлі алкогольні"),
        Product(name="Текіла Санрайз", description="текіла, апельсиновий сік, гренадин", weight="100 г", price=210, category="Коктейлі", subcategory="Коктейлі алкогольні"),
        Product(name="Голуба лагуна", description="горілка, блю курасао, сік ананасовий, мінеральна вода, лід, спрайт", weight="200 г", price=110, category="Коктейлі", subcategory="Коктейлі алкогольні"),
        Product(name="Пампушка", description="ананасовий сік, морозиво, Старий Талін", weight="200 г", price=90, category="Коктейлі", subcategory="Коктейлі алкогольні"),
        Product(name="Мулатка", description="Coca-Cola, морозиво, вишневий лікер, вершки", weight="200 г", price=100, category="Коктейлі", subcategory="Коктейлі алкогольні"),
        Product(name="Мохіто", description="спрайт, мінеральна вода, лайм, лимон, лід, ром", weight="200 г", price=110, category="Коктейлі", subcategory="Коктейлі алкогольні"),
        Product(name="Осіннє листя", description="лікер лимонний, м'ятний лікер, біле вино", weight="200 г", price=90, category="Коктейлі", subcategory="Коктейлі алкогольні"),
        Product(name="Оригінальний", description="сік на вибір, морозиво, горілка", weight="300 г", price=85, category="Коктейлі", subcategory="Коктейлі алкогольні"),
        Product(name="Кавовий", description="Coca-Cola, коньяк, кава", weight="200 г", price=90, category="Коктейлі", subcategory="Коктейлі алкогольні"),
        Product(name="Лимонний", description="біле сухе вино, лікер лимонний, лід, лимон, мінеральна вода", weight="200 г", price=90, category="Коктейлі", subcategory="Коктейлі алкогольні"),
        Product(name="Кривава Мері", description="горілка, томатний сік", weight="150 г", price=80, category="Коктейлі", subcategory="Коктейлі алкогольні"),
        Product(name="Хуґо", description="шампанське Prosecco, лайм, сироп бузини, м'ята, лимон, лід", weight="300 г", price=150, category="Коктейлі", subcategory="Коктейлі алкогольні"),
        Product(name="Піна Колада", description="білий ром, кокосовий сироп, ананасовий сік", weight="200 г", price=140, category="Коктейлі", subcategory="Коктейлі алкогольні"),

        # =========================
        # КОКТЕЙЛІ -> БЕЗАЛКОГОЛЬНІ
        # =========================
        Product(name="Десертний", description="", weight="250 г", price=70, category="Коктейлі", subcategory="Коктейлі безалкогольні"),
        Product(name="Молочно-банановий", description="", weight="250 г", price=70, category="Коктейлі", subcategory="Коктейлі безалкогольні"),
        Product(name="Молочно-полуничний", description="", weight="250 г", price=70, category="Коктейлі", subcategory="Коктейлі безалкогольні"),
        Product(name="Молочно-шоколадний", description="", weight="250 г", price=70, category="Коктейлі", subcategory="Коктейлі безалкогольні"),
        Product(name="Мохіто безалкогольний", description="", weight="200 г", price=70, category="Коктейлі", subcategory="Коктейлі безалкогольні"),
    ]

    db.add_all(products)
    db.commit()
    db.close()

    print(f"Успішно додано {len(products)} страв у базу.")


if __name__ == "__main__":
    seed_products()