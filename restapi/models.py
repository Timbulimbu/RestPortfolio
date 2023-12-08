from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Me(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="Имя", help_text="Введите имя")
    last_name = models.CharField(max_length=50, verbose_name="Фамилия", help_text="Введите фамилию")
    email = models.EmailField(max_length=50, verbose_name="Почта", help_text="Введите почту")
    phone = models.CharField(max_length=50, verbose_name="Телефон", help_text="Введите телефон")    
    instagram = models.URLField(max_length=150, verbose_name="Instagram", blank=True, null=True, help_text="Instagram")
    github = models.URLField(max_length=150, verbose_name="Github", blank=True, null=True, help_text="Github")
    linkedin = models.URLField(max_length=150, verbose_name="LinkedIn", blank=True, null=True, help_text="LinkedIn")
    telegram = models.URLField(max_length=150, verbose_name="Telegram", blank=True, null=True, help_text="Telegram")
    education = models.TextField(verbose_name="Образование", help_text="Образование", blank=True, null=True)
    work_history = models.TextField(verbose_name="Опыт работы", help_text="Опыт работы", blank=True, null=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        verbose_name = "Обо мне"
        verbose_name_plural = "Обо мне"
        

class Project(models.Model):
    file = models.FileField(upload_to='project_file/', verbose_name="Файл проекта", help_text="Загрузите файл, если необходимо", blank=True, null=True)
    image = models.ImageField(upload_to='project_image/', verbose_name="Изображение проекта", help_text="Загрузите изображение, если есть", blank=True, null=True)
    title = models.CharField(max_length=150, verbose_name="Название проекта", help_text="Введите название проекта")
    description = models.TextField(verbose_name="Описание проекта", help_text="Введите описание проекта")
    start_date = models.DateField(verbose_name="Дата начала", help_text="Введите дату начала")
    end_date = models.DateField(verbose_name="Дата окончания", help_text="Введите дату окончания, если завершён", blank=True, null=True)
    url = models.URLField(max_length=150, verbose_name="Ссылка на проект", help_text="Введите ссылку на проект", blank=True, null=True)
    repository = models.URLField(max_length=150, verbose_name="GitHub репозиторий", help_text="Введите репозиторий GitHub", blank=True, null=True)
    technologies_used = models.CharField(max_length=300, verbose_name="Использованные технологии", help_text="Введите технологии, используемые в проекте")
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"
        
        
class Skill(models.Model): 
    CATEGORY_CHOICES = [
            ('programming', 'Программирование'),
            ('design', 'Дизайн'),
            ('languages', 'Языки программирования'),
            ('database', 'Базы данных'),
            ('frameworks', 'Фреймворки'),
            ('tools', 'Инструменты разработки'),
            ('soft_skills', 'Soft Skills'),
            ('web', 'Веб-разработка'),
            ('mobile', 'Мобильная разработка'),
            ('cloud', 'Облачные технологии'),
            ('testing', 'Тестирование и QA'),
            ('analytics', 'Аналитика данных'),
            ('machine_learning', 'Машинное обучение и искусственный интеллект'),
            ('security', 'Информационная безопасность'),
            ('networking', 'Сетевые технологии'),
            ('graphics', 'Графический дизайн'),
            ('audio_video', 'Аудио и видео производство'),
            ('project_management', 'Управление проектами'),
            ('communication', 'Коммуникационные навыки'),
            ('leadership', 'Лидерство'),
            ('entrepreneurship', 'Предпринимательство'),
            ('data_science', 'Наука о данных'),
            ('automation', 'Автоматизация процессов'),
            ('devops', 'DevOps'),
            ('blockchain', 'Блокчейн технологии'),
            ('robotics', 'Робототехника'),
            ('language', 'Знание языков'),
        ]

    category = models.CharField(max_length=50, verbose_name="Категория", help_text="Выберите категорию для навыка", choices=CATEGORY_CHOICES)
    name = models.CharField(max_length=50, verbose_name="Навык", help_text="Введите название навыка")
    percentage = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], verbose_name="Процент знаний", help_text="Введите процент знаний навыка")
    
    def __str__(self):
        return f"{self.name} ({self.percentage}%)"
    
    class Meta:
        verbose_name = "Навык"
        verbose_name_plural = "Навыки"
        
        
class Pricing(models.Model):
    service = models.CharField(max_length=100, verbose_name="Услуга", help_text="Введите название услуги")
    description = models.TextField(verbose_name="Описание услуги", help_text="Введите описание услуги")
    rate_per_hour = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Стоимость за час", help_text="Введите стоимость в долларах за час")
    estimated_time = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Оценка времени", help_text="Оцените, сколько часов требуется для выполнения услуги")
    

    def total_cost(self):
        return self.rate_per_hour * self.estimated_time

    def __str__(self):
        return f"{self.service}  - ${self.total_cost()}"
    
    class Meta:
        verbose_name = "Расценка"
        verbose_name_plural = "Расценки"
        

class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя",  help_text="Введите имя")
    email = models.EmailField(max_length=100, verbose_name="Email", help_text="Введите свой действующий адрес электронной почты")
    subject = models.CharField(max_length=400, verbose_name="Тема", help_text="Введите тему сообщения")
    message = models.TextField(verbose_name="Сообщение", help_text="Введите сообщение")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата и время создания")
    is_read = models.BooleanField(default=False, verbose_name="Отметка о прочитанном сообщении")
    
    def __str__(self):
        return f"{self.subject} - {self.name} - {self.email}"
    
    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"



    
    
    
    
    
    
    
    
    