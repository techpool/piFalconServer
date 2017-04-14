import falcon
from gpiozero import LED

class GPIO4Resource(object):
    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200  # This is the default status
        resp.body = ('\nTwo things awe me most, the starry sky '
                     'above me and the moral law within me.\n'
                     '\n'
                     '    ~ Immanuel Kant\n\n')
    
    def on_post(self, req, resp):
        """Handles POST Requests"""
        # based on the query parameter 'status' the GPIO pin is turned ON or OFF
        PIN4 = LED(4)
        ledStatus = req.get_param('status')
        if ledStatus == 'ON':
            print('The GPIO4 on pin 7 needs to be turned on')
            resp.status = falcon.HTTP_200
            PIN4.on()
        elif ledStatus == 'OFF':
            print('The GPIO4 on pin 7 needs to be turned off')
            resp.status = falcon.HTTP_200
            PIN4.off()
        else:
            print('Invalid operation')
            resp.status = falcon.HTTP_304
