# -*- mode: python -*-

block_cipher = None


a = Analysis(['down_list.py'],
             pathex=['C:\\Users\\Administrator\\Desktop\\驱动器参数校验\\子函数模块\\HlsBk驱动器参数校验程序X3'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='down_list',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
