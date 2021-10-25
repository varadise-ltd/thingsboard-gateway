#     Copyright 2021. ThingsBoard
#
#     Licensed under the Apache License, Version 2.0 (the "License");
#     you may not use this file except in compliance with the License.
#     You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#     Unless required by applicable law or agreed to in writing, software
#     distributed under the License is distributed on an "AS IS" BASIS,
#     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#     See the License for the specific language governing permissions and
#     limitations under the License.

from thingsboard_gateway.gateway.tb_gateway_service import *


class TBGatewayServiceMicroservice(TBGatewayService):
    def __init__(self, config, config_dir):
        super().__init__(config, config_dir)

    def _handle_rpc_for_connector(self, device, content):
        # connector_name = self.get_devices()[device].get("connector")
        # if connector_name is not None:
        #     connector_name.server_side_rpc_handler(content)
        # else:
        #     log.error("Received RPC request but connector for the device %s not found. Request data: \n %s",
        #               content["device"],
        #               dumps(content))
        pass

    def _load_connectors(self):
        # self.connectors_configs = {}
        # if self._config.get("connectors"):
        #     for connector in self._config['connectors']:
        #         try:
        #             connector_class = TBModuleLoader.import_module(connector["type"],
        #                                                            self.DEFAULT_CONNECTORS.get(connector["type"],
        #                                                                                         connector.get("class")))
        #             self._implemented_connectors[connector["type"]] = connector_class
        #             config_file_path = self._config_dir + connector['configuration']
        #             with open(config_file_path, 'r', encoding="UTF-8") as conf_file:
        #                 connector_conf = load(conf_file)
        #                 if not self.connectors_configs.get(connector['type']):
        #                     self.connectors_configs[connector['type']] = []
        #                 connector_conf["name"] = connector["name"]
        #                 self.connectors_configs[connector['type']].append({"name": connector["name"],
        #                                                                    "config": {connector[
        #                                                                                   'configuration']: connector_conf},
        #                                                                    "config_updated": stat(config_file_path),
        #                                                                    "config_file_path": config_file_path})
        #         except Exception as e:
        #             log.error("Error on loading connector:")
        #             log.exception(e)
        # else:
        #     log.error("Connectors - not found! Check your configuration!")
        #     self._init_remote_configuration(force=True)
        #     log.info("Remote configuration is enabled forcibly!")
        pass

    def _connect_with_connectors(self):
        # for connector_type in self.connectors_configs:
        #     for connector_config in self.connectors_configs[connector_type]:
        #         for config in connector_config["config"]:
        #             connector = None
        #             try:
        #                 if connector_config["config"][config] is not None:
        #                     if self._implemented_connectors[connector_type]:
        #                         connector = self._implemented_connectors[connector_type](self,
        #                                                                                  connector_config["config"][
        #                                                                                      config],
        #                                                                                  connector_type)
        #                         connector.setName(connector_config["name"])
        #                         self.available_connectors[connector.get_name()] = connector
        #                         connector.open()
        #                     else:
        #                         log.warning("Connector implementation not found for %s", connector_config["name"])
        #                 else:
        #                     log.info("Config not found for %s", connector_type)
        #             except Exception as e:
        #                 log.exception(e)
        #                 if connector is not None:
        #                     connector.close()
        pass

    def _form_statistics(self):
        # summary_messages = {"eventsProduced": 0, "eventsSent": 0}
        # telemetry = {}
        # for connector in self.available_connectors:
        #     connector_camel_case = connector.lower().replace(' ', '')
        #     telemetry[(connector_camel_case + ' EventsProduced').replace(' ', '')] = \
        #         self.available_connectors[connector].statistics['MessagesReceived']
        #     self.available_connectors[connector].statistics['MessagesReceived'] = 0
        #     telemetry[(connector_camel_case + ' EventsSent').replace(' ', '')] = \
        #         self.available_connectors[connector].statistics['MessagesSent']
        #     self.available_connectors[connector].statistics['MessagesSent'] = 0
        #     summary_messages['eventsProduced'] += telemetry[
        #         str(connector_camel_case + ' EventsProduced').replace(' ', '')]
        #     summary_messages['eventsSent'] += telemetry[
        #         str(connector_camel_case + ' EventsSent').replace(' ', '')]
        #     summary_messages.update(**telemetry)
        # return summary_messages
        pass