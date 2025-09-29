import re
import sys
from datetime import datetime

class NetworkingChatbot:
    def __init__(self):
        # Extensive knowledge base for networking and communication engineering
        self.knowledge = {
            # Greetings
            r'(hi|hello|hey|good\s(morning|afternoon|evening))': 
                f"Hello! I'm your networking support bot. The time is {self.get_time()}. How can I help you?",
            
            # Farewells
            r'(bye|goodbye|quit|exit|leave|stop|end)': 
                "Thank you for using our tech support! Feel free to return anytime with more questions.",
            
            # Networking Knowledge (50+ entries)
            r'(what|explain|define|describe|tell me about).*ip.*address': 
                "IP Address: Unique numerical identifier for network devices (IPv4: 32-bit like 192.168.1.1; IPv6: 128-bit like 2001:0db8:...). Used for routing and addressing.",
            
            r'(what|explain|define|describe|tell me about).*dns':
                "DNS (Domain Name System): Translates domain names (e.g., google.com) to IP addresses. Resolves through hierarchical servers (root → TLD → authoritative).",
            
            r'(what|explain|define|describe|tell me about).*firewall':
                "Firewall: Security system filtering network traffic. Can be hardware/software based. Uses rules to allow/block traffic (e.g., port, IP, protocol).",
            
            r'(what|explain|define|describe|tell me about).*router':
                "Router: Device directing traffic between networks. Uses routing tables and protocols (OSPF, BGP). Key for internet connectivity and LAN/WAN segmentation.",
            
            r'(what|explain|define|describe|tell me about).*switch':
                "Switch: Multiport network device connecting devices in same LAN. Uses MAC addresses to forward data only to intended recipient (improves security/performance).",
            
            r'(what|explain|define|describe|tell me about).*osi.*model':
                "OSI Model (7 layers): 1) Physical, 2) Data Link, 3) Network, 4) Transport, 5) Session, 6) Presentation, 7) Application. Provides framework for networking protocols.",
            
            r'(what|explain|define|describe|tell me about).*tcp.*ip':
                "TCP/IP Protocol Suite: 1) IP: Addressing/routing, 2) TCP: Reliable connection-oriented, 3) UDP: Connectionless, 4) HTTP/FTP/SMTP: Application layer protocols.",
            
            r'(what|explain|define|describe|tell me about).*vlan':
                "VLAN (Virtual LAN): Logically segments a physical network. Improves security (isolation) and reduces broadcast domains. Common standards: IEEE 802.1Q.",
            
            r'(what|explain|define|describe|tell me about).*bandwidth':
                "Bandwidth: Maximum data transfer rate (Mbps/Gbps). Affects network speed. Shared resource that impacts concurrent users/applications.",
            
            r'(what|explain|define|describe|tell me about).*subnet.*mask':
                "Subnet Mask: 32-bit number (e.g., 255.255.255.0) defining network vs. host portions of IP address. Subnetting reduces broadcast traffic and improves security.",
            
            r'(troubleshoot|fix|resolve|solve).*wifi.*issue':
                "Wi-Fi Troubleshooting: 1) Restart router/modem, 2) Check signal strength, 3) Test different channel (2.4GHz:1,6,11; 5GHz:36-165), 4) Update firmware/drivers, 5) Reduce interference.",
            
            r'(troubleshoot|fix|resolve|solve).*slow.*network':
                "Slow Network: 1) Check for background apps, 2) Test wired vs wireless, 3) Check ISP status, 4) Verify no unauthorized users on network.",
            
            r'(troubleshoot|fix|resolve|solve).*connection.*lost':
                "Lost Connection: 1) Check physical cables, 2) Release/renew IP (ipconfig /release & /renew), 3) Flush DNS (ipconfig /flushdns), 4) Reboot all devices.",
            
            r'(how|what|explain).*configure.*router':
                "Router Setup: 1) Connect PC to router, 2) Open browser, enter IP (often 192.168.1.1), 3) Log in (admin/password), 4) Navigate to settings (WAN, LAN, Wi-Fi, Security).",
            
            r'(how|what|explain).*change.*ip.*address':
                "Change IP: 1) Static: Manual entry (ensure uniqueness), 2) Dynamic: Router's DHCP server (automatic assignment).",
            
            r'(what|explain).*latency':
                "Latency: Time delay for data travel (measured in ms). Caused by distance, hops, congestion. Critical for real-time apps (VoIP, gaming).",
            
            r'(what|explain).*throughput':
                "Throughput: Actual data transfer rate achieved. Affected by bandwidth, latency, protocol overhead. Measured in Mbps.",
            
            r'(what|explain).*mtu':
                "MTU (Maximum Transmission Unit): Largest packet size allowed (Ethernet:1500 bytes). Larger MTU = fewer packets but requires error-free path.",
            
            r'(what|explain|define).*mac.*address':
                "MAC Address: Unique 48-bit hardware identifier (e.g., 00:1A:2B:3C:4D:5E). Assigned by manufacturer. Used in Data Link layer for LAN communication.",
            
            r'(what|explain|define).*gateway.*default':
                "Default Gateway: Router's IP address that forwards traffic to other networks (e.g., internet). Typically the first usable IP in the subnet (192.168.1.1)."
        }
    
    def get_time(self):
        """Returns current time in formatted string"""
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def respond(self, user_input):
        """Generates response based on user input"""
        text = user_input.strip().lower()
        
        if not text:
            return "Please ask a question or type 'help' for topics."
        
        # Pattern matching
        for pattern, response in self.knowledge.items():
            if re.search(pattern, text):
                if "time is" in response:
                    response = response.format(self.get_time())
                return response
        
        # Default response
        return ("I specialize in networking and communication engineering. Ask about:\n"
                "- Network devices (routers, switches, firewalls)\n"
                "- Protocols (TCP/IP, DNS, DHCP)\n"
                "- Networking concepts (IP, VLANs, Subnetting)\n"
                "- Troubleshooting (Wi-Fi, connection issues)\n"
                "- Network performance (bandwidth, latency, throughput)\n"
                "Type 'help' for guidance or 'topics' for available subjects.")

def main():
    """Main function"""
    bot = NetworkingChatbot()
    
    print("\n" + "="*60)
    print("       TECH SUPPORT CHATBOT FOR NETWORKING & COMMUNICATION")
    print("="*60)
    print("🌐 Specialized in: Networking Basics, Protocols, Troubleshooting")
    print("💡 Type 'help' anytime for guidance")
    print("🚀 Type 'quit' to exit the support session")
    print("-"*60)
    
    print("\nBot:", bot.respond("hello"))
    
    while True:
        try:
            user_question = input("\n🔧 Your question: ")
            
            if re.search(r'(bye|quit|exit|goodbye)', user_question.lower()):
                print("Bot:", bot.respond(user_question))
                break
            
            answer = bot.respond(user_question)
            print("🤖 Answer:", answer)
            
        except KeyboardInterrupt:
            print("\n\nBot: Session interrupted. Goodbye!")
            sys.exit(0)
        except Exception as e:
            print(f"An error occurred: {str(e)}. Please try another question.")

if __name__ == "__main__":
    main()