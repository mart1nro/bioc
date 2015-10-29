__author__ = 'Yifan Peng'

from distutils.core import setup
setup(
    name = 'bioc',
    packages = ['bioc'], # this must be the same as the name above
    version = '1.0.dev2',
    description = 'Data structures and code to read/write BioC XML.',
    author = 'Yifan Peng',
    author_email = 'yfpeng@udel.edu',
    keywords = ['bioc'],
    license = 'BSD 3-clause license',
    url = 'https://github.com/yfpeng/pengyifan-pybioc',
    download_url = 'https://github.com/yfpeng/pengyifan-pybioc/releases/tag/1.0.dev1',
    classifiers = [
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'Environment :: MacOS X',
        'Environment :: X11 Applications :: Qt',
        'Environment :: Win32 (MS Windows)',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Microsoft',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Text Processing :: Markup :: XML',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
    ],
)