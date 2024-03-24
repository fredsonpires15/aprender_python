velocidade = 68 # velocidade atual do carro
local_carro = 99# local em o carro  está na estrada


RADAR_1 = 60 # velocidade máxima do radar 1
LOCAL_1 = 100 # local onde o radar 1 está
RADAR_RANGE = 1 # A distância onde o radar pega

vel_carra_pass_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado_radar_1 = carro_passou_radar_1 and vel_carra_pass_radar_1

if vel_carra_pass_radar_1:
    print('Velocidade do carro passou do radar 1')
if carro_passou_radar_1:
    print('Carro passou radar 1')
if carro_multado_radar_1:
    print('carro multado em radar 1')

