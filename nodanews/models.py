from django.db import models
from django.db.models.aggregates import Count
from datetime import datetime

class Theme(models.Model):
    name = models.CharField(max_length=100, default=' ')
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('name',)
        
class Variation(models.Model):
    name = models.CharField(max_length=100, default=' ')
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('name',)        
      
class Author(models.Model):
    name = models.CharField(max_length=100, default='name here')
    image = models.ImageField(upload_to='media/stock', default='')    
    def __str__(self):
        return self.name
    class Meta:
        ordering = ('name',)        

class Front_Page(models.Model):
    featureQ = models.BooleanField(default=False)
    title = models.CharField(max_length=100, default='date written out')
    date = models.DateField(auto_now=False, auto_now_add=False)
    feature_headline = models.CharField(max_length=150, default=' ', blank=True)
    feature_url = models.CharField(max_length=300, default='', blank=True)
    feature_pic = models.ImageField(upload_to='media/stock', blank=True, default=' ')
    feature_pic_credit = models.CharField(max_length=150, blank=True, default=' ')
    slug = models.SlugField(max_length=100, default='date')        
    
    def __str__(self):
        return self.slug
    class Meta:
        ordering = ('-date',)        

    
class Event(models.Model):
    LEFT = 'L'
    MIDDLE = 'M'
    RIGHT = 'R'
    COLUMN_CHOICES = [
        (LEFT, 'Left'),
        (MIDDLE, 'Middle'),
        (RIGHT, 'Right'),
        ]
    headline = models.CharField(max_length=150, default=' ', blank=True)
    lead = models.TextField(blank=True)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    body = models.TextField(default=' ', blank=True)
    body2 = models.TextField(default=' ', blank=True)
    image1 = models.ImageField(upload_to='media/stock', default='', blank=True)
    displayQ = models.BooleanField(default=False)    
    credit1 = models.CharField(max_length=200, default='', blank=True) 
    image2 = models.ImageField(upload_to='media/stock', default='', blank=True)
    credit2 = models.CharField(max_length=200, default='', blank=True) 
    videoQ = models.BooleanField(default=False)
    video = models.CharField(max_length=500, default='', blank=True)
    column = models.CharField(max_length=1, choices=COLUMN_CHOICES, default=LEFT)
    front_page = models.ForeignKey(
        'Front_Page',
        on_delete=models.CASCADE,
        null=True,
        blank=True)
    theme = models.ForeignKey(
        'Theme',
        on_delete=models.CASCADE,
        blank=True)
    author = models.ForeignKey(
        'Author',
        on_delete=models.CASCADE,
        null=True,
        blank=True)
    slug = models.SlugField(max_length=100, default=' ')
    readyQ = models.BooleanField(default=False)
    
    def __str__(self):
        return self.headline
    class Meta:
        ordering = ('-date_created',)

class Media_Org(models.Model):
    name = models.CharField(max_length=100, default='')
    date_posted = models.DateTimeField(auto_now_add=True)
    home_page = models.CharField(max_length=200, default='')
    country = models.CharField(max_length=100, default='')
    date_founded = models.DateField(default='1956-02-27')
    logo = models.ImageField(upload_to='media/logos')
    description = models.TextField()
    ready = models.BooleanField(default=False)
    slug = models.SlugField(max_length=100, default=' ')

    
    def __str__(self):
        return self.name
    class Meta:
        ordering = ('name',)
        
class Report_Link(models.Model):
    url = models.CharField(max_length=300, default='', blank=True)
    title = models.CharField(max_length=150, default='', blank=True)
    posted = models.DateTimeField(auto_now=True, blank=True)    
    media = models.ForeignKey(
        'Media_Org',
        on_delete=models.CASCADE,
        blank=True)
    event = models.ForeignKey(
        'Event',
        on_delete=models.CASCADE,
        blank=True,
        null=True)
    imageQ = models.BooleanField(default=False)
    image = models.ImageField(upload_to='media/temp', default='', blank=True)        

    def __str__(self):
        return "{}/{}".format(self.title, self.event)  
        
    class Meta:
        ordering = ('-posted',)
        
class Other_Link(models.Model):
    url = models.CharField(max_length=300, default='', blank=True)
    title = models.CharField(max_length=150, default='', blank=True)
    posted = models.DateTimeField(auto_now=True, blank=True)    
    media = models.ForeignKey(
        'Media_Org',
        on_delete=models.CASCADE,)
    imageQ = models.BooleanField(default=False)
    image = models.ImageField(upload_to='media/temp', default='', blank=True)
    major = models.BooleanField(default=False, blank=True)
    liberal = models.BooleanField(default=False, blank=True)
    conservative = models.BooleanField(default=False, blank=True)
    front_page = models.ForeignKey(
        'Front_Page',
        on_delete=models.CASCADE,
        null=True,
        blank=True)    
    def __str__(self):
        return "{}/{}".format(self.title, self.media.name)  
        
    class Meta:
        ordering = ('-posted',)
        
class Blog(models.Model):
    headline = models.CharField(max_length=200, default='')
    date_posted = models.DateField(auto_now_add=True)
    text = models.TextField()
    slug = models.SlugField(max_length=200, default=' ') 
    event = models.ForeignKey(
        'Event',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        default=1)    
    def __str__(self):
        return "{}".format(self.headline)
    class Meta:
        ordering = ('-date_posted',)
        
class About(models.Model):
    description = models.TextField()





        
#################Archives###################



class Region(models.Model):
    name = models.CharField(max_length=100, default='')
    color = models.CharField(max_length=100, default='')
    
    def __str__(self):
        return self.name
    class Meta:
        ordering = ('name',)    

class Node_Dir(models.Model):
    name = models.CharField(max_length=100, default='')
    active = models.BooleanField(default=False)
    date_updated = models.DateTimeField(auto_now=True, blank=True)
    description = models.TextField(default=' ')
    region = models.ForeignKey(
        'Region',
        default=8,
        null=True,
        on_delete=models.PROTECT,)
    banner = models.ImageField(upload_to='media/nodes', default='', blank=True)
    slug = models.SlugField(max_length=100, default=' ')    
   
    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)

class Feature(models.Model):
    name = models.CharField(max_length=100, default='')
    image = models.ImageField(upload_to='media/temp', default='', blank=True)    

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)

class STF_Hub(models.Model):
    name = models.CharField(max_length=100, default='')
    banner = models.ImageField(upload_to='media/nodes')
    credit = models.CharField(max_length=200, default='')     
    date_updated = models.DateTimeField(auto_now=True, blank=True)
    description = models.TextField(default='', blank=True)
    node_dir = models.ForeignKey(
        'Node_Dir',
        on_delete=models.PROTECT,)
    slug = models.SlugField(max_length=200, default=' ') 

    def __str__(self):
        return self.name

class Node(models.Model):
    headline = models.CharField(max_length=200, default='')
    country = models.CharField(max_length=100, default='')
    date_posted = models.DateField(auto_now_add=True)
    lead = models.TextField(default='')
    head_image = models.ImageField(upload_to='media/nodes', default='')
    credit1 = models.CharField(max_length=200, default='')        
    my_take = models.TextField()
    video_embed1 = models.CharField(max_length=500, default='', blank=True)    
    my_take2 = models.TextField(default='')
    video_embed2 = models.CharField(max_length=500, default='', blank=True)    
    foot_image = models.ImageField(upload_to='media/nodes', default='')
    credit2 = models.CharField(max_length=200, default='')    
    video_embed3 = models.CharField(max_length=500, default='', blank=True)    
    node_direc = models.ForeignKey(
        'Node_Dir',
        on_delete=models.PROTECT,)
    region = models.ForeignKey('Region',
    default=1,
    null=True,
    on_delete=models.PROTECT,)
    slug = models.SlugField(max_length=200, default=' ') 

    def __str__(self):
        return "{}/{}".format(self.headline, self.country)
    class Meta:
        ordering = ('-date_posted',)

class Perspective(models.Model):
    name = models.CharField(max_length=47, default='')
    node = models.ForeignKey(
        'Node',
        on_delete=models.CASCADE,)
    
    def __str__(self):
        return "{}/{}".format(self.node, self.name)
    class Meta:
        ordering = ('-id',)
        
class Political_Lean(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Media_Character(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name


class STF(models.Model):
    headline = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media/nodes', default='')
    credit = models.CharField(max_length=200, default='')     
    update = models.TextField()
    date_updated = models.DateTimeField(auto_now=True)
    videoQ = models.BooleanField(default=False)
    video = models.CharField(max_length=500, default='', blank=True) 
    hub= models.ForeignKey(
        'STF_Hub',
        on_delete=models.PROTECT)
    node_dir = models.ForeignKey(
        'Node_Dir',
        on_delete=models.PROTECT,)

    slug = models.SlugField(max_length=200, default=' ') 

    def __str__(self):
        return "{}/{}".format(self.headline, self.hub)
    class Meta:
        ordering = ('-date_updated',)        

class Journalist(models.Model):
    name = models.CharField(max_length=200, default='')
    contact = models.CharField(max_length=200, default='')
    organization = models.ForeignKey(
        'Media_Org',
        on_delete=models.PROTECT,)
    bio = models.TextField(default='bio goes here')
    picture = models.ImageField(upload_to='media/logos', default=" ")
    slug = models.SlugField(max_length=100, default=' ')
    def __str__(self):
        return self.name
    class Meta:
        ordering = ('name',)
        
class Link(models.Model):
    url = models.CharField(max_length=300, default='', blank=True)
    title = models.CharField(max_length=150, default='', blank=True)
    media = models.ForeignKey(
        'Media_Org',
        on_delete=models.CASCADE,)
    perspective = models.ForeignKey(
        'Perspective',
        on_delete=models.CASCADE,)
    
    def __str__(self):
        return "{}/{}".format(self.id, self.perspective)
        
class Feature_Link(models.Model):
    url = models.CharField(max_length=300, default='', blank=True)
    title = models.CharField(max_length=150, default='', blank=True)
    posted = models.DateTimeField(auto_now=True, blank=True)
    media = models.ForeignKey(
        'Media_Org',
        on_delete=models.CASCADE,)
    feature = models.ForeignKey(
        'Feature',
        on_delete=models.CASCADE,)
    
    def __str__(self):
        return "{}/{}".format(self.id, self.feature)        

    class Meta:
        ordering = ('-posted',)

class STF_Link(models.Model):
    url = models.CharField(max_length=300, default='', blank=True)
    title = models.CharField(max_length=150, default='', blank=True)
    media = models.ForeignKey(
        'Media_Org',
        on_delete=models.CASCADE,)
    story = models.ForeignKey(
        'STF',
        on_delete=models.CASCADE,)
    def __str__(self):
        return "{}/{}".format(self.id, self.story)

class Topic_Link(models.Model):
    url = models.CharField(max_length=300, default='', blank=True)
    title = models.CharField(max_length=150, default='', blank=True)
    posted = models.DateTimeField(default=datetime.now, blank=True)
    region = models.ForeignKey(
        'Region',
        default=8,
        null=True,
        on_delete=models.CASCADE,)
    media = models.ForeignKey(
        'Media_Org',
        on_delete=models.CASCADE,)
    node_dir = models.ForeignKey(
        'Node_Dir',
        on_delete=models.CASCADE,)
    journalist = models.ForeignKey('Journalist',
    null=True,
    blank=True,
    on_delete=models.PROTECT,)	
    def __str__(self):
        return "{}/{}".format(self.id, self.node_dir.name)




############################### Old Stuff Below ######################################
        
class Analysis(models.Model):
    headline = models.CharField(max_length=200, default='')
    date_posted = models.DateField()
    head_image = models.ImageField(upload_to='media/nodes', default='')
    summary = models.TextField()
    text1 = models.TextField()
    second_image = models.ImageField(upload_to='media/nodes', default='')
    text2 = models.TextField()
    pop_out_quote = models.TextField()
    video_embed1 = models.CharField(max_length=500, default='', blank=True)
    video_embed2 = models.CharField(max_length=500, default='', blank=True)
    video_embed3 = models.CharField(max_length=500, default='', blank=True)    
    node_direc = models.ForeignKey(
        'Node_Dir',
        on_delete=models.CASCADE,)
    slug = models.SlugField(max_length=200, default=' ') 
    def __str__(self):
        return "{}".format(self.headline)
    class Meta:
        ordering = ('-date_posted',)

class AnalPerspective(models.Model):
    name = models.CharField(max_length=47, default='')
    article = models.ForeignKey(
        'Analysis',
        on_delete=models.CASCADE,)
    
    def __str__(self):
        return "{}/{}".format(self.article, self.name)
    class Meta:
        ordering = ('-id',)

class PoliticalIssue(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(default="description goes here")
    head_image = models.ImageField(upload_to='media/nodes', default='')
    slug = models.SlugField(max_length=100, default=' ')    
    def __str__(self):
        return "{}".format(self.name)
    class Meta:
        ordering = ('-id',)

class PoliticalBiasNews(models.Model):
    url = models.CharField(max_length=300, default='')
    title = models.CharField(max_length=150, default='')
    media = models.ForeignKey(
        'Media_Org',
        on_delete=models.CASCADE,)
    posted = models.DateTimeField(default=datetime.now, blank=True)
    region = models.ForeignKey(
        'Region',
        default=9,
        null=True,
        on_delete=models.CASCADE,)
    conservative = models.BooleanField(default=False)
    liberal = models.BooleanField(default=True)
    issue = models.ForeignKey(
        'PoliticalIssue',
        default=1,
        on_delete=models.CASCADE,)	
    def __str__(self):
        return "{}/{}".format(self.id, self.issue.name)

    class Meta:
        ordering = ('-posted',)

class AnalLink(models.Model):
    url = models.CharField(max_length=300, default='', blank=True)
    title = models.CharField(max_length=150, default='', blank=True)
    media = models.ForeignKey('Media_Org',
    blank=True,
    null=True,
    on_delete=models.CASCADE,)
    academic = models.BooleanField(default=False)
    author = models.ForeignKey(
        'Journalist',
        null=True,
        blank=True,
        on_delete=models.CASCADE,)
    perspective = models.ForeignKey(
        'AnalPerspective',
        on_delete=models.CASCADE,)
    
    def __str__(self):
        return "{}/{}".format(self.id, self.perspective)