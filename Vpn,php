<?php
header('Content-Type: application/json');

// استقبال بيانات تسجيل الدخول
$input = json_decode(file_get_contents('php://input'), true);

if ($input['username'] === 'admin' && $input['password'] === 'secret123') {
    // إرجاع تفاصيل الخادم والمفاتيح في حال نجاح الدخول
    echo json_encode([
        "status" => "success",
        "vpn_gateway" => "157.230.x.x",
        "assigned_ip" => "10.0.0.2",
        "secret_key" => "Go_Server_Generated_Key"
    ]);
} else {
    echo json_encode(["status" => "error", "message" => "بيانات الدخول خاطئة"]);
}
