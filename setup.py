from setuptools import setup, find_packages

setup(
    name="log-learning",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "gitpython",
    ],
    entry_points={
        "console_scripts": [
            "log-learning=log_learning.main:main",
        ],
    },
    author="Mahdi Jamali",
    author_email="mahdijamali@gmail.com",
    description="A CLI tool to log daily learning and push to GitHub",
)