/*
 * Simple demo JS to manipulate DOM and show base64/hash examples.
 */
(function(){
  function b64Encode(s){ return btoa(unescape(encodeURIComponent(s))); }
  function md5Stub(s){
    // small non-cryptographic stub (demo only)
    let h=0; for(let i=0;i<s.length;i++){ h=(h<<5)-h + s.charCodeAt(i); h|=0; } return (h>>>0).toString(16);
  }
  const btn=document.getElementById('btn');
  const out=document.getElementById('output');
  btn.addEventListener('click',()=>{
    const txt="demo:"+new Date().toISOString();
    out.textContent = "b64:"+b64Encode(txt)+" | md5:"+md5Stub(txt);
  });
})();
