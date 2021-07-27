import setuptools

setuptools.setup(
    name="python-sendfox-api",
    version="0.1.2",
    author="Smirnov.EV",
    author_email="knyazz@gmail.com",
    url="https://github.com/knyazz/python-sendfox-api",
    description="A straighforward python client for Sendfox API",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    keywords=["sendfox", "python sendfox api"],
    install_requires=[
        # certifi-2021.5.30 charset-normalizer-2.0.3 idna-3.2 urllib3-1.26.6
        "requests==2.26.0"
    ],
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Intended Audience :: Developers",
        "Development Status :: 4 - Beta"
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
