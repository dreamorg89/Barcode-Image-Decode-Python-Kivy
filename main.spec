# -*- mode: python ; coding: utf-8 -*-

from kivy_deps import sdl2, glew, gstreamer

import win32api
import win32con
import win32file
import win32event
import win32service
import win32timezone
import win32serviceutil
from pylibdmtx import pylibdmtx
from pyzbar import pyzbar

block_cipher = None


a = Analysis(['main.py'],
             pathex=['\\'],
             binaries=[],
             datas=[('Test.kv', '.')],
             hiddenimports=['pyzbar','cv2','decode','numpy','scipy'],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

# dylibs not detected because they are loaded by ctypes
a.binaries += TOC([
    (Path(dep._name).name, dep._name, 'BINARY')
    for dep in pylibdmtx.EXTERNAL_DEPENDENCIES + pyzbar.EXTERNAL_DEPENDENCIES
])

# A dependency of libzbar.dylib that PyInstaller does not detect
MISSING_DYLIBS = (
    Path('C:\Python39\Lib\site-packages\pyzbar\DynLib.dll'),
)
a.binaries += TOC([
    (lib.name, str(lib.resolve()), 'BINARY') for lib in MISSING_DYLIBS
])


exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,  
          [],
          name='main',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )
