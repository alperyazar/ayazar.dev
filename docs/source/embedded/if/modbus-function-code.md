# Modbus Function Codes

Bu yazıda, Modbus standartında belirtilen **Function Code** lara bakacağız.
Serideki diğer yazılarda Modbus ve Modbus RTU'yu konuştuk:

- [](modbus.md)
- [](modbus-rtu.md)

---

`1-127` arası function code'ların geçerli olduğundan bahsetmiştik. Bir
hatırlayalım:

```{figure} assets/modbus-figure-10.jpg
:align: center

Function code'ların bir kısmı rezerve, bir kısmına da önden anlamlar
yüklenmiştir. Görsel alıntıdır. `[1]`
```

Bu aralıktaki kodların bir kısmı Modbus tarafından PUBLIC olarak işaretlenmiş ve
genel amaçlıdır. Bir kısmı ise User Defined olarak bırakılmıştır.

```{figure} assets/modbus-function-codes-tablo.jpg
:align: center

YAZ,XXX Görsel alıntıdır. `[1]`
```

[^1f]: <https://modbus.org/docs/Modbus_Application_Protocol_V1_1b3.pdf>
[^2f]: <https://www.modbus.org/docs/Modbus_over_serial_line_V1_02.pdf>