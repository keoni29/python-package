from setuptools import setup

setup(name='mypackage',
      version='0.1.1',
      description='My first python package',
      url='',
      author='Koen van Vliet',
      author_email='8by8mail@gmail.com',
      license='MIT',
      packages=['mypackage'],
      entry_points = {
        'console_scripts': ['myscript=mypackage.myscript:main']},
      zip_safe=False,
)