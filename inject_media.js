const fs = require('fs');
const path = require('path');

const htmlPath = path.join(__dirname, 'index.html');
const videoPath = path.join(__dirname, 'bg.mp4');
const audioPath = path.join(__dirname, 'bg.mp3');

let html = fs.readFileSync(htmlPath, 'utf8');

if (fs.existsSync(videoPath)) {
  const videoBase64 = fs.readFileSync(videoPath, 'base64');
  const videoDataUrl = `data:video/mp4;base64,${videoBase64}`;
  html = html.replace('src="bg.mp4"', `src="${videoDataUrl}"`);
  console.log('Video injected.');
} else {
  console.log('Video file not found.');
}

if (fs.existsSync(audioPath)) {
  const audioBase64 = fs.readFileSync(audioPath, 'base64');
  const audioDataUrl = `data:audio/mpeg;base64,${audioBase64}`;
  html = html.replace('src="bg.mp3"', `src="${audioDataUrl}"`);
  console.log('Audio injected.');
} else {
  console.log('Audio file not found.');
}

fs.writeFileSync(htmlPath, html, 'utf8');
console.log('Injection complete.');
