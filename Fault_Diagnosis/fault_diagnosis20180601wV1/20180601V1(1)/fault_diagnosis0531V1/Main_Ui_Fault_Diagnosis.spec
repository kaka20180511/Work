# -*- mode: python -*-

block_cipher = None


a = Analysis(['Main_Ui_Fault_Diagnosis.py'],
             pathex=['D:\\TestPyQt5\\fault_diagnosis0529V2'],
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
          name='Main_Ui_Fault_Diagnosis',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
