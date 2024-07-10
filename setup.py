from setuptools import setup,find_packages 



setup(
   name='flask_cli',
   version='o.1',
   packages=find_packages,
   entry_points={
       'console_scrpts':[
           'create-flask-app=flask_cli.cli:main'
       ]
   }

)