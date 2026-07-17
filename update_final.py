import re
import os

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update points (Silencio 1s -> Silencio 7d)
html = html.replace('Silencio 1s', 'Silencio 7d')

# 2. Update video src
html = html.replace('src="bg.mp4"', 'src="cherry-blossom-neverness-to-everness-moewalls-com.mp4"')

# 3. Remove ambientAudio logic because the file was deleted
audio_js = """
    if(ambientAudio) {
      ambientAudio.volume = 0;
      ambientAudio.play().then(() => {
        let vol = 0;
        let fade = setInterval(() => {
          vol += 0.05;
          if (vol >= 0.5) {
            clearInterval(fade);
          } else {
            ambientAudio.volume = vol;
          }
        }, 100);
      }).catch(e => console.log('Audio autoplay blocked', e));
    }
"""
html = html.replace(audio_js.strip(), "")
# and remove the audio tag
html = re.sub(r'<audio id="ambient-audio" src="ambient.mp3" loop></audio>\s*', '', html)
html = re.sub(r'const ambientAudio = document\.getElementById\(\'ambient-audio\'\);\s*', '', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated HTML with new video path and fixed points")
