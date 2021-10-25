
from os import path
from yaml import safe_load
import logging
import logging.config
import logging.handlers


class TBGatewayServiceResolver():
    def __init__(self, config_file=None):
        config_dir = path.dirname(path.abspath(config_file)) + path.sep
        try:
            logging.config.fileConfig(config_dir + "logs.conf", disable_existing_loggers=False)
        except Exception as e:
            print(e)
        if config_file is None:
            config_file = path.dirname(path.dirname(path.abspath(__file__))) + '/config/tb_gateway.yaml'.replace('/',
                                                                                                                 path.sep)
        with open(config_file) as general_config:
            config = safe_load(general_config)
        log = logging.getLogger('service')

        mode = config["service"]["mode"] if config.get("service") is not None and config["service"].get("mode") is not None else "monolith"

        log.info("Loading gateway in %s mode...", mode)

        if mode == "microservice":
            try:
                from thingsboard_gateway.gateway.tb_gateway_service_microservice import TBGatewayServiceMicroservice
                self.service = TBGatewayServiceMicroservice(config, config_dir)
            except Exception as e:
                log.exception(e)
        else:
            try:
                from thingsboard_gateway.gateway.tb_gateway_service_monolith import TBGatewayServiceMonolith
                self.service = TBGatewayServiceMonolith(config, config_dir)
            except Exception as e:
                log.exception(e)

