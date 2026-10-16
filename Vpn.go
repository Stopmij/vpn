package main
import (
    "fmt"
    "net"
)
func main() {
    // التسمع على منفذ UDP لاستقبال اتصالات الـ VPN
    listener, _ := net.ListenPacket("udp", ":51820")
    defer listener.Close()
    fmt.Println("خادم الـ VPN يعمل الآن على المنفذ 51820...")
    
    buffer := make([]byte, 1024)
    for {
        n, addr, _ := listener.ReadFrom(buffer)
        // هنا يتم معالجة البيانات، فك التشفير، وإعادة التوجيه
        go func(p []byte, a net.Addr) {
            fmt.Printf("تم استقبال بيانات مشفرة من: %s\n", a.String())
        }(buffer[:n], addr)
    }
}
