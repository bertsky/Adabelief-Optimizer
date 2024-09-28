import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ocrd-fork-adabelief_tf",
    version="0.2.1",
    author="Juntang Zhuang",
    author_email="j.zhuang@yale.edu",
    description="Tensorflow implementation of AdaBelief Optimizer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bertsky/Adabelief-Optimizer/tree/pypi-fork/pypi_packages/adabelief_tf0.2.1",
    project_urls={
        "Bug Tracker": "https://github.com/bertsky/Adabelief-Optimizer/issues",
        "Upstream": "https://github.com/juntang-zhuang/Adabelief-Optimizer",
        "Pull Request": "https://github.com/juntang-zhuang/Adabelief-Optimizer/pull/68",
    },
    maintainer="bertsky",
    license="BSD-2-Clause",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
          'tensorflow>=2.0.0,<2.16.0',
      ],
    python_requires='>=3.6',
)
