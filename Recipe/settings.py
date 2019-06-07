
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'kf7e13hy!cft54d@f^twh!a)ov=j*ej1z)bd^^mq15q%pd*bsr'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'accounts.apps.AccountsConfig',
    'posts.apps.PostsConfig',
    'guest_home',
    'user_profile',
    'comments',
    'social_django',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'Recipe.urls'

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

                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',

            ],
        },
    },
]

WSGI_APPLICATION = 'Recipe.wsgi.application'




AUTHENTICATION_BACKENDS = [

    'django.contrib.auth.backends.ModelBackend',

    'social_core.backends.github.GithubOAuth2',
    'social_core.backends.linkedin.LinkedinOAuth2',

    'social_core.backends.facebook.FacebookOAuth2',

    'social_core.backends.google.GoogleOAuth2',
    ]


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {

        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'recipedb2',
        'USER': 'user2',
        'PASSWORD': 'user2@123',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators



# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'login'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

if DEBUG:
   STATIC_ROOT = "Projects/test_projects/new_design/Recipe-web-app/static"
STATICFILES_DIRS =(

os.path.join(BASE_DIR, "templates/static"),
)



SOCIAL_AUTH_GITHUB_KEY = '91e1d93236716e26e2b9'
SOCIAL_AUTH_GITHUB_SECRET ='9a478e68684acf8d567e800a168dc98a0da8e8e6'


LOGIN_URL = 'login'
LOGOUT_URL = 'logout'


SOCIAL_AUTH_FACEBOOK_KEY = '585819201928577'
SOCIAL_AUTH_FACEBOOK_SECRET = '6adb27c9272eb9992a2a805cbeca6172'


SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '856435669466-3brk7olhkmvntpgtmhrtu5vq8fm7dbt0.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'fXSMyW0J4QgH8hGJIqq33VAl'


SOCIAL_AUTH_LINKEDIN_OAUTH2_KEY = '811rl6kiistmhu'
SOCIAL_AUTH_LINKEDIN_OAUTH2_SECRET = 'ciznZCdqTGNCxsmX'
