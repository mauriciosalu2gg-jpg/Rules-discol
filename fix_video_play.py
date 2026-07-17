import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

play_js = """
    if(ambientAudio) {
      ambientAudio.volume = 0;
      ambientAudio.play().then(() => {
"""

new_play_js = """
    // Ensure video plays
    const heroVideo = document.getElementById('hero-video');
    if (heroVideo) { heroVideo.play().catch(e => console.log(e)); }
    
    if(ambientAudio) {
      ambientAudio.volume = 0;
      ambientAudio.play().then(() => {
"""

html = html.replace(play_js.strip(), new_play_js.strip())

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated video play logic")
