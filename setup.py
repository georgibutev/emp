try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

setup(
    name='emp',
    version='0.1',
    description='Pylons Employees Application',
    author='Georgi Butev',
    author_email='georgibutev@gmail.com',
    url='',
    install_requires=[
        "Pylons>=1.0.1rc1",
        "SQLAlchemy>=0.8",
    ],
    setup_requires=["PasteScript>=1.6.3"],
    packages=find_packages(exclude=['ez_setup']),
    include_package_data=True,
    test_suite='nose.collector',
    package_data={'emp': ['i18n/*/LC_MESSAGES/*.mo']},
    #message_extractors={'emp': [
    #        ('**.py', 'python', None),
    #        ('templates/**.mako', 'mako', {'input_encoding': 'utf-8'}),
    #        ('public/**', 'ignore', None)]},
    zip_safe=False,
    paster_plugins=['PasteScript', 'Pylons'],
    entry_points="""
    [paste.app_factory]
    main = emp.config.middleware:make_app

    [paste.app_install]
    main = pylons.util:PylonsInstaller
    """,
)
