from django.db import models


class Banner(models.Model):
    tg = models.URLField()
    fb= models.URLField()
    yt = models.URLField()
    tw= models.URLField()
    logo = models.ImageField()
    number = models.IntegerField()
    email= models.EmailField()
    photo = models.ImageField()
    data = models.DateField()



class Navbar(models.Model):
    title = models.TextField()
    photo = models.ImageField()


class News(models.Model):
    photo = models.ImageField()
    title = models.TextField()
    data = models.DateField()
    more = models.URLField()


class Game_schedule(models.Model):
    name = models.CharField(max_length=225)
    result = models.IntegerField()
    logo = models.ImageField()


class Calendar(models.Model):
    top = models.CharField(max_length=225)
    data = models.DateField()
    game = models.ManyToManyField(Game_schedule)


class Schedule(models.Model):
    logo = models.ImageField()
    name = models.CharField(max_length=200)
    game= models.IntegerField()
    win= models.IntegerField()
    defeat= models.IntegerField()
    tie= models.IntegerField()
    pts= models.IntegerField()
    t_f = models.IntegerField()


class Youtube(models.Model):
    photo = models.ImageField()
    name = models.CharField(max_length=200)
    video = models.URLField()
    video_2 = models.URLField()
    video_3 = models.URLField()


class Player_statistics(models.Model):
    photo = models.ImageField()
    f_name = models.CharField(max_length=300)
    l_name = models.CharField(max_length=300)
    pasition= models.CharField(max_length=300)
    games = models.IntegerField()
    started = models.IntegerField()
    sub_off = models.IntegerField()
    minutes= models.IntegerField()
    number = models.IntegerField()




class Shop_1(models.Model):
    photo = models.ImageField()
    fc_name = models.CharField(max_length=200)
    name = models.CharField(max_length=200)

class Stadium_photo(models.Model):
    photo = models.ImageField()

class Arena_history2(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField()
    photo = models.ImageField()

class Stadium(models.Model):
    name = models.CharField(max_length=200)
    text = models.TextField()
    size = models.IntegerField()
    places  = models.IntegerField()
    sector = models.IntegerField()
    map = models.CharField(max_length=300)
    number = models.IntegerField()
    photo = models.ManyToManyField(Stadium_photo)


class Partners(models.Model):
    photo = models.ImageField()
    photo_2 = models.ImageField()
    photo_3 = models.ImageField()
    photo_4 = models.ImageField()
    photo_5 = models.ImageField()



class Team_members(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField()


class Management(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField()



class Coach(models.Model):
    photo = models.ImageField()
    name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    text = models.TextField()




class Club_info(models.Model):
    tex = models.TextField()
    icon = models.CharField(max_length=200)


class Club_history(models.Model):
    photo = models.ImageField()
    title = models.CharField(max_length=200)
    info = models.ManyToManyField(Club_info)
    text = models.TextField()
    photo_2 = models.ImageField()


class Arena_history3(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField()
    photo = models.ImageField()


class Recommendations(models.Model):
    photo = models.ImageField()
    tex = models.TextField()
    data = models.DateField(auto_now_add=True)


class Academy(models.Model):
    name = models.CharField(max_length=200)
    bg_photo = models.ImageField()


class Training(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField()


class Shop_2(models.Model):
    text = models.TextField()
    back_photo = models.ImageField()
    photo = models.ImageField()



class Bobur_arena(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField()


class Shop_3(models.Model):
    photo = models.ImageField()
    title = models.TextField()
    photo_one = models.ImageField()
    photo_two = models.ImageField()
    text =  models.TextField()


class About_shop(models.Model):
        img = models.ImageField()
        tex =  models.TextField()
        img1 = models.ImageField()
        img2 = models.ImageField()
        title =  models.TextField()
        img3 = models.ImageField()
        img4 = models.ImageField()
        img5 = models.ImageField()
        img6 = models.ImageField()
        img7 = models.ImageField()
        url = models.URLField()
        img8 = models.ImageField()
        img9 = models.ImageField()
        img10 = models.ImageField()





class Arena_history(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField()
    img = models.ImageField()