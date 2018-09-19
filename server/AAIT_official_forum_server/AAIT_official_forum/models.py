# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Administrator(models.Model):
    administrator_id = models.PositiveIntegerField(primary_key=True)
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'administrator'


class Article(models.Model):
    article_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField(blank=True, null=True)
    article_time = models.DateTimeField(blank=True, null=True)
    title = models.CharField(max_length=45, blank=True, null=True)
    is_valid = models.IntegerField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    article_board_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'article'


class ArticleBoard(models.Model):
    article_board_id = models.AutoField(primary_key=True)
    board_name = models.CharField(max_length=45, blank=True, null=True)
    board_description = models.TextField(blank=True, null=True)
    last_article_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'article_board'


class ArticleComment(models.Model):
    article_comment_id = models.PositiveIntegerField(primary_key=True)
    user_id = models.IntegerField(blank=True, null=True)
    article_id = models.IntegerField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'article_comment'


class Goods(models.Model):
    goods_id = models.AutoField(primary_key=True)
    price = models.BigIntegerField(blank=True, null=True)
    stock = models.BigIntegerField(blank=True, null=True)
    goods_image = models.CharField(max_length=45, blank=True, null=True)
    goods_info = models.TextField(blank=True, null=True)
    is_online = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'goods'


class Group(models.Model):
    group_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    is_close = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    group_name = models.CharField(max_length=45, blank=True, null=True)
    group_type = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'group'


class GroupActivity(models.Model):
    group_activity_id = models.AutoField(primary_key=True)
    group_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    is_close = models.IntegerField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    group_activity_name = models.CharField(max_length=45, blank=True, null=True)
    remind_time = models.DateTimeField(blank=True, null=True)
    appendix = models.CharField(max_length=45, blank=True, null=True)
    group_activity_cover = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'group_activity'


class GroupBulletin(models.Model):
    group_bulletin_id = models.AutoField(primary_key=True)
    group_id = models.IntegerField(blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'group_bulletin'


class GroupMembers(models.Model):
    group_members_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField(blank=True, null=True)
    is_administrator = models.IntegerField(blank=True, null=True)
    group_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'group_members'


class GroupTask(models.Model):
    group_task_id = models.AutoField(primary_key=True)
    group_id = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    is_close = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    appendix = models.CharField(max_length=45, blank=True, null=True)
    group_task_cover = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'group_task'


class GroupTaskJoin(models.Model):
    group_task_join_id = models.IntegerField(primary_key=True)
    group_task_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    is_finish = models.IntegerField(blank=True, null=True)
    group_id = models.IntegerField(blank=True, null=True)
    finish_time = models.DateTimeField(blank=True, null=True)
    join_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'group_task_join'


class JoinGroupActivity(models.Model):
    join_group_activity_id = models.AutoField(primary_key=True)
    group_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    group_activity_id = models.IntegerField(blank=True, null=True)
    join_time = models.DateTimeField(blank=True, null=True)
    is_join_finish = models.IntegerField(blank=True, null=True)
    is_expire = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'join_group_activity'


class PoromodoClock(models.Model):
    poromodo_clock_id = models.AutoField(db_column='Poromodo_Clock_id', primary_key=True)  # Field name made lowercase.
    user_id = models.IntegerField(blank=True, null=True)
    clock_count = models.SmallIntegerField(blank=True, null=True)
    invalid_poromodo_clock = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'poromodo_clock'


class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField(blank=True, null=True)
    post_time = models.DateTimeField(blank=True, null=True)
    post_content = models.TextField(blank=True, null=True)
    title = models.CharField(max_length=45, blank=True, null=True)
    post_board_id = models.CharField(max_length=45, blank=True, null=True)
    is_vaild = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'post'


class PostBoard(models.Model):
    post_board_id = models.AutoField(primary_key=True)
    board_description = models.TextField(blank=True, null=True)
    post_theme_id = models.IntegerField(blank=True, null=True)
    last_post_id = models.IntegerField(blank=True, null=True)
    board_name = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'post_board'


class PostComment(models.Model):
    post_comment_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField(blank=True, null=True)
    post_comment_content = models.TextField(blank=True, null=True)
    post_comment_time = models.DateTimeField(blank=True, null=True)
    post_id = models.IntegerField(blank=True, null=True)
    is_have_comment = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'post_comment'


class PostCommentReply(models.Model):
    post_comment_reply_id = models.AutoField(primary_key=True)
    post_comment_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    reply_content = models.TextField(blank=True, null=True)
    reply_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'post_comment_reply'


class PostTheme(models.Model):
    post_theme_id = models.IntegerField(primary_key=True)
    theme_name = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'post_theme'


class Prize(models.Model):
    prize_id = models.IntegerField(primary_key=True)
    prize_image = models.CharField(max_length=45, blank=True, null=True)
    title = models.CharField(max_length=45, blank=True, null=True)
    price = models.SmallIntegerField(blank=True, null=True)
    prize_description = models.TextField(blank=True, null=True)
    prize_stock = models.IntegerField(blank=True, null=True)
    is_online = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prize'


class Schedule(models.Model):
    schedule_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    schedule_class_id = models.IntegerField(blank=True, null=True)
    is_finish = models.IntegerField(blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'schedule'


class ScheduleClassify(models.Model):
    schedule_classify_id = models.IntegerField(primary_key=True)
    classify_info = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'schedule_classify'


class ScheduleTag(models.Model):
    schedule_tag_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField(blank=True, null=True)
    schedule_id = models.IntegerField(blank=True, null=True)
    tag = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'schedule_tag'


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    salt = models.CharField(max_length=45, blank=True, null=True)
    e_mail = models.CharField(max_length=45)
    user_logo = models.CharField(max_length=45, blank=True, null=True)
    user_rank = models.IntegerField(blank=True, null=True)
    user_description = models.CharField(max_length=200, blank=True, null=True)
    last_post_id = models.IntegerField(blank=True, null=True)
    last_article_id = models.IntegerField(blank=True, null=True)
    def __str__(self):
        return self.username  
    class Meta:
        managed = False
        db_table = 'user'


class UserAccount(models.Model):
    user_account_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField(blank=True, null=True)
    user_score = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_account'
