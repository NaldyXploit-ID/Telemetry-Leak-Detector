// Minimal TypeScript demo (compile with tsc if needed)
type Result = { input: string; b64: string; checksum: string };
function encode(s: string): Result {
  const b64 = Buffer.from(s, 'utf8').toString('base64');
  const checksum = Array.from(s).reduce((a,c)=>a + c.charCodeAt(0),0).toString(16);
  return { input: s, b64, checksum };
}
if (require.main === module) {
  const r = encode("ts-demo-"+new Date().toISOString());
  console.log(JSON.stringify(r, null, 2));
}
