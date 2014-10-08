from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
args_linear = ['/openmp', '/O2', '/favor:INTEL64']
args_nonlinear = ['/openmp', '/O2', '/favor:INTEL64', '/fp:fast']
ext_modules = [
    Extension('fsdt_commons_bc1', ['fsdt_commons_bc1.pyx'],
              extra_compile_args=args_linear),
    Extension('fsdt_donnell_bc1_linear', ['fsdt_donnell_bc1_linear.pyx'],
              extra_compile_args=args_linear),
    Extension('fsdt_commons_free', ['fsdt_commons_free.pyx'],
              extra_compile_args=args_linear),
    Extension('fsdt_donnell_free_linear', ['fsdt_donnell_free_linear.pyx'],
              extra_compile_args=args_linear),
    ]
setup(
name = 'fsdt_donnell',
cmdclass = {'build_ext': build_ext},
ext_modules = ext_modules
)
