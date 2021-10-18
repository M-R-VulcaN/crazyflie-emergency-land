# zvuv-emergency-land

## How to add emergency land to your crazyflie

1. Upload the nrf [.bin firmware file](https://github.com/M-R-VulcaN/zvuv-emergency-land/blob/da50aae5750fa001568360d4338a2dd59cbd8c20/crazyflie2_nrf_emergency_land.bin) in this repo to the crazyflie nrf
2. Add  `emergency_land.c` to `/src/deck/drivers/src/` stm firmware directory
3. Add `emergency_land.h` to `/src/deck/drivers/interface/` stm firmware  directory
4. Add `PROJ_OBJ += emergency_land.o` to your makefile of your stm firmware 
5. And on a different line add `CFLAGS += -DDECK_FORCE=emergency_land` to the same makefile
6. Compile the stm firmware and upload the stm firmware to your crazyflie
7. Connect a cable according to the picture bellow to your crazyflie:

![2e610349-ad5a-4518-bc3a-d8b367f3c0c3 sketchpad](https://user-images.githubusercontent.com/32649570/137742891-7aff069d-f8cc-4a74-a0d0-b31d228c3c8d.png)

## How to test 
1. make sure to have [cflib installed](https://github.com/bitcraze/crazyflie-lib-python/blob/master/docs/installation/install.md)
2. run `python3 send_emergency_land.py <your_crazyflie_radio_uri>`

## How to develop
Replace the line [here](https://github.com/M-R-VulcaN/zvuv-emergency-land/blob/30e61b90e58d7636af3be6a932981955d58d3d73/emergency_land.c#L48) with your emergency land code
