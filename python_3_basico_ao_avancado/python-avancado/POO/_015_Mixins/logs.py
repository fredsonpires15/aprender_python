
# Abstração 

from pathlib import Path

LOG_FILE = Path(__file__).parent / 'log.txt'

class Log:
    def _log(self, msg):
        raise NotImplementedError('Implemente o método _log')
    
    def log_error(self,msg):
        return self._log(f'Error: {msg}')
    
    def log_success(self,msg):
        return self._log(f'Success: {msg}')

class LogFileMixin(Log):
    def _log(self,msg):
        msg_formatada = f'{msg} - {self.__class__.__name__}' 
        print('Arquivo salvo em "log.txt". . .')
        with open(LOG_FILE, 'a') as arquivo:
            arquivo.write(msg_formatada)
            arquivo.write('\n')


class LogPrintMixin(Log):
    def _log(self,msg):
        print(f'{msg} - {self.__class__.__name__}')



if __name__ == '__main__':
    l1 = LogFileMixin()
    l1.log_error('outra Coisa')
    l1.log_success('Que bom!!')

    l2 = LogPrintMixin()
    l2.log_error('outra Coisa')
    l2.log_success('Que bom!!')
    
    #l1.log_error('Qualquer coisa')