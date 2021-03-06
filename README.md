## 一、环境配置
1. VSCode  下载，安装python ，chinese，path intellisence，npm ，npm intellisence   ,Vetur，Vue3 Snippets ,vscode-icons，live server 这些插件

2. 配置终端

   切换到cmd

3. 安装前端开发工具HbuilderX   https://www.dcloud.io/hbuilderx.html

4. 安装小程序开发工具   https://developers.weixin.qq.com/miniprogram/dev/devtools/download.html


## 二、安装git：https://git-scm.com/；

1. 创建远程仓库myBlog

2. 初始化本地仓库，也就是在本地的myBLog文件夹下执行：`git init`，执行完后会创建一个.git的隐藏文件

3. 远程仓库和本地仓库进行关联：`git remote add origin "你的远程仓库地址"`

4. 如果出现错误，ssh没有创建

5. 先去创建密钥：`ssh-keygen` ，一路enter，生成密钥

6. 查看生成的密钥   `cat ~/.ssh/id_rsa.pub`，将密钥写入到github上的settings下的SSH and GPG keys下

7. 推送四步骤：

   git status           查看发生变化的文件

   git add .             追踪所有发生变化的文件

   git commit -m "备注"    提交到本地仓库

   git push -u origin master  第一次提交  到远程仓库

   git push  之后的提交

   

## 三、创建myBlog项目

1. 空文件夹下，执行 `django-admin startproject myBlog`;
2. 给myBlog创建虚拟环境，使用：`python -m venv env`
3. 进入到虚拟环境，windows下：`.\\env\\Scrtipst\\activate`;
4. 退出虚拟环境，windows下：`deactivate`；
5. 使用VSCode打开myBlog，执行：`python manage.py startapp articles`



## 四、创建articles的models
1. 创建model

2. 数据库同步

3. 在admin.py中注册model 

   

## 五、业务逻辑

1. 文章列表页，分页   
2. 文章详情页，评论
3. 全局搜索功能   Q
4. 最新文章，最新评论的排行
5. 按照分类，标签的一个聚类操作  
6. 联系我页面，发送邮件


## 六、将所有app归拢到apps文件夹下
import sys
sys.path.insert(0,os.path.join(BASE_DIR,'apps'))


## 七、评论和集成markdownx插件
django-contrib-comments
django-markdownx   


## 八、配置media路径

```python
# settings.py
MEDIA_ROOT = os.path.join(BASE_DIR,'media')
MEDIA_URL = '/media/'

# urls.py
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
```

## 九、快速注册账号，使用第三方框架：django-registration-redux

1. 允许注册：安装 registration
   pip install django-registration-redux
2. 添加到 apps 中 
   ```
   INSTALLED_APPS = [
       'django.contrib.sites',
       'registration', #should be immediately above 'django.contrib.admin'
       'django.contrib.admin',
       # ...other installed applications...
   ]
   ```
3. 同步数据库
 一阶段注册，用户注册后立即激活并登录。
   `path('accounts/', include('registration.backends.simple.urls')),`
4. 分两个阶段进行的注册，包括初始注册和确认电子邮件，以及有关激活新帐户的说明。
   `path('accounts/', include('registration.backends.default.urls')),`
5. 用户进行注册的三阶段注册通过电子邮件确认其帐户，然后管理员批准该帐户以允许用户登录。
   `path('accounts/', include('registration.backends.admin_approval.urls')),`

6. 同步数据库后，拥有这些接口
   accounts/login
   accounts/register
   accounts/logout


