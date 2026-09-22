#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate the legal pages: privacy_ko.html / privacy.html / terms_ko.html / terms.html.

    python3 scripts/legal/build_legal.py     # from the repo root

Page bodies live in this file so header/footer/head stay identical to the landing pages.
Effective dates are defined below; bump only the document whose text changes."""
import os
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PRIVACY_EFFECTIVE = {'ko': '2026년 9월 21일', 'en': 'September 21, 2026'}
TERMS_EFFECTIVE = {'ko': '2026년 9월 22일', 'en': 'September 22, 2026'}

GA = '''<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-WHQVKQ58P6"></script>
<script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());

    gtag('config', 'G-WHQVKQ58P6');
</script>'''

def page(lang, fname, title, desc, alt_href, alt_label, home_href, home_label, other_href, other_label, body):
    font = 'Manrope:wght@400;500;600;700;800' + ('&family=Noto+Sans+KR:wght@300;400;500;700' if lang == 'ko' else '')
    privacy_href = 'privacy_ko.html' if lang == 'ko' else 'privacy.html'
    terms_href = 'terms_ko.html' if lang == 'ko' else 'terms.html'
    privacy_label = '개인정보 처리방침' if lang == 'ko' else 'Privacy Policy'
    terms_label = '이용약관' if lang == 'ko' else 'Terms of Service'
    return f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} — ViewRingo</title>
<meta name="description" content="{desc}">
<meta name="robots" content="noindex, follow">
<link rel="canonical" href="https://www.viewringo.com/{fname}">
<link rel="alternate" hreflang="{lang}" href="https://www.viewringo.com/{fname}">
<link rel="alternate" hreflang="{'en' if lang == 'ko' else 'ko'}" href="https://www.viewringo.com/{alt_href}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family={font}&display=swap" rel="stylesheet">
<link href="css/style.css" rel="stylesheet">
{GA}
</head>
<body>
<header class="legal-head">
  <div class="wrap">
    <a href="{home_href}" aria-label="ViewRingo"><img src="images/logos/viewringo.png" alt="ViewRingo"></a>
    <nav>
      <a href="{home_href}">{home_label}</a>
      <a href="{other_href}">{other_label}</a>
      <a href="{alt_href}" hreflang="{'en' if lang == 'ko' else 'ko'}">{alt_label}</a>
    </nav>
  </div>
</header>
<main class="legal">
{body}
</main>
<footer class="foot">
  <div class="wrap foot-in">
    <img src="images/logos/viewringo.png" alt="ViewRingo">
    <div>
      <p class="meta"><b>&copy; 2025 ViewRingo. All rights reserved.</b>ViewRingo | Enterprise Analytics Portal</p>
      <p class="foot-links"><a href="{privacy_href}">{privacy_label}</a><span>·</span><a href="{terms_href}">{terms_label}</a></p>
    </div>
  </div>
</footer>
</body>
</html>
'''

# ============================================================ PRIVACY (KO)
PRIVACY_KO = f'''<h1>개인정보 처리방침</h1>
<p class="eff">시행일: {PRIVACY_EFFECTIVE['ko']}</p>
<p class="intro">ViewRingo(이하 "회사")는 「개인정보 보호법」 등 관련 법령을 준수하며, 회사가 운영하는 웹사이트(www.viewringo.com, 이하 "웹사이트")를 통해 수집하는 개인정보를 다음과 같이 처리합니다.</p>

<h2>1. 적용 범위</h2>
<p>이 방침은 웹사이트 방문자와, 웹사이트의 문의 양식 또는 이메일로 회사에 연락하는 분의 개인정보에 적용됩니다. 회사가 고객사에 공급하는 ViewRingo Enterprise Analytics Portal 소프트웨어(이하 "제품") 안에서 처리되는 개인정보에 관하여는 제10조를 참고하시기 바랍니다.</p>

<h2>2. 수집하는 개인정보의 항목 및 수집 방법</h2>
<div class="tbl"><table>
<thead><tr><th>구분</th><th>항목</th><th>수집 방법</th></tr></thead>
<tbody>
<tr><td>문의 양식</td><td>이름, 이메일 주소, 문의 내용(이용자가 메시지에 직접 기재한 정보 포함)</td><td>이용자가 웹사이트의 "문의하기" 양식을 작성하여 전송할 때</td></tr>
<tr><td>이메일 문의</td><td>발신자 이메일 주소, 이름, 문의 내용</td><td>이용자가 sales@viewringo.com 또는 support@viewringo.com으로 직접 이메일을 보낼 때</td></tr>
<tr><td>자동 수집 정보</td><td>방문 일시, 열람한 페이지, 브라우저·기기 종류, 화면 해상도, 유입 경로, 대략적인 위치(국가·도시 수준), 쿠키 식별자</td><td>웹사이트 이용 시 Google Analytics를 통해 자동으로 수집</td></tr>
</tbody></table></div>
<p>회사는 웹사이트에서 회원가입을 받지 않으며, 주민등록번호 등 고유식별정보나 민감정보를 수집하지 않습니다.</p>

<h2>3. 개인정보의 처리 목적</h2>
<ol>
<li>제품 문의, 도입 상담, 견적 요청에 대한 응대 및 회신</li>
<li>제품 소개 자료 제공 및 이용자가 요청한 범위의 후속 연락</li>
<li>웹사이트 이용 통계 분석 및 서비스 개선</li>
<li>법령상 의무 이행 및 분쟁 대응</li>
</ol>

<h2>4. 개인정보의 보유 및 이용 기간</h2>
<ul>
<li><b>문의 관련 정보</b>: 문의 처리 완료 후 3년간 보관(재문의, 계약 협의, 분쟁 대응 목적)한 뒤 지체 없이 파기합니다. 이용자가 삭제를 요청하면 법령상 보관 의무가 없는 한 즉시 파기합니다.</li>
<li><b>자동 수집 정보</b>: Google Analytics의 데이터 보존 기간 설정에 따라 최대 14개월간 보관됩니다.</li>
<li><b>파기 방법</b>: 전자 파일은 복구할 수 없는 방법으로 삭제하고, 출력물은 분쇄 또는 소각합니다.</li>
</ul>

<h2>5. 개인정보의 제3자 제공</h2>
<p>회사는 이용자의 개인정보를 제3자에게 제공하지 않습니다. 다만 이용자가 별도로 동의한 경우 또는 법령에 특별한 규정이 있는 경우에는 예외로 합니다.</p>

<h2>6. 개인정보 처리의 위탁 및 국외 이전</h2>
<p>회사는 웹사이트 운영을 위해 다음과 같이 개인정보 처리를 위탁하며, 이 과정에서 개인정보가 국외로 이전됩니다.</p>
<div class="tbl"><table>
<thead><tr><th>수탁자(이전받는 자)</th><th>이전 국가</th><th>이전 항목</th><th>이전 시기·방법</th><th>위탁 업무(목적)</th><th>보유·이용 기간</th></tr></thead>
<tbody>
<tr><td>EmailJS<br><a href="https://www.emailjs.com/legal/privacy-policy/" rel="noopener" target="_blank">개인정보 처리방침</a></td><td>수탁자의 클라우드 인프라 소재국(미국 등)</td><td>문의 양식의 이름, 이메일 주소, 문의 내용</td><td>이용자가 문의 양식을 전송할 때 네트워크를 통해 전송</td><td>문의 양식 내용을 회사 이메일로 전달(이메일 발송 중계)</td><td>발송 처리 후 수탁자 정책에 따른 발송 이력 보관 기간</td></tr>
<tr><td>Google LLC<br><a href="https://policies.google.com/privacy" rel="noopener" target="_blank">개인정보 처리방침</a></td><td>미국</td><td>제2조의 자동 수집 정보</td><td>웹사이트 이용 시 네트워크를 통해 자동 전송</td><td>웹사이트 이용 통계 분석(Google Analytics)</td><td>최대 14개월</td></tr>
</tbody></table></div>
<p>국외 이전을 원하지 않는 이용자는 문의 양식 대신 이메일로 직접 연락하실 수 있으며(EmailJS 미사용), 제8조의 방법으로 Google Analytics의 수집을 거부하실 수 있습니다.</p>

<h2>7. 정보주체의 권리·의무 및 행사 방법</h2>
<ul>
<li>이용자는 언제든지 자신의 개인정보에 대한 열람, 정정·삭제, 처리정지를 요구할 수 있습니다.</li>
<li>권리 행사는 <a href="mailto:support@viewringo.com">support@viewringo.com</a>으로 요청하시면 되며, 회사는 지체 없이(10일 이내) 조치합니다.</li>
<li>법정대리인이나 위임을 받은 자를 통하여 권리를 행사할 수 있으며, 이 경우 위임장을 제출하여야 합니다.</li>
<li>법령에서 개인정보의 보존을 요구하는 경우 등에는 요구를 제한할 수 있으며, 그 사유를 통지합니다.</li>
</ul>

<h2>8. 쿠키 및 분석 도구</h2>
<p>웹사이트는 이용 통계를 위해 Google Analytics 4를 사용하며, 이를 위해 이용자의 브라우저에 쿠키가 저장됩니다. Google Analytics 4는 IP 주소를 저장하지 않으며 대략적인 위치 정보만 도출합니다. 웹사이트는 광고 목적의 쿠키를 사용하지 않습니다.</p>
<ul>
<li>브라우저 설정에서 쿠키 저장을 거부하거나 삭제할 수 있습니다. 이 경우에도 웹사이트 열람에는 지장이 없습니다.</li>
<li><a href="https://tools.google.com/dlpage/gaoptout" rel="noopener" target="_blank">Google Analytics 차단 브라우저 부가기능</a>을 설치하면 Google Analytics의 수집을 차단할 수 있습니다.</li>
</ul>

<h2>9. 개인정보의 안전성 확보 조치</h2>
<ul>
<li>개인정보에 접근할 수 있는 인원을 업무상 필요한 최소한으로 제한</li>
<li>웹사이트 및 문의 전송 구간의 암호화(HTTPS/TLS)</li>
<li>문의 정보가 수신·보관되는 이메일 계정의 접근 통제 및 다단계 인증</li>
<li>보유 기간 경과 시 파기 절차 운영</li>
</ul>

<h2>10. 제품(ViewRingo)에서의 개인정보 처리</h2>
<p>제품은 고객사의 자체 환경(온프레미스 또는 고객사가 계약한 클라우드)에 설치·운영되며, 제품 이용자의 계정 정보와 활동 로그 등은 고객사가 개인정보처리자로서 관리합니다. 회사는 제품을 통해 고객사 이용자의 개인정보를 수집하거나 회사의 서버로 전송하지 않습니다.</p>
<p>유지보수·기술지원 계약에 따라 회사가 고객사 환경에 접근하는 경우에는 해당 계약과 고객사의 지침에 따라 필요한 최소한의 범위에서만 처리합니다. 제품의 AI 분석 기능은 고객사가 선택하고 계약한 AI 서비스(LLM)와 연동되며, 해당 서비스에서의 처리 조건은 고객사와 서비스 제공자 간의 계약에 따릅니다.</p>

<h2>11. 개인정보 보호책임자 및 고충 처리</h2>
<ul>
<li><b>개인정보 보호책임자</b>: ViewRingo 고객지원 담당 · <a href="mailto:support@viewringo.com">support@viewringo.com</a></li>
<li>이용자는 개인정보 관련 문의, 불만 처리, 피해 구제 등을 위 연락처로 요청할 수 있으며, 회사는 지체 없이 답변합니다.</li>
</ul>
<p>기타 개인정보 침해에 대한 신고나 상담이 필요한 경우 아래 기관에 문의하실 수 있습니다.</p>
<ul>
<li>개인정보침해신고센터: 국번 없이 118 · <a href="https://privacy.kisa.or.kr" rel="noopener" target="_blank">privacy.kisa.or.kr</a></li>
<li>개인정보분쟁조정위원회: 1833-6972 · <a href="https://www.kopico.go.kr" rel="noopener" target="_blank">www.kopico.go.kr</a></li>
<li>대검찰청 사이버수사과: 국번 없이 1301</li>
<li>경찰청 사이버수사국: 국번 없이 182</li>
</ul>

<h2>12. 개인정보 처리방침의 변경</h2>
<p>이 방침의 내용이 추가·삭제·수정되는 경우 시행 7일 전(이용자 권리에 중요한 변경이 있는 경우 30일 전)부터 웹사이트에 공지합니다. 이 방침은 {PRIVACY_EFFECTIVE['ko']}부터 시행됩니다.</p>
'''

# ============================================================ PRIVACY (EN)
PRIVACY_EN = f'''<h1>Privacy Policy</h1>
<p class="eff">Effective date: {PRIVACY_EFFECTIVE['en']}</p>
<p class="intro">ViewRingo ("we", "us") operates the website www.viewringo.com (the "Website"). This policy explains what personal data we collect through the Website, why, and how you can exercise your rights. We process personal data in accordance with the Personal Information Protection Act of the Republic of Korea and, where applicable, other privacy laws such as the GDPR.</p>

<h2>1. Scope</h2>
<p>This policy applies to visitors of the Website and to anyone who contacts us through the Website's contact form or by email. For personal data processed inside the ViewRingo Enterprise Analytics Portal software that we supply to customers (the "Product"), see section 10.</p>

<h2>2. Data we collect and how</h2>
<div class="tbl"><table>
<thead><tr><th>Category</th><th>Data</th><th>How it is collected</th></tr></thead>
<tbody>
<tr><td>Contact form</td><td>Name, email address, message content (including anything you choose to write)</td><td>When you fill in and submit the "Contact us" form</td></tr>
<tr><td>Email enquiries</td><td>Sender email address, name, message content</td><td>When you email sales@viewringo.com or support@viewringo.com directly</td></tr>
<tr><td>Automatically collected data</td><td>Date and time of visit, pages viewed, browser and device type, screen resolution, referrer, approximate location (country/city level), cookie identifiers</td><td>Automatically via Google Analytics while you use the Website</td></tr>
</tbody></table></div>
<p>The Website has no user accounts. We do not collect government identifiers or special categories of personal data.</p>

<h2>3. Purposes and legal bases</h2>
<ol>
<li>Responding to product enquiries, evaluation requests and quotation requests (performance of pre-contractual steps at your request, or our legitimate interest in responding to you).</li>
<li>Sending product information and follow-up communication within the scope you requested (your consent, which you may withdraw at any time).</li>
<li>Analysing how the Website is used in order to improve it (your consent to analytics cookies, or our legitimate interest in aggregate usage statistics).</li>
<li>Complying with legal obligations and handling disputes.</li>
</ol>

<h2>4. Retention</h2>
<ul>
<li><b>Enquiry data</b>: kept for 3 years after the enquiry is closed (follow-up enquiries, contract discussions, dispute handling), then deleted without delay. If you ask us to delete it earlier, we do so unless the law requires us to keep it.</li>
<li><b>Analytics data</b>: retained for up to 14 months according to our Google Analytics data-retention setting.</li>
<li><b>Deletion</b>: electronic records are deleted irreversibly; printed copies are shredded.</li>
</ul>

<h2>5. Disclosure to third parties</h2>
<p>We do not sell or disclose your personal data to third parties, except with your separate consent or where required by law.</p>

<h2>6. Processors and international transfers</h2>
<p>We rely on the following service providers to operate the Website. Your data is transferred to them, including to countries outside the Republic of Korea.</p>
<div class="tbl"><table>
<thead><tr><th>Processor</th><th>Country</th><th>Data transferred</th><th>When and how</th><th>Purpose</th><th>Retention</th></tr></thead>
<tbody>
<tr><td>EmailJS<br><a href="https://www.emailjs.com/legal/privacy-policy/" rel="noopener" target="_blank">Privacy policy</a></td><td>Country of the processor's cloud infrastructure (including the United States)</td><td>Name, email address and message from the contact form</td><td>Transmitted over the network when you submit the contact form</td><td>Relaying contact-form submissions to our mailbox</td><td>Per the processor's delivery-log retention policy</td></tr>
<tr><td>Google LLC<br><a href="https://policies.google.com/privacy" rel="noopener" target="_blank">Privacy policy</a></td><td>United States</td><td>The automatically collected data in section 2</td><td>Transmitted automatically while you use the Website</td><td>Website usage analytics (Google Analytics)</td><td>Up to 14 months</td></tr>
</tbody></table></div>
<p>If you prefer not to have your data transferred this way, you can email us directly instead of using the contact form, and block Google Analytics as described in section 8. Where the GDPR applies, transfers rely on the recipient's standard contractual clauses or an equivalent safeguard.</p>

<h2>7. Your rights</h2>
<ul>
<li>You may request access to, correction or deletion of, or restriction of the processing of your personal data at any time, and you may withdraw consent you have given.</li>
<li>Send requests to <a href="mailto:support@viewringo.com">support@viewringo.com</a>. We respond without undue delay and within 10 days (or within one month where the GDPR applies).</li>
<li>You may act through an authorised representative; we will ask for proof of authorisation.</li>
<li>We may have to limit a request where the law requires us to keep the data; we will tell you why.</li>
<li>If you are in the EEA or UK you also have the right to lodge a complaint with your supervisory authority.</li>
</ul>

<h2>8. Cookies and analytics</h2>
<p>The Website uses Google Analytics 4 for usage statistics, which stores cookies in your browser. Google Analytics 4 does not log or store IP addresses and derives only coarse location. The Website does not use advertising cookies.</p>
<ul>
<li>You can refuse or delete cookies in your browser settings; the Website remains fully readable without them.</li>
<li>You can block Google Analytics entirely with the <a href="https://tools.google.com/dlpage/gaoptout" rel="noopener" target="_blank">Google Analytics opt-out browser add-on</a>.</li>
</ul>

<h2>9. Security</h2>
<ul>
<li>Access to personal data is limited to the minimum number of people who need it.</li>
<li>The Website and contact-form transmission are encrypted (HTTPS/TLS).</li>
<li>The mailbox that receives enquiries is protected by access control and multi-factor authentication.</li>
<li>Data is deleted once its retention period ends.</li>
</ul>

<h2>10. Personal data in the Product</h2>
<p>The Product is installed and operated in the customer's own environment (on-premise or in a cloud the customer contracts). User accounts, activity logs and similar data inside the Product are controlled by the customer, which acts as the data controller. We do not collect personal data of a customer's users through the Product, and the Product does not send such data to our servers.</p>
<p>Where a maintenance or support agreement gives us access to a customer environment, we process data only to the extent necessary and in accordance with that agreement and the customer's instructions. The Product's AI analytics features connect to the AI service (LLM) the customer selects and contracts; processing by that service is governed by the customer's agreement with the provider.</p>

<h2>11. Children</h2>
<p>The Website is intended for business audiences and is not directed at children under 14. We do not knowingly collect personal data from children.</p>

<h2>12. Contact</h2>
<p>Privacy officer: ViewRingo Customer Support · <a href="mailto:support@viewringo.com">support@viewringo.com</a>. Use this address for any question, request or complaint about personal data; we will reply without undue delay. Residents of the Republic of Korea may also contact the Personal Information Infringement Report Center (118, <a href="https://privacy.kisa.or.kr" rel="noopener" target="_blank">privacy.kisa.or.kr</a>) or the Personal Information Dispute Mediation Committee (1833-6972, <a href="https://www.kopico.go.kr" rel="noopener" target="_blank">www.kopico.go.kr</a>).</p>

<h2>13. Changes to this policy</h2>
<p>We announce changes on the Website at least 7 days before they take effect (30 days for changes that materially affect your rights). This policy is effective as of {PRIVACY_EFFECTIVE['en']}.</p>
'''

# ============================================================ TERMS (KO)
TERMS_KO = f'''<h1>이용약관</h1>
<p class="eff">시행일: {TERMS_EFFECTIVE['ko']}</p>
<p class="intro">이 약관은 ViewRingo(이하 "회사")가 운영하는 웹사이트 www.viewringo.com(이하 "웹사이트")의 이용 조건을 정합니다. 웹사이트를 이용함으로써 이용자는 이 약관에 동의한 것으로 봅니다.</p>

<h2>1. 정의</h2>
<ul>
<li><b>웹사이트</b>: 회사가 www.viewringo.com 및 그 하위 페이지를 통해 제공하는 정보와 기능 일체</li>
<li><b>이용자</b>: 웹사이트에 접속하여 열람하거나 문의 양식을 이용하는 모든 사람</li>
<li><b>제품</b>: 회사가 고객사에 공급하는 ViewRingo Enterprise Analytics Portal 소프트웨어와 관련 서비스</li>
<li><b>콘텐츠</b>: 웹사이트에 게시된 문서, 이미지, 화면 캡처, 로고, 디자인, 소스코드 등 일체의 자료</li>
</ul>

<h2>2. 약관의 효력 및 변경</h2>
<p>회사는 관련 법령을 위반하지 않는 범위에서 이 약관을 변경할 수 있으며, 변경된 약관은 웹사이트에 게시한 날부터 효력이 발생합니다. 이용자에게 불리한 변경은 시행 7일 전부터 공지합니다. 변경 후 웹사이트를 계속 이용하면 변경된 약관에 동의한 것으로 봅니다.</p>

<h2>3. 웹사이트의 이용</h2>
<ul>
<li>웹사이트는 제품과 회사를 소개하고 문의를 접수하기 위한 정보 제공 목적으로 운영되며, 별도의 회원가입 없이 이용할 수 있습니다.</li>
<li>이용자는 문의 양식에 정확한 정보를 기재하여야 하며, 타인의 정보를 도용해서는 안 됩니다.</li>
<li>회사는 운영상·기술상 필요에 따라 사전 통지 없이 웹사이트의 내용 또는 기능을 변경하거나 일시 중단할 수 있습니다.</li>
</ul>

<h2>4. 지식재산권</h2>
<ul>
<li>웹사이트의 콘텐츠에 관한 저작권 및 기타 지식재산권은 회사 또는 정당한 권리자에게 있습니다. ViewRingo 명칭과 로고는 회사의 상표입니다.</li>
<li>웹사이트에 표시된 Microsoft, Power BI, Power BI Report Server, Tableau, Qlik, Apache Superset, Longview, Strategy, Databricks 등 제3자의 명칭·로고·상표는 각 권리자의 자산이며, 제품이 해당 플랫폼과 연동됨을 설명하기 위해 표시한 것입니다. 이러한 표시가 각 권리자의 제휴, 후원 또는 보증을 의미하지는 않습니다.</li>
<li>웹사이트에 인용된 시장 조사 수치 등 제3자 자료는 출처를 함께 표기하며, 해당 자료의 권리는 각 출처에 있습니다.</li>
<li>이용자는 개인적·비상업적 열람 목적 외에 회사의 사전 서면 동의 없이 콘텐츠를 복제, 배포, 전송, 전시, 2차적 저작물 작성에 이용할 수 없습니다. 다만 출처(www.viewringo.com)를 표시한 링크 공유와 정당한 범위의 인용은 허용됩니다.</li>
</ul>

<h2>5. 금지행위</h2>
<p>이용자는 다음 행위를 하여서는 안 됩니다.</p>
<ol>
<li>자동화된 수단(크롤러, 스크래퍼 등)으로 콘텐츠를 대량 수집하는 행위. 다만 검색엔진의 통상적인 색인은 예외로 합니다.</li>
<li>웹사이트나 연동된 서비스의 취약점을 탐색·악용하거나, 정상적인 운영을 방해하는 행위</li>
<li>허위 또는 스팸성 문의를 전송하거나, 문의 양식을 광고·홍보 목적으로 이용하는 행위</li>
<li>타인의 개인정보를 무단으로 기재하거나 타인을 사칭하는 행위</li>
<li>관련 법령 또는 이 약관에 위반되는 행위</li>
</ol>

<h2>6. 제품 및 서비스</h2>
<ul>
<li>제품의 이용 조건, 라이선스 범위, 유지보수 및 기술지원은 회사와 고객사 간에 체결하는 별도의 소프트웨어 라이선스 계약 및 유지보수 계약에 따릅니다. 웹사이트의 제품 설명은 계약의 내용을 구성하지 않습니다.</li>
<li>웹사이트에 기재된 기능, 지원 플랫폼, 지원 범위는 제품 버전과 고객사 환경에 따라 달라질 수 있으며, 회사는 이를 사전 통지 없이 변경할 수 있습니다.</li>
<li>제3자 BI 플랫폼과의 연동은 각 플랫폼 제공자의 공식 임베딩·인증 방식과 이용 조건에 따르며, 해당 플랫폼의 이용 권한은 고객사가 별도로 확보하여야 합니다.</li>
</ul>

<h2>7. 제3자 서비스 및 링크</h2>
<p>웹사이트는 문의 양식 전송을 위해 EmailJS를, 이용 통계를 위해 Google Analytics를 사용하며, 외부 웹사이트로 연결되는 링크를 포함할 수 있습니다. 제3자 서비스와 외부 웹사이트는 각 제공자의 약관과 개인정보 처리방침이 적용되며, 회사는 그 내용에 대해 책임을 지지 않습니다. 개인정보 처리에 관한 사항은 <a href="privacy_ko.html">개인정보 처리방침</a>을 참고하시기 바랍니다.</p>

<h2>8. 보증의 부인 및 책임의 제한</h2>
<ul>
<li>웹사이트와 콘텐츠는 "있는 그대로" 제공되며, 회사는 콘텐츠의 정확성, 완전성, 최신성 또는 특정 목적에의 적합성을 보증하지 않습니다.</li>
<li>회사는 관련 법령이 허용하는 범위에서, 웹사이트의 이용 또는 이용 불능으로 인해 발생한 간접적·특별·결과적 손해에 대하여 책임을 지지 않습니다. 다만 회사의 고의 또는 중대한 과실로 인한 손해는 제외합니다.</li>
<li>이용자가 이 약관을 위반하여 회사 또는 제3자에게 손해를 발생시킨 경우 이용자는 그 손해를 배상할 책임이 있습니다.</li>
</ul>

<h2>9. 준거법 및 관할</h2>
<p>이 약관과 웹사이트 이용에 관한 분쟁에는 대한민국 법이 적용됩니다. 분쟁이 원만히 해결되지 않는 경우 민사소송법에 따른 관할 법원에 제소할 수 있습니다.</p>

<h2>10. 문의</h2>
<p>이 약관에 관한 문의는 <a href="mailto:support@viewringo.com">support@viewringo.com</a>으로 보내주시기 바랍니다.</p>

<h2>부칙</h2>
<p>이 약관은 {TERMS_EFFECTIVE['ko']}부터 시행합니다.</p>
'''

# ============================================================ TERMS (EN)
TERMS_EN = f'''<h1>Terms of Service</h1>
<p class="eff">Effective date: {TERMS_EFFECTIVE['en']}</p>
<p class="intro">These terms govern your use of the website www.viewringo.com (the "Website") operated by ViewRingo ("we", "us"). By using the Website you agree to these terms.</p>

<h2>1. Definitions</h2>
<ul>
<li><b>Website</b>: the information and functionality we provide at www.viewringo.com and its sub-pages.</li>
<li><b>User</b>: anyone who accesses the Website or uses its contact form.</li>
<li><b>Product</b>: the ViewRingo Enterprise Analytics Portal software and related services we supply to customers.</li>
<li><b>Content</b>: all material published on the Website, including text, images, screenshots, logos, design and source code.</li>
</ul>

<h2>2. Changes to these terms</h2>
<p>We may change these terms within the limits of applicable law. Changes take effect when published on the Website; changes that are unfavourable to users are announced at least 7 days in advance. Continued use of the Website after a change constitutes acceptance of the updated terms.</p>

<h2>3. Use of the Website</h2>
<ul>
<li>The Website exists to present the Product and our company and to receive enquiries. No account is required.</li>
<li>You must provide accurate information in the contact form and must not use another person's details.</li>
<li>We may change, suspend or discontinue any part of the Website at any time without notice for operational or technical reasons.</li>
</ul>

<h2>4. Intellectual property</h2>
<ul>
<li>Copyright and other intellectual property rights in the Content belong to us or to the respective rights holders. The ViewRingo name and logo are our trademarks.</li>
<li>Third-party names, logos and trademarks shown on the Website — including Microsoft, Power BI, Power BI Report Server, Tableau, Qlik, Apache Superset, Longview, Strategy and Databricks — are the property of their respective owners and are shown only to describe the platforms the Product integrates with. Their display does not imply affiliation, sponsorship or endorsement by those owners.</li>
<li>Third-party material quoted on the Website, such as market-research figures, is attributed to its source, which retains all rights.</li>
<li>Except for personal, non-commercial viewing, you may not reproduce, distribute, transmit, display or create derivative works from the Content without our prior written consent. Sharing links and quoting reasonable excerpts with attribution to www.viewringo.com is permitted.</li>
</ul>

<h2>5. Prohibited conduct</h2>
<ol>
<li>Bulk collection of Content by automated means (crawlers, scrapers), other than ordinary search-engine indexing.</li>
<li>Probing or exploiting vulnerabilities of the Website or its connected services, or interfering with their normal operation.</li>
<li>Sending false or spam enquiries, or using the contact form for advertising or solicitation.</li>
<li>Submitting another person's personal data without authorisation, or impersonating anyone.</li>
<li>Any conduct that violates applicable law or these terms.</li>
</ol>

<h2>6. Product and services</h2>
<ul>
<li>Use of the Product, the scope of its licence, and maintenance and support are governed by the separate software licence and maintenance agreements concluded between us and each customer. Product descriptions on the Website do not form part of any contract.</li>
<li>Features, supported platforms and support scope described on the Website may vary by Product version and customer environment and may change without notice.</li>
<li>Integration with third-party BI platforms relies on each provider's official embedding and authentication methods and terms; customers must hold their own entitlements to those platforms.</li>
</ul>

<h2>7. Third-party services and links</h2>
<p>The Website uses EmailJS to deliver contact-form submissions and Google Analytics for usage statistics, and may link to external websites. Those services and websites are governed by their own terms and privacy policies, for which we are not responsible. See our <a href="privacy.html">Privacy Policy</a> for how personal data is handled.</p>

<h2>8. Disclaimer and limitation of liability</h2>
<ul>
<li>The Website and its Content are provided "as is". We do not warrant that the Content is accurate, complete, current or fit for a particular purpose.</li>
<li>To the extent permitted by law, we are not liable for indirect, special or consequential damages arising from the use of, or inability to use, the Website, except where caused by our wilful misconduct or gross negligence.</li>
<li>You are liable for damage you cause to us or to third parties by breaching these terms.</li>
</ul>

<h2>9. Governing law and jurisdiction</h2>
<p>These terms and any dispute relating to the Website are governed by the laws of the Republic of Korea. Disputes that cannot be settled amicably are subject to the courts having jurisdiction under the Korean Civil Procedure Act.</p>

<h2>10. Contact</h2>
<p>Questions about these terms: <a href="mailto:support@viewringo.com">support@viewringo.com</a>.</p>

<h2>Effective date</h2>
<p>These terms take effect on {TERMS_EFFECTIVE['en']}.</p>
'''

PAGES = [
    ('ko', 'privacy_ko.html', '개인정보 처리방침', 'ViewRingo 웹사이트의 개인정보 처리방침 — 수집 항목, 목적, 보유 기간, 위탁·국외 이전, 정보주체의 권리.',
     'privacy.html', 'English', 'index_ko.html', '홈', 'terms_ko.html', '이용약관', PRIVACY_KO),
    ('en', 'privacy.html', 'Privacy Policy', 'ViewRingo website privacy policy — what we collect, why, retention, processors and international transfers, your rights.',
     'privacy_ko.html', '한국어', 'index.html', 'Home', 'terms.html', 'Terms of Service', PRIVACY_EN),
    ('ko', 'terms_ko.html', '이용약관', 'ViewRingo 웹사이트 이용약관 — 이용 조건, 지식재산권, 금지행위, 면책, 준거법.',
     'terms.html', 'English', 'index_ko.html', '홈', 'privacy_ko.html', '개인정보 처리방침', TERMS_KO),
    ('en', 'terms.html', 'Terms of Service', 'ViewRingo website terms of service — conditions of use, intellectual property, prohibited conduct, disclaimer, governing law.',
     'terms_ko.html', '한국어', 'index.html', 'Home', 'privacy.html', 'Privacy Policy', TERMS_EN),
]

if __name__ == '__main__':
    for args in PAGES:
        html = page(*args)
        out = os.path.join(ROOT, args[1])
        open(out, 'w', encoding='utf-8').write(html)
        print('%s: %d KB' % (args[1], len(html.encode('utf-8')) // 1024))
