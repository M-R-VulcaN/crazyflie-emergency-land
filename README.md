# Crazyflie Emergency Land

## How to add emergency land to your crazyflie

1. Upload the nrf [.bin firmware file](https://github.com/M-R-VulcaN/crazyflie-emergency-land/blob/da50aae5750fa001568360d4338a2dd59cbd8c20/crazyflie2_nrf_emergency_land.bin) in this repo to the crazyflie nrf. The source code for the binary file could be found [here](https://github.com/M-R-VulcaN/crazyflie2-nrf-firmware-emergency-land)
2. Add  `emergency_land.c` to `/src/deck/drivers/src/` stm firmware directory
3. Add `emergency_land.h` to `/src/deck/drivers/interface/` stm firmware  directory
4. Add `PROJ_OBJ += emergency_land.o` to your makefile of your stm firmware 
5. And on a different line add `CFLAGS += -DDECK_FORCE=emergency_land` to the same makefile
6. Compile the stm firmware and upload the stm firmware to your crazyflie
7. Connect a cable according to the picture bellow to your crazyflie:

IMPORTANT: Make sure to add the 5kΩ resistor between the ground and the two cables, without the resistor the GND could damage the drone.

![cf2_with_wires](https://user-images.githubusercontent.com/32649570/145978360-d20fcdbf-cb90-455e-9c46-0f600d5bd5dc.png)

Please note: In the image above the WKUP pin and the N_IO_1 pin are swapped for some reason, the lines I drew are the correct way for connecting the cables to the drone however. 


## How to test 
1. make sure to have [cflib installed](https://github.com/bitcraze/crazyflie-lib-python/blob/master/docs/installation/install.md)
2. run `python3 send_emergency_land.py <your_crazyflie_radio_uri>`

## How to develop
Replace the line [here](https://github.com/M-R-VulcaN/crazyflie-emergency-land/blob/30e61b90e58d7636af3be6a932981955d58d3d73/emergency_land.c#L48) with your emergency land code

## Additional material

* The repo which I used to develop the firmware code could be found [here](https://github.com/M-R-VulcaN/crazyflie-firmware-emergency-land/)
  * Also is useful the [pull request](https://github.com/M-R-VulcaN/crazyflie2-nrf-firmware-emergency-land/pull/1/files) in which all the changes I've made for the emergency land stm firmware code
* The source code for the nrf firmware could be found [here](https://github.com/M-R-VulcaN/crazyflie2-nrf-firmware-emergency-land) 
  *  Also is useful the [pull request](https://github.com/M-R-VulcaN/crazyflie2-nrf-firmware-emergency-land/pull/1/files) in which all the changes I've made for the emergency land nrf firmware code
