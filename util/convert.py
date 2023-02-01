'''
Convert query string to WebKitFormBoundary Format
'''

from urllib.parse import unquote

txt = r"__EVENTTARGET=persinfo%24ctl01%24btnSubmit&__EVENTARGUMENT=&__VIEWSTATE="
txt = unquote(txt)
dic = {txt.split("=")[0]: txt.split("=")[1] for txt in txt.split("&")}

bound = """------WebKitFormBoundaryvoA5YjMd3Uf0m32z
Content-Disposition: form-data; name="%s"

%s
"""
out = ""
for item in dic:
    out += bound % (item, dic[item])
print(out)
