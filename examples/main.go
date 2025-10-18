package main
import (
  "encoding/json"
  "fmt"
  "net/http"
  "time"
)
type Resp struct { Project string `json:"project"` Time string `json:"time"` Status string `json:"status"` }
func handler(w http.ResponseWriter, r *http.Request) {
  w.Header().Set("Content-Type","application/json")
  resp := Resp{Project: "Telemetry-Leak-Detector", Time: time.Now().Format(time.RFC3339), Status: "ok"}
  json.NewEncoder(w).Encode(resp)
}
func main(){
  http.HandleFunc("/", handler)
  fmt.Println("Listening on :8080")
  http.ListenAndServe(":8080", nil)
}
