# 다국어 페이지 빌드

- **원본**: `index_ko.html` (마크업 + 한국어 카피)
- **번역 사전**: `strings.py` — 한국어 문자열 → (en, ja, zh)
- **생성**: 저장소 루트에서 `python3 scripts/i18n/build_pages.py` → `index.html`, `index_ja.html`, `index_zh.html`

생성된 세 파일은 직접 편집하지 않습니다. 카피를 바꾸려면 `index_ko.html`을 고치고 사전에 번역을 추가한 뒤 다시 빌드하세요.
빌드는 생성 페이지에 한글이 남아 있으면(언어 메뉴의 "한국어" 제외) 실패합니다 — 번역 누락 방지 장치입니다.
