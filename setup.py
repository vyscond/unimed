from distutils.core import setup

cfg = {
    name: "nest",
    author: "Ramon Moraes",
    author_email: "ramon@vyscond.io",
    version: "0.1.0",
    description: "Client that return JSON format information from the UNIMED home page",
    long_description: "".join(open("README.md")),
    url: "https://github.com/vyscond/unimed",
    license: "MIT",
    packages: [
        "unimed"
    ],
}

setup(**cfg)
