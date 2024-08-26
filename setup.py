from setuptools import setup, find_namespace_packages

setup(
    name='mkdocs-bootstrap-elements-plugin',
    version='0.1.6',  # Increment the version number
    description='A MkDocs plugin that adds Bootstrap accordions, modals, and cards.',
    long_description='This plugin allows you to easily add Bootstrap accordions, modals, and cards to your MkDocs site using custom Markdown syntax.',
    long_description_content_type='text/markdown',
    keywords='mkdocs python markdown bootstrap',
    url='https://github.com/kdkiss/mkdocs-bootstrap-elements-plugin',
    author='Your Name',
    author_email='your.email@example.com',
    license='MIT',
    python_requires='>=3.6',
    install_requires=[
        'mkdocs>=1.0.4',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    packages=find_namespace_packages(include=['mkdocs_bootstrap_elements_plugin*']),
    include_package_data=True,
    package_data={
        'mkdocs_bootstrap_elements_plugin': [
            'css/*.css',
            'js/*.js'
        ],
    },
    entry_points={
        'mkdocs.plugins': [
            'bootstrap_elements = mkdocs_bootstrap_elements_plugin:BootstrapElementsPlugin',
        ]
    },
    zip_safe=False
)