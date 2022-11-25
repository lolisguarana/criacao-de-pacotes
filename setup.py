from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt", "r") as f:
    requirements = f.read().splitlines()

setup(
    name="image-processing-louise",
    version="0.0.2",
    author="Louise Pereira das Neves",
    author_email="louiseneves87@gmail.com",
    description="Passo a passo passado por Karina Kato.",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lolisguarana/criacao-de-pacotes.git",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)        


