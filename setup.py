from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = ["os", "subprocess"], excludes = [])

base = 'Console'

executables = [
    Executable('webrofs-fuse', base=base)
]

setup(name='webrofs',
      version = 'git',
      description = 'Web Read Only File System',
      options = dict(build_exe = buildOptions),
      executables = executables)
