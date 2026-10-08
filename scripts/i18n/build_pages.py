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

# hreflang targets are the same on every page: each language points at its own file and never
# at the page being generated. x-default goes to English.
ALTERNATES = {'en': 'index.html', 'ko': 'index_ko.html', 'ja': 'index_ja.html', 'zh': 'index_zh.html'}
X_DEFAULT = 'index.html'
SITE = 'https://www.viewringo.com/'


def check_seo(s, fname):
    """Fail the build if canonical/og:url don't name this page, or if any hreflang drifted.

    A blanket URL replace used to rewrite the hreflang='ko' alternate as well, so every generated
    page told search engines its own URL was the Korean one. These assertions make that class of
    bug impossible to ship again."""
    want_self = SITE + fname
    for tag, pat in (('canonical', '<link rel="canonical" href="%s">'),
                     ('og:url', '<meta property="og:url" content="%s">')):
        assert s.count(pat % want_self) == 1, '%s: %s must be %s' % (fname, tag, want_self)
    for code, target in ALTERNATES.items():
        want = '<link rel="alternate" hreflang="%s" href="%s">' % (code, SITE + target)
        assert s.count(want) == 1, '%s: hreflang=%s must point at %s' % (fname, code, SITE + target)
    want_xd = '<link rel="alternate" hreflang="x-default" href="%s">' % (SITE + X_DEFAULT)
    assert s.count(want_xd) == 1, '%s: x-default must point at %s' % (fname, SITE + X_DEFAULT)

src = open(os.path.join(ROOT, 'index_ko.html'), encoding='utf-8').read()
check_seo(src, 'index_ko.html')  # the source's own head must already be correct

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
    # canonical and og:url name THIS page; the hreflang alternates below must keep pointing at
    # their own language's file, so rewrite the two tags by name instead of replacing every URL.
    s = s.replace('<link rel="canonical" href="https://www.viewringo.com/index_ko.html">',
                  '<link rel="canonical" href="https://www.viewringo.com/%s">' % fname)
    s = s.replace('<meta property="og:url" content="https://www.viewringo.com/index_ko.html">',
                  '<meta property="og:url" content="https://www.viewringo.com/%s">' % fname)
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
    check_seo(s, fname)
    open(os.path.join(ROOT, fname), 'w', encoding='utf-8').write(s)
    print('%s: %d KB, lang=%s, menu=%s, mailto=%s' % (fname, len(s.encode('utf-8')) // 1024, lang, label, mail))
