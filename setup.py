from setuptools import find_packages, setup

setup(
    name="mcqgenerator",
    version="0.0.1",
    author="Sulphite",
    author_email="aqibaabdulqadir@gmail.com",
    install_requires=["openai", "langchain", "streamlit", "python-dotenv", "pyPDF2"],
    packages=find_packages(),
)