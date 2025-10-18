use std::time::{SystemTime, UNIX_EPOCH};
fn main(){
  let start = SystemTime::now();
  let since_epoch = start.duration_since(UNIX_EPOCH).unwrap().as_secs();
  println!("Project: Telemetry-Leak-Detector");
  println!("Epoch seconds: {}", since_epoch);
  println!("Rust demo: small CLI output");
}
