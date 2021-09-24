from distutils.core import setup

from Cython.Build import cythonize

setup(
    ext_modules=cythonize(
        ["cumprimenta.pyx", "python_th.pyx", "corre_pastas.pyx", "for_foda.pyx"]
    )
)
