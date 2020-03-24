from setuptools import setup

setup(name='sendotp',
      version='0.0.1',
      description='For sending OTP and SMS via MSG91',
      url='',
      author='Selvamani Kannan',
      author_email='selvamanikannan55@gmail.com',
      license='MIT',
      packages=['sendsms'],
      install_requires=['requests']
      zip_safe=False)