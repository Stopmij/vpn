class LoadBalancer:
    def __init__(self, servers):
        # قائمة بالخوادم المتاحة لاستقبال الضغط
        self.servers = servers
        self.current_index = 0

    def get_server(self):
        if not self.servers:
            return None
        
        # اختيار الخادم الحالي بناءً على الدور
        server = self.servers[self.current_index]
        
        # الانتقال إلى الخادم التالي في الدورة
        self.current_index = (self.current_index + 1) % len(self.servers)
        return server

# --- تجربة كود توزيع الضغط ---

# لدينا 3 خوادم لتلقي الضغط
my_servers = ["Server_A", "Server_B", "Server_C"]
balancer = LoadBalancer(my_servers)

# محاكاة وصول 6 طلبات (ضغط) من المستخدمين في نفس الوقت
print("🚀 بدء توزيع ضغط الطلبات:")
for request_id in range(1, 7):
    assigned_server = balancer.get_server()
    print(\u200f`الطلب رقم {request_id} تم توجيهه إلى: {assigned_server}`)
  
