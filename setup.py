from setuptools import setup

setup(
    name = 'cliweather_dicky',
    version = '0.1',
    py_modules = ['cliweather'],
    install_requires = [
        'Click',
    ],
    entry_points = '''
        [console_scripts]
        cliweather=cliweather_dicky.main:cli
    ''',
)