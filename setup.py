from setuptools import setup


setup(
    name='Scrapy YAML item exporter',
    version='0.1.1',
    description='Very simple YAML item exporter for Scrapy',
    author='Eugenio Lacuesta',
    author_email='eugenio.lacuesta@gmail.com',
    license='BSD',
    packages=['scrapy_yaml_item_exporter'],
    install_requires=[
        'scrapy>=1.0',
        'ruamel.yaml>=0.15.0',
    ],
)
