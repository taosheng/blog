
const CDP = require('chrome-remote-interface');
const argv = require('minimist')(process.argv.slice(2));
const fs = require('fs');

const targetURL = argv.url || 'https://www.shopback.com.tw';
const outfileName = argv.f || 's.png';
const delay = argv.d || 10;
console.log(outfileName)
const viewport = [1680,3072];
const screenshotDelay = 1000*delay; // ms
const fullPage = argv.fullPage || true;

if(fullPage){
  console.log("will capture full page")
}

CDP(async function(client){
  const {DOM, Emulation, Network, Page, Runtime} = client;

  // Enable events on domains we are interested in.
  await Page.enable();
  await DOM.enable();
  await Network.enable();

  // change these for your tests or make them configurable via argv
  var device = {
    width: viewport[0],
    height: viewport[1],
    deviceScaleFactor: 0,
    mobile: false,
    fitWindow: false
  };

  // set viewport and visible size
  await Emulation.setDeviceMetricsOverride(device);
  await Emulation.setVisibleSize({width: viewport[0], height: viewport[1]});
  const start =  Date.now() / 1000.0;

  await Page.navigate({url: targetURL});

  Page.loadEventFired(async() => {
    if (fullPage) {
         console.log("get full pages")
          const end =  Date.now() / 1000.0;
      
         console.log(end-start);
    }
    client.close();
  });


}).on('error', err => {
  console.error('Cannot connect to browser:', err);
});

