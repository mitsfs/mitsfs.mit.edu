import os
import stat

def postBuild(site):
    path = os.path.join(site.build_path, 'pinkdex/pinkdex.py')
    st = os.stat(path)
    os.chmod(path, st.st_mode | stat.S_IEXEC)
