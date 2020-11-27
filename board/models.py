from datetime import datetime

from django.db import models

class Board(models.Model):
    #autofield라서 자동 증가 되고 primary key 가 됩니다. 
    idx=models.AutoField(primary_key=True)
    writer=models.CharField(null=False,max_length=50)
    #null=False 는 not null이라는 뜻 
    title=models.CharField(null=False,max_length=120)
    #readcount 
    hit=models.IntegerField(default=0)
    content=models.TextField(null=False)
    #default는 지금시간 , 비워도 된다. 
    post_date=models.DateTimeField(default=datetime.now,blank=True)
#파일 업로드를 위한 . type은 charfield , null, blank여도 된다. 
#만약에 안들어오면 , null이 아니라 ""이 되게 한다. 
#charfield는 max_length 가 들어간다. 
    filename=models.CharField(null=True,blank=True,default="",max_length=500)
    #파일사이즈  (업로드 안되면0) 
    filesize=models.IntegerField(default=0)
        # 다운로드 한 횟수 
    down=models.IntegerField(default=0)
#게시물 수 올라갈때마다 갯수 추적 
    def hit_up(self):
        self.hit += 1
    #다운로드 수 올라갈때마다 갯수 추적 
    def down_up(self):
        self.down += 1
        
class Comment(models.Model):
 #댓글 글번호
    idx=models.AutoField(primary_key=True)
    #게시물 번호
    board_idx=models.IntegerField(null=False)
    writer=models.CharField(null=False,max_length=50)
    content=models.TextField(null=False)
    post_date=models.DateTimeField(default=datetime.now,blank=True)
    
    
class Movie(models.Model):
#자동증가하는 primarykey를 index로 설정한다. 
    idx=models.AutoField(primary_key=True)
    title=models.CharField(null=False, max_length=500)
    content=models.TextField(null=False)
    point=models.IntegerField(default=0)