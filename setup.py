from distutils.core import setup

setup(
    name='django-chinook',
    version='1.0.0',
    author=u'Muhammed K K',
    author_email='bruno.renie.fr',
    packages=['chinook'],
    url='https://bitbucket.org/xeoscript/django-chinook',
    license='BSD licence, see LICENCE.txt',
    description='A django app with models for chinook sample database and fixtures.',
    long_description=open('README.txt').read(),
    zip_safe=False,
)