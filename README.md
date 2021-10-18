# zvuv-emergency-land

## How to add emergency land to your crazyflie

1. Upload the nrf .bin firmware file in this repo to the crazyflie nrf
2. Add  `emergency_land.c` to `/src/deck/drivers/src/` stm firmware directory
3. Add `emergency_land.h` to `/src/deck/drivers/interface/` stm firmware  directory
4. Add `PROJ_OBJ += emergency_land.o` to your makefile of your stm firmware 
5. And on a different line add `CFLAGS += -DDECK_FORCE=emergency_land` to the same makefile
6. Compile the stm firmware and upload the stm firmware to your crazyflie
7. Connect a cable according to the picture bellow to your crazyflie:

## How to test 
1. make sure to have [cflib installed](https://github.com/bitcraze/crazyflie-lib-python/blob/master/docs/installation/install.md)
2. run `python3 send_emergency_land.py <your_crazyflie_radio_uri>`

## How to develop
Add your emergency land code in this line [here](https://github.com/M-R-VulcaN/zvuv-emergency-land/blob/30e61b90e58d7636af3be6a932981955d58d3d73/emergency_land.c#L48)
