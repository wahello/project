"""
Django settings for meiduomall project.

Generated by 'django-admin startproject' using Django 1.11.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#
#添加apps 项目应用目录到工程目录下
#insert(index,element) 将元素添加列表索引位置
sys.path.insert(0,os.path.join(BASE_DIR,'apps'))



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=x#0p6)2ua9u9%9qnomrlkvgo0#nkiw$&9&4yss33hy9l@_#)n'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['api.meiduo.site', '127.0.0.1', 'localhost', 'www.meiduo.site']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    #添加rest_framework模块
    'rest_framework',

    #应用文件中导入用户应用模块
    'users.apps.UsersConfig',

    #添加第三方QQ登录模块
    'oauth.apps.OauthConfig',

    #到入收货地址模块
    'area.apps.AreaConfig',
    #导入验证模块
    'verifications.apps.VerificationsConfig',

    #CORS来解决后端对跨域访问的支持
    'corsheaders',

    #使用django_celery_results模块异步发送短信验证码
    'celery',

    #导入商品模块
    'goods.apps.GoodsConfig',

    #导入广告数据模块
    'contents.apps.ContentsConfig',

    'ckeditor',  # 富文本编辑器
    'ckeditor_uploader',  # 富文本编辑器上传图片模块

    #添加定时模块　定时任务
    'django_crontab',

    # 使用haystack对接Elasticsearch  通过使用haystack来调用Elasticsearch搜索引擎
    #注册haystack应用
    'haystack',

    #注册购物车模块
    'carts.apps.CartsConfig',

    #订单模块
    'order.apps.OrderConfig',

    #payment
    'payment.apps.PaymentConfig',

    #使用xadmin模块
    'xadmin',
    'crispy_forms',
    'reversion',

]

# 配置Haystack的后端引擎
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'URL': 'http://192.168.22.135:9200/',  # 此处为elasticsearch运行的服务器ip地址，端口号固定为9200
        'INDEX_NAME': 'meiduo',  # 指定elasticsearch建立的索引库的名称
    },
}

# 当添加、修改、删除数据时，自动生成索引
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'





# 定时任务
CRONJOBS = [
    # 每5分钟执行一次生成主页静态文件
    ('*/1 * * * *', 'contents.crons.generate_static_index_html', '>>/home/python/Django_code/project_code/meiduomall/meiduomall/logs/crontab.log')
]

# 解决crontab中文问题
CRONTAB_COMMAND_PREFIX = 'LANG_ALL=zh_cn.UTF-8'



MIDDLEWARE = [

    #添加跨域访问中间键
    'corsheaders.middleware.CorsMiddleware',

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'meiduomall.urls'

# CORS　配置跨域的白名单　　凡是出现在白名单中的域名，都可以访问后端接口
CORS_ORIGIN_WHITELIST = (
    '127.0.0.1:8080',
    'localhost:8080',
    'www.meiduo.site:8080',
    'api.meiduo.site:8000'
)

# 指明在跨域访问中，后端是否支持对cookie的操作
CORS_ALLOW_CREDENTIALS = True  # 允许携带cookie

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'meiduomall.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    #主服务器
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'meiduo_mall', #数据库名
        'HOST': '127.0.0.1',  # 数据库主机
        'PORT': 3306,  # 数据库端口
        'USER': 'meiduo',  # 数据库用户名
        'PASSWORD': 'meiduo',  # 数据库用户密码
    },
    #从服务器
    'slave': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'meiduo_mall',  # 数据库名
        'HOST': '127.0.0.1',  # 数据库主机
        'PORT': 8306,  # 数据库端口
        'USER': 'root',  # 数据库用户名
        'PASSWORD': 'mysql',  # 数据库用户密码
    },

}

#数据库读写分离路由分配
DATABASE_ROUTERS = ['meiduomall.utils.db_router.MasterSlaveDBRouter']


#自定义的用户模型类
#AUTH_USER_MODEL 参数的设置以点.来分隔，表示应用名.模型类名。
#重载Django认证系统的模型类　使用我们自定义的模型类
AUTH_USER_MODEL = 'users.User'


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

#静态文件前缀
STATIC_URL = '/static/'

#REST_FRAMEWORK配置
REST_FRAMEWORK = {
    # 异常处理
    'EXCEPTION_HANDLER': 'meiduomall.utils.exceptions.exception_handler',

    #rest_franework默认的认证模块
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # 添加jwt认证模块组件
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
    # 分页
    'DEFAULT_PAGINATION_CLASS': 'meiduomall.utils.paginations.MYPageNumberPagination',
}
#设置jwt的token有效期时间
import datetime
JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=1),
    #重载obtain 视图的响应函数　增加返回值　　默认只返回用户登录的jwt_token标识
    'JWT_RESPONSE_PAYLOAD_HANDLER': "users.utils.jwt_response_payload_handler"
}

#重载django的认证系统后端　默认的后端只支持使用用户名登录
# 自定义django的认证系统的authenticate方法　增加使用手机号码登录
AUTHENTICATION_BACKENDS = [
    'users.utils.UsernameMobileAuthBackEnd',
]

#配置redis
CACHES = {

    #配置redis
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/0",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },

    #配置session保存到redis
    "session": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
    #配置保存图片验证码和短信验证码的redis库
    "verification":{
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/2",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
    #配置用户历史浏览记录缓存
    "history": {
            "BACKEND": "django_redis.cache.RedisCache",
            "LOCATION": "redis://127.0.0.1:6379/3",
            "OPTIONS": {
                "CLIENT_CLASS": "django_redis.client.DefaultClient",
            }
    },
    #配置缓存购物车缓存
    "cart": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/4",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },

}
#配置session保存redis缓存引擎 Django的Session机制使用redis保存
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "session"

#配置日志
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,  # 是否禁用已经存在的日志器
    'formatters': {  # 日志信息显示的格式
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(lineno)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(module)s %(lineno)d %(message)s'
        },
    },
    'filters': {  # 对日志进行过滤
        'require_debug_true': {  # django在debug模式下才输出日志
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {  # 日志处理方法
        'console': {  # 向终端中输出日志
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'file': {  # 向文件中输出日志
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(os.path.dirname(BASE_DIR), "logs/meiduo.log"),  # 日志文件的位置
            'maxBytes': 300 * 1024 * 1024,
            'backupCount': 10,
            'formatter': 'verbose'
        },
    },
    'loggers': {  # 日志器
        'django': {  # 定义了一个名为django的日志器
            'handlers': ['console', 'file'],  # 可以同时向终端与文件中输出日志
            'propagate': True,  # 是否继续传递日志信息
            'level': 'INFO',  # 日志器接收的最低日志级别
        },
    }
}

#第三方QQ登录配置信息
QQ_CLIENT_ID = '101474184'  #appid
QQ_CLIENT_SECRET = 'c6ce949e04e12ecc909ae6a8b09b637c' #appkey
QQ_REDIRECT_URI = 'http://www.meiduo.site:8080/oauth_callback.html' #回调域
QQ_STATE = '/' #client端的状态值。用于第三方应用防止CSRF攻击，成功授权后回调时会原样带回
QQ_SCOPE = 'get_user_info'


#邮件发送配置
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.163.com'
EMAIL_PORT = 25
#发送邮件的邮箱
EMAIL_HOST_USER = 'zgq722@163.com'
#在邮箱中设置的客户端授权密码
EMAIL_HOST_PASSWORD = 'qazwsx123'
#收件人看到的发件人
EMAIL_FROM = 'keys<zgq722@163.com>'



# DRF扩展
REST_FRAMEWORK_EXTENSIONS = {
    # 缓存时间
    'DEFAULT_CACHE_RESPONSE_TIMEOUT': 60 * 60*24,
    # 缓存存储
    'DEFAULT_USE_CACHE': 'default',
}


# django文件存储
DEFAULT_FILE_STORAGE = 'meiduomall.utils.fdfs.fdfs_storage.FastDFSStorage'

# FastDFS
FDFS_URL = 'http://image.meiduo.site:8888/'
FDFS_CLIENT_CONF = os.path.join(BASE_DIR, 'utils/fdfs/client.conf')

# 富文本编辑器ckeditor配置
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',  # 工具条功能
        'height': 300,  # 编辑器高度
        # 'width': 300,  # 编辑器宽
    },
}

CKEDITOR_UPLOAD_PATH = ''  # 上传图片保存路径，使用了FastDFS，所以此处设为''

# 生成的静态html文件保存目录
GENERATED_STATIC_HTML_FILES_DIR = os.path.join(os.path.dirname(os.path.dirname(BASE_DIR)), 'front_end_pc')

#第三方支付－支付宝应用
#支付宝应用id
ALIPAY_APPID= "2016091400513191"
#支付宝网关　https://openapi.alipaydev.com/gateway.do＋order_string
ALIPAY_URL="https://openapi.alipaydev.com/gateway.do"
#支付模式，True表示沙箱模式
ALIPAY_DEBUG =True


#第三方库静态文件目录
STATIC_ROOT = os.path.join(os.path.dirname(os.path.dirname(BASE_DIR)), 'front_end_pc/static')