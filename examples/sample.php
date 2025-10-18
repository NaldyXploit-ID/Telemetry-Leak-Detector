<?php
// Simple PHP demo: JSON response for API mock
header('Content-Type: application/json; charset=utf-8');
$data = [
  'project' => getenv('PROJECT') ?: 'Telemetry-Leak-Detector',
  'time' => date('c'),
  'status' => 'ok',
];
echo json_encode($data, JSON_PRETTY_PRINT);
