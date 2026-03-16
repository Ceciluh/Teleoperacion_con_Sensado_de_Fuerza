#include <WiFi.h>
#include <WiFiUdp.h>
#include <HX711.h>

const char* SSID      = "alfresi";
const char* PASS      = "mora2025";
const char* SLAVE_IP  = "192.168.1.226";
const int   UDP_PORT  = 9003;

const int DT_PIN  = 15;
const int SCK_PIN = 2;

long offset = -351650;
float factor = 0.009;   

const int HZ = 50;

HX711 scale;
WiFiUDP udp;
char buf[64];

void setup() {

    Serial.begin(115200);

    scale.begin(DT_PIN, SCK_PIN);

    WiFi.begin(SSID, PASS);
    Serial.print("WiFi");
    while (WiFi.status() != WL_CONNECTED) {
        delay(250);
        Serial.print(".");
    }

    Serial.print(" OK  IP=");
    Serial.println(WiFi.localIP());

    udp.begin(UDP_PORT);
}

void loop() {

    static unsigned long t_prev = 0;
    unsigned long t_now = millis();
    if (t_now - t_prev < (1000 / HZ)) return;
    t_prev = t_now;

    float force = 0.0;

    if(scale.is_ready()){

        long raw = scale.read();

        force = (raw - offset) * factor;

        if(force < 0) force = 0;
    }

    snprintf(buf, sizeof(buf), "{\"F\":%.4f}", force);

    udp.beginPacket(SLAVE_IP, UDP_PORT);
    udp.write((uint8_t*)buf, strlen(buf));
    udp.endPacket();
}