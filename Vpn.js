async function connectVPN() {
    const credentials = { username: 'admin', password: 'secret123' };

    // 1. الاتصال بـ PHP للتحقق من الحساب والحصول على الإعدادات
    let response = await fetch('https://my-vpn-panel.com', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(credentials)
    });

    let config = await response.json();

    if (config.status === "success") {
        console.log(`تم التحقق بنجاح! جاري الاتصال بالخادم: ${config.vpn_gateway}`);
        // 2. هنا يتم تمرير إعدادات JSON إلى الجزء المسؤول عن تشغيل نفق الاتصال
        startTunnel(config);
    } else {
        console.error("فشل الاتصال:", config.message);
    }
}
