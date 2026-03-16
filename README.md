# Cómo correr con los xArm6 físicos

- Ambas PCs en la misma red
- xArm maestro conectado a PC maestra (192.168.1.195)
- xArm esclavo conectado a PC esclava (192.168.1.226)
- Robots encendidos
- 
## PC Maestra (192.168.1.XXX)

Terminal 1, lanzar MoveIt Servo:
```bash
ros2 launch xarm_moveit_servo xarm_moveit_servo_realmove.launch.py robot_ip:=192.168.1.195 dof:=6
```

Terminal 2, correr maestro:
```bash
ros2 run arm_bridge master --slave-ip 192.168.1.XXX
```

## PC Esclava (192.168.1.XXX)

```bash
ros2 run arm_bridge slave --master-ip 192.168.1.XXX
```

## Controles

| Tecla | Acción |
|-------|--------|
| W / X | +y / -y |
| A / D | -x / +x |
| P | salir y guardar datos |
