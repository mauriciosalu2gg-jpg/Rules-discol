const fs = require('fs');
const path = require('path');

const imgPath = '/home/larita/Documentos/FLUX-MCP-DOC/Paginas-web/rules-discord-alero/hero.jpg';
const htmlPath = '/home/larita/Documentos/FLUX-MCP-DOC/Paginas-web/rules-discord-alero/index.html';

try {
  const imgBuffer = fs.readFileSync(imgPath);
  const base64Img = imgBuffer.toString('base64');
  const dataUrl = `data:image/jpeg;base64,${base64Img}`;

  let htmlContent = fs.readFileSync(htmlPath, 'utf8');
  
  // Reemplazar la URL por el Data URL
  htmlContent = htmlContent.replace(
    /background-image: url\('file:\/\/\/home\/larita\/Documentos\/FLUX-MCP-DOC\/Paginas-web\/rules-discord-alero\/hero\.jpg'\);/g,
    `background-image: url('${dataUrl}');`
  );

  fs.writeFileSync(htmlPath, htmlContent);
  console.log('Successfully injected base64 image into HTML');
} catch (e) {
  console.error('Error:', e);
}
