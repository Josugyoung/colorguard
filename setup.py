from distutils.core import setup
import subprocess

setup(
      name='colorguard',
      version='0.01',
      packages=['colorguard'],
      install_requires=[
            'rex',
            'tracer',
            'harvester',
            'simuvex'
      ],
)
