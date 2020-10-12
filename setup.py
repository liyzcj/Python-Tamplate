"""A setuptools based setup module.
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / 'README.md').read_text(encoding='utf-8')

# Get About for project.
about: dict = {}
with open(here / "src/sample/__about__.py") as fp:
    exec(fp.read(), about)


# “必填” 表示必须填写才能上传 PyPI。
# “可选” 表示可以注释不填写。

setup(
    # 该项目的名称，这会决定用户如何安装这个包。例如：
    #
    # $ pip install sampleproject
    #
    # 这个名字会作为 PyPI 项目网址的一部分: https://pypi.org/project/sampleproject/
    #
    # 命名规范如下
    # https://packaging.python.org/specifications/core-metadata/#name
    name='sampleproject',  # 必填

    # 版本号应该符合 PEP 440 的规定:
    # https://www.python.org/dev/peps/pep-0440/
    #
    # 关于如何做到代码与 setup.py 文件中的版本一致性，可以查看：
    # https://packaging.python.org/en/latest/single_source_version.html
    version=about['__version__'],  # 必填

    # 项目作者或者组织
    author=about['__author__'],  # 可选

    # 项目持有者的电子邮箱
    author_email=about['__email__'],  # 可选

    # 项目的简短描述. 对应着元数据字段 "Summary":
    # https://packaging.python.org/specifications/core-metadata/#summary
    description='A sample Python project',  # 可选

    # 项目长文描述，可以选择填写。这会在 PyPI 的项目主页中显示。
    #
    # 通常情况下，这个内容和项目中的 README 内容一致，所以这里直接读取 README 中的内容。
    #
    # 这一项对应项目元数据中的 "Description":
    # https://packaging.python.org/specifications/core-metadata/#description-optional
    long_description=long_description,  # 可选

    # 决定上面的长描述的文本类型，这会决定 PyPI 如何渲染文本。可以选择的文本类型有：
    # text/plain, text/x-rst, and text/markdown
    #
    # 【 如果长描述是使用 reStructuredText (rst) 编写的，则可以省略这个选项，如果不是则必须填写，
    #    因为如果不指定, 应用会尝试使用 text/x-rst; charset=UTF-8 的格式渲染，如果不符合 rst 语法
    #    则会尝试 text/plain 渲染。】
    #
    # 这个参数对应元数据中的 "Description-Content-Type" 字段:
    # https://packaging.python.org/specifications/core-metadata/#description-content-type-optional
    long_description_content_type='text/markdown',  # 可选（rst）

    # 项目的主页。
    #
    # 这个参数对应着元数据中的 "Home-Page" 字段:
    # https://packaging.python.org/specifications/core-metadata/#home-page-optional
    # url='https://github.com/pypa/sampleproject',  # 可选

    # 作者的名称，或者拥有该项目的组织。
    # author='A. Random Developer',  # 可选

    # 作者或者组织的邮箱。
    # author_email='author@example.com',  # 可选

    # 项目的分类，这可以帮助用户在 PyPI 中根据类别找到这个项目。
    #
    # 查看 https://pypi.org/classifiers/ 可以获取所有的类别。
    classifiers=[  # 可选
        # 项目的阶段，可以填的值有：
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # 表明该项目的受众，以及项目的相关主题。
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # 选择一个可用的 License。
        'License :: OSI Approved :: MIT License',

        # 指定支持的 Python 版本，确保你支持 Python3。【安装时不会检查，仅仅作为分类使用】
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3 :: Only',
    ],

    # 项目的相关关键字。
    #
    # 关键字可以指定多个，由逗号隔开。关键字可以帮助用户找到需要的工具。
    # keywords='sample, setuptools, development',  # 可选

    # 当你的源代码不在根目录，而在一个子目录中, 例如
    # 代码在目录 `src/` 中，那么就必须指定这个参数。
    package_dir={'': 'src'},  # 可选

    # 如果你的项目比较简单，则可以手动指定包含的 Module，但是通常使用 find_packages() 自动查找。
    #
    # 此外，如果你仅仅想发布一个 Python 文件或着说 Module，则应该使用参数 `py_modules`，例如
    # 如果要添加一个名称为 `my_module.py` 的文件：
    #
    #   py_modules=["my_module"],
    #
    packages=find_packages(where='src'),  # 必填

    # 指定支持的 Python 版本，和上面的分类不同，这个会在 'pip install' 时进行版本检查。
    # https://packaging.python.org/guides/distributing-packages-using-setuptools/#python-requires
    python_requires='>=3.6, <4',  # 必填

    # 这个参数用来指定当前项目依赖的其他 Python 项目。
    # 所有的项目必须可以使用 pip 安装，并且是有效的 Python 项目。
    #
    # 一个比较 "install_requires" vs pip's requirements files 的文章:
    # https://packaging.python.org/en/latest/requirements.html
    # install_requires=['peppercorn'],  # 可选

    # 在这里列出额外的依赖 (例如，开发依赖、测试依赖)，用户可以使用 "extras" 语法来安装这些依赖，例如：
    #
    #   $ pip install sampleproject[dev]
    #
    # extras_require={  # 可选
    #     'dev': ['check-manifest'],
    #     'test': ['coverage'],
    # },

    # 如果有一些其他的数据文件需要和项目一起打包，则需要在这里指定。
    # package_data={  # 可选
    #     'sample': ['package_data.dat'],
    # },

    # 尽管 'package_data' 是比较推荐的添加数据的方法, 有时候你仍然需要在项目外部添加数据。查看:
    # http://docs.python.org/distutils/setupscript.html#installing-additional-files
    #
    # 这种情况下， 'data_file' 会被安装到 '<sys.prefix>/my_data' 目录下。
    # data_files=[('my_data', ['data/data_file'])],  # 可选

    # 如果要添加一个可执行的命令行脚本，则应该倾向使用 'entry_points' 而不是 'scripts' 参数。
    # Entry points 提供了跨平台的支持。
    #
    # 例如，下面的参数会添加命令 `sample`，这个命令会指定 'sample' 中的 'main' 函数:
    # entry_points={  # 可选
    #     'console_scripts': [
    #         'sample=sample:main',
    #     ],
    # },

    # 列出额外的 URL 地址，以字典的形式提供。
    #
    # 这个字段对应项目元数据中的 "Project-URL" 字段:
    # https://packaging.python.org/specifications/core-metadata/#project-url-multiple-use
    #
    # 下面这个例子中包含了 Bug 报告的地址，源代码的地址，感谢的地址，以及项目资金支持的地址。
    # 字典中的 Key 会作为链接 🔗 显示在 PyPI 中。
    # project_urls={  # 可选
    #     'Bug Reports': 'https://github.com/pypa/sampleproject/issues',
    #     'Funding': 'https://donate.pypi.org',
    #     'Say Thanks!': 'http://saythanks.io/to/example',
    #     'Source': 'https://github.com/pypa/sampleproject/',
    # },
)
