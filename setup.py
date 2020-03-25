from setuptools import setup, find_packages

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='msg91-sms-otp',
    packages=find_packages(),
    version='0.0.3',
    license='MIT',
    description='A tiny library for sending OTP and SMS via MSG91',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Selvamani Kannan',
    author_email='selvamanikannan55@gmail.com',
    url='',
    keywords=['msg91', 'sms', 'otp', 'sms-otp','sms-otp','msg91-sms-otp'],
    install_requires=['requests'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)