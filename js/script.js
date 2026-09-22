/* ViewRingo landing — shared script for all four language pages.
   All user-visible strings come from data-* attributes in the HTML, so this file stays language-agnostic. */
(function () {
  'use strict';

  /* ---------- hero slider: slide count derived from the DOM ---------- */
  var track = document.getElementById('heroTrack');
  var label = document.getElementById('heroTool');
  var ticksWrap = document.getElementById('heroTicks');
  var shots = track ? track.querySelectorAll('.hero-shot') : [];
  var total = shots.length;          // includes the duplicated first slide (seamless loop)
  var unique = total - 1;            // real platforms
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)');

  if (track && total > 1) {
    track.style.setProperty('--slide-count', total);

    for (var i = 0; i < unique; i++) {
      (function (idx) {
        var b = document.createElement('button');
        b.type = 'button';
        b.className = 'hero-tick';
        b.setAttribute('aria-label', shots[idx].getAttribute('data-tool'));
        b.addEventListener('click', function () { stop(); go(idx); start(); });
        ticksWrap.appendChild(b);
      })(i);
    }
    var ticks = ticksWrap.querySelectorAll('.hero-tick');
    var index = 0, autoTimer = null, snapTimer = null;

    function place(i, animate) {
      track.style.transition = animate ? 'transform 1s cubic-bezier(.65,0,.35,1)' : 'none';
      track.style.transform = 'translateX(' + (-i * (100 / total)) + '%)';
    }
    function paint(i) {
      var real = i >= unique ? 0 : i;
      if (label) label.textContent = shots[i].getAttribute('data-tool');
      for (var k = 0; k < ticks.length; k++) {
        ticks[k].classList.toggle('is-on', k === real);
        ticks[k].setAttribute('aria-current', k === real ? 'true' : 'false');
      }
    }
    function go(i) { index = i; place(i, true); paint(i); }
    function step() {
      var nx = index + 1;                // slides 0..unique-1 are real; slide `unique` is the duplicated first one
      place(nx, true); paint(nx); index = nx;
      if (nx === unique) {               // reached the duplicate: after the 1s slide, snap back to the real first slide
        snapTimer = window.setTimeout(function () { index = 0; place(0, false); paint(0); snapTimer = null; }, 1000);
      }
    }
    function stop() {
      if (autoTimer) { clearInterval(autoTimer); autoTimer = null; }
      if (snapTimer) { clearTimeout(snapTimer); snapTimer = null; }
    }
    function start() {
      stop();
      if (reduce.matches) return;      // reduced motion: static first slide
      autoTimer = window.setInterval(step, 3000);
    }

    place(0, false); paint(0); start();
    document.addEventListener('visibilitychange', function () { if (document.hidden) { stop(); } else { start(); } });
    if (reduce.addEventListener) { reduce.addEventListener('change', function () { stop(); go(0); start(); }); }
  }

  /* ---------- nav ---------- */
  var nav = document.getElementById('siteNav');
  var burger = document.getElementById('navBurger');
  var links = document.getElementById('navLinks');
  var lang = document.getElementById('langBox');

  function onScroll() { if (nav) nav.classList.toggle('is-stuck', window.scrollY > 12); }
  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });

  if (burger && links) {
    var labelOpen = burger.getAttribute('data-label-open') || burger.getAttribute('aria-label');
    var labelClose = burger.getAttribute('data-label-close') || labelOpen;
    burger.addEventListener('click', function () {
      var open = links.classList.toggle('is-open');
      burger.setAttribute('aria-expanded', open ? 'true' : 'false');
      burger.setAttribute('aria-label', open ? labelClose : labelOpen);
    });
    links.addEventListener('click', function (e) {
      if (e.target.tagName === 'A') { links.classList.remove('is-open'); burger.setAttribute('aria-expanded', 'false'); burger.setAttribute('aria-label', labelOpen); }
    });
  }
  document.addEventListener('click', function (e) { if (lang && lang.open && !lang.contains(e.target)) lang.open = false; });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && lang && lang.open) { lang.open = false; lang.querySelector('summary').focus(); }
  });

  /* ---------- contact form (EmailJS) ---------- */
  if (window.emailjs) { emailjs.init('o9OuOowb-wue0AEy-'); }

  var form = document.getElementById('contact-form');
  if (form) {
    var msgSending = form.getAttribute('data-sending') || 'Sending...';
    var msgSent = form.getAttribute('data-sent') || 'Your message has been sent successfully!';
    var msgFailed = form.getAttribute('data-failed') || 'Failed to send the message. Please try again later.';

    form.addEventListener('submit', function (event) {
      event.preventDefault();
      var btn = form.querySelector('button[type="submit"]');
      var original = btn.innerHTML;
      btn.disabled = true;
      btn.innerHTML = '<span class="spin" aria-hidden="true"></span>' + msgSending;

      var serviceID = 'service_gmqugw6';
      var templateID = 'template_7y2k35p';

      emailjs.sendForm(serviceID, templateID, form)
        .then(function () {
          alert(msgSent);
          form.reset();
        }, function (err) {
          alert(msgFailed + ' ' + JSON.stringify(err));
        })
        .finally(function () {
          btn.disabled = false;
          btn.innerHTML = original;
        });
    });
  }

  // ---- demo video: click-to-load YouTube (privacy-enhanced domain, no request before play)
  var video = document.getElementById('demoVideo');
  var playBtn = video && video.querySelector('.video-play');
  if (video && playBtn) {
    playBtn.addEventListener('click', function () {
      var id = video.getAttribute('data-video-id');
      if (!id) return;
      var frame = document.createElement('iframe');
      frame.src = 'https://www.youtube-nocookie.com/embed/' + encodeURIComponent(id) + '?autoplay=1&rel=0';
      frame.title = video.getAttribute('data-title') || '';
      frame.setAttribute('allow', 'accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share');
      frame.setAttribute('allowfullscreen', '');
      frame.setAttribute('referrerpolicy', 'strict-origin-when-cross-origin');
      video.replaceChild(frame, playBtn);
      frame.focus();
    });
  }
})();
