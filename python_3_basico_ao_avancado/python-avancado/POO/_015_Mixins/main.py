#from logs import LogFileMixin, LogPrintMixin

from eletronico import Smartphone


galaxy_s = Smartphone('Galaxy s')
iphone = Smartphone('iphone')

galaxy_s.ligar()
iphone.desligar()


# l1 = LogFileMixin()
# l1.log_error('outra Coisa')
# l1.log_success('Que bom!!')

# l2 = LogPrintMixin()
# l2.log_error('outra Coisa')
# l2.log_success('Que bom!!')






