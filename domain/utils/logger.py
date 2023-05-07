import logging

class Logger():
    '''Log controls to easily call log messages in any location.'''

    def __init__(self):

        self.logger = logging.basicConfig(
                format='%(name)s || %(asctime)s (%(levelname)s) || %(message)s',
                level=logging.NOTSET
                )

    def get_logger(self, step: str) -> logging:
        '''Get the logger to pass logging messages.
        
        Attributes:
            step (str): the name of the actual step of the data process.
            
        Return:
            The logger named by the step status.'''

        self.logger = logging.getLogger(step)

        return self.logger