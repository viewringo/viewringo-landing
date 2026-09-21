#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate index.html (en), index_ja.html and index_zh.html from index_ko.html.

    python3 scripts/i18n/build_pages.py         # from the repo root

index_ko.html is the single source of truth for markup and copy. Edit Korean copy there, add the
translation to scripts/i18n/strings.py, re-run this script. Never hand-edit the three generated files.
The script fails loudly if any Korean text survives in a generated page (other than the '한국어' entry
in the language menu), so a missing translation cannot slip through."""
import re, sys, os
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from strings import STRINGS

HANGUL = re.compile(r'[\uac00-\ud7a3]')
LANGS = {
    # code: (file, html lang, font family param, language menu label, mailto address)
    'en': ('index.html',    'en', None,                              'English', 'sales@viewringo.com'),
    'ja': ('index_ja.html', 'ja', 'Noto+Sans+JP:wght@300;400;500;700', '日本語',  'support@viewringo.com'),
    'zh': ('index_zh.html', 'zh', 'Noto+Sans+SC:wght@300;400;500;700', '中文',    'support@viewringo.com'),
}
IDX = {'en': 0, 'ja': 1, 'zh': 2}

src = open(os.path.join(ROOT, 'index_ko.html'), encoding='utf-8').read()

def translate(s, code):
    i = IDX[code]
    # longest keys first so a short key never clips a longer one
    for ko in sorted(STRINGS, key=len, reverse=True):
        tr = STRINGS[ko][i]
        esc = re.escape(ko)
        # text nodes (keep surrounding whitespace) and attribute values
        s = re.sub(r'>(\s*)' + esc + r'(\s*)<', lambda m: '>' + m.group(1) + tr + m.group(2) + '<', s)
        s = re.sub(r'="' + esc + r'"', '="' + tr.replace('\\', '\\\\') + '"', s)
    return s

for code, (fname, lang, font, label, mail) in LANGS.items():
    s = src
    s = s.replace('<html lang="ko">', '<html lang="%s">' % lang)
    s = s.replace('https://www.viewringo.com/index_ko.html', 'https://www.viewringo.com/' + fname)  # canonical + og:url
    if font:
        s = s.replace('Noto+Sans+KR:wght@300;400;500;700', font)
    else:
        s = s.replace('&family=Noto+Sans+KR:wght@300;400;500;700', '')
    # language menu: summary shows the current language; aria-current moves with it
    s = s.replace('<summary>한국어</summary>', '<summary>%s</summary>' % label)
    s = s.replace('<a href="index_ko.html" hreflang="ko" aria-current="true">한국어</a>', '<a href="index_ko.html" hreflang="ko">한국어</a>')
    s = s.replace('<a href="%s" hreflang="%s">' % (fname, lang), '<a href="%s" hreflang="%s" aria-current="true">' % (fname, lang))
    s = s.replace('mailto:support@viewringo.com">support@viewringo.com', 'mailto:%s">%s' % (mail, mail))
    # legal pages exist in Korean and English only; every non-Korean page links to the English versions
    s = s.replace('href="privacy_ko.html"', 'href="privacy.html"').replace('href="terms_ko.html"', 'href="terms.html"')
    s = translate(s, code)
    # residue check: the only Korean allowed is the '한국어' item in the language menu
    left = [ln for ln in s.splitlines() if HANGUL.search(ln) and '>한국어</a>' not in ln]
    if left:
        sys.exit('Untranslated Korean remains in %s:\n  ' % fname + '\n  '.join(ln.strip()[:120] for ln in left))
    assert s.count('aria-current="true"') == 1, fname
    open(os.path.join(ROOT, fname), 'w', encoding='utf-8').write(s)
    print('%s: %d KB, lang=%s, menu=%s, mailto=%s' % (fname, len(s.encode('utf-8')) // 1024, lang, label, mail))
