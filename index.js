const express = require('express');
const puppeteer = require('puppeteer');

const app = express();
const port = process.env.PORT || 3000;

app.get('/', async (req, res) => {
  const browser = await puppeteer.launch({
    args: ['--no-sandbox', '--disable-setuid-sandbox'],
    headless: true // O Render.com exige que o Puppeteer seja executado em modo headless.
  });

  const page = await browser.newPage();
  await page.goto('https://google.com');

  // Aqui você pode inserir mais comandos do Puppeteer para interagir com a página, como tirar screenshots ou extrair informações.

  await browser.close();
  res.send('Hello World com Puppeteer e Express!');
});

app.listen(port, () => {
  console.log(`Servidor rodando na porta ${port}`);
});
