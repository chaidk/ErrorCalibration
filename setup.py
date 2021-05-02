from setuptools import setup

setup(
    name='ErrorCalibrationToos',
    scripts=['main.py']
    version='0.1.0',
    description='非线性误差校准工具',
    author='DKC',
    license='MIT',
    install_requires=['pycrypto==2.6.1'],
    python_requires='>=3'
)