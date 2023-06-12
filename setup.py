from setuptools import setup, find_packages


REQUIRES = [
    'requests',
    'structlog',
    'pydantic',
    'allure-pytest',
]

setup(
    name='dm_api_account_gen',
    version='0.0.1',
    packages=find_packages(),
    url='https://github.com/surovp/dm_api_account_gen.git',
    license='MIT',
    author='Pavel Surov',
    author_email='-',
    install_requires=REQUIRES,
    description='Generated Client with apis and models'
)
