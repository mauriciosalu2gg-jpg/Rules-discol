import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Video Tag to use optimized versions
old_video_tag = """<video id="hero-video" autoplay loop muted playsinline poster="poster.jpg">
    <source src="cherry-blossom-neverness-to-everness-moewalls-com.mp4" type="video/mp4">
  </video>"""
new_video_tag = """<video id="hero-video" autoplay loop muted playsinline poster="poster.jpg">
    <source src="bg-optimized.webm" type="video/webm">
    <source src="bg-optimized.mp4" type="video/mp4">
  </video>"""
if old_video_tag in html:
    html = html.replace(old_video_tag, new_video_tag)
else:
    # try regex
    html = re.sub(r'<video id="hero-video"[^>]*>.*?<\/video>', new_video_tag, html, flags=re.DOTALL)

# 2. Fix the Navigation Observer issue by using a robust scroll event
# We remove navIO completely and add a scroll listener
old_nav_js = """  // ── Active nav highlight ──
  const sections = document.querySelectorAll('[id]');
  const links    = document.querySelectorAll('.nav a');

  const navIO = new IntersectionObserver((entries) => {
    entries.forEach(e => {
      if (e.isIntersecting) {
        links.forEach(a => a.classList.remove('active'));
        const a = document.querySelector(`.nav a[href="#${e.target.id}"]`);
        if (a) a.classList.add('active');
      }
    });
  }, { threshold: 0, rootMargin: '-80px 0px -80% 0px' });

  sections.forEach(s => navIO.observe(s));"""

new_nav_js = """  // ── Active nav highlight (Robust Scroll Listener) ──
  const sections = Array.from(document.querySelectorAll('section[id], main[id]'));
  const links = document.querySelectorAll('.nav a');
  
  window.addEventListener('scroll', () => {
    let current = '';
    const scrollY = window.scrollY;
    
    sections.forEach(sec => {
      const secTop = sec.offsetTop - 100; // offset for navbar
      const secHeight = sec.offsetHeight;
      if (scrollY >= secTop && scrollY < secTop + secHeight) {
        current = sec.getAttribute('id');
      }
    });
    
    links.forEach(a => {
      a.classList.remove('active');
      if (current && a.getAttribute('href') === '#' + current) {
        a.classList.add('active');
      }
    });
  }, { passive: true });"""

html = html.replace(old_nav_js, new_nav_js)

# Fallback just in case old_nav_js wasn't matched exactly (e.g. if I missed the exact threshold line earlier)
if "navIO" in html:
    html = re.sub(r'// ── Active nav highlight ──.*?sections\.forEach\(s => navIO\.observe\(s\)\);', new_nav_js, html, flags=re.DOTALL)


# 3. Aggressively remove any slow hover transitions from the CSS to make it 0 delay
html = re.sub(r'transition:\s*([^;}]+)', lambda m: 'transition: ' + re.sub(r'0\.\d+s', '0.05s', m.group(1)).replace('1.5s', '0.05s'), html)
# Let's fix the progress bars transition back so they actually animate
html = html.replace('width 0.05 cubic-bezier', 'width 1.5s cubic-bezier')
# Let's fix the enter screen fade transition so it doesn't snap instantly
html = html.replace('opacity 0.05 ease', 'opacity 0.8s ease')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("HTML rewrite complete")
