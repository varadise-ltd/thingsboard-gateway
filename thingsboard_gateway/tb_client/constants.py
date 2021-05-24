#      Copyright 2021. ThingsBoard
#  #
#      Licensed under the Apache License, Version 2.0 (the "License");
#      you may not use this file except in compliance with the License.
#      You may obtain a copy of the License at
#  #
#          http://www.apache.org/licenses/LICENSE-2.0
#  #
#      Unless required by applicable law or agreed to in writing, software
#      distributed under the License is distributed on an "AS IS" BASIS,
#      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#      See the License for the specific language governing permissions and
#      limitations under the License.

from enum import Enum


class MqttScheme(Enum):
    PROTOBUF = 1
    JSON = 2


class MqttPayloadTopics:
    REQUEST = ""
    RESPONSE = ""
    RPC = ""
    CONNECT = ""
    DISCONNECT = ""
    TELEMETRY = ""
    ATTRIBUTES = ""
    CLAIM = ""
    ACTION = ""

class MqttProtoPayloadTopics(MqttPayloadTopics):
    REQUEST = "/req"
    RESPONSE = "/rsp"
    CONNECT = "/con"
    DISCONNECT = "/dis"
    ATTRIBUTES = "/atr"
    TELEMETRY = "/tel"
    RPC = "/rpc"
    CLAIM = "/clm"
    ACTION = "/act"
    GATEWAY_MAIN_TOPIC = "v2/g"


class MqttJsonPayloadTopics(MqttPayloadTopics):
    REQUEST = "/request"
    RESPONSE = "/response"
    CONNECT = "/connnect"
    DISCONNECT = "/disconnect"
    ATTRIBUTES = "/attributes"
    TELEMETRY = "/telemetry"
    RPC = "/rpc"
    CLAIM = "/claim"
    ACTION = "/action"
    GATEWAY_MAIN_TOPIC = "v1/gateway"


MqttPayloadTopics = {
    MqttScheme.PROTOBUF: MqttProtoPayloadTopics,
    MqttScheme.JSON: MqttJsonPayloadTopics
    }


class MqttTopics:
    PAYLOAD = "/payload"
    ATTRIBUTES_RESPONSE = ""
    ATTRIBUTES_REQUEST = ""
    GATEWAY_CONNECT_TOPIC = ""
    GATEWAY_DISCONNECT_TOPIC = ""
    GATEWAY_ATTRIBUTES_TOPIC = ""
    GATEWAY_TELEMETRY_TOPIC = ""
    GATEWAY_RPC_TOPIC = ""
    GATEWAY_DEVICE_ACTION_TOPIC = ""
    GATEWAY_ATTRIBUTES_REQUEST_TOPIC = ""
    GATEWAY_ATTRIBUTES_RESPONSE_TOPIC = ""

    def __init__(self, mqtt_scheme: MqttScheme):
        payload_topics = MqttPayloadTopics[mqtt_scheme]
        self.ATTRIBUTES_RESPONSE = payload_topics.ATTRIBUTES + payload_topics.RESPONSE
        self.ATTRIBUTES_REQUEST = payload_topics.ATTRIBUTES + payload_topics.REQUEST
        self.GATEWAY_CONNECT_TOPIC = payload_topics.GATEWAY_MAIN_TOPIC + payload_topics.CONNECT
        self.GATEWAY_DISCONNECT_TOPIC = payload_topics.GATEWAY_MAIN_TOPIC + payload_topics.DISCONNECT
        self.GATEWAY_ATTRIBUTES_TOPIC = payload_topics.GATEWAY_MAIN_TOPIC + payload_topics.ATTRIBUTES
        self.GATEWAY_TELEMETRY_TOPIC = payload_topics.GATEWAY_MAIN_TOPIC + payload_topics.TELEMETRY
        self.GATEWAY_RPC_TOPIC = payload_topics.GATEWAY_MAIN_TOPIC + payload_topics.RPC
        self.GATEWAY_DEVICE_ACTION_TOPIC = payload_topics.GATEWAY_MAIN_TOPIC + payload_topics.ACTION
        self.GATEWAY_ATTRIBUTES_REQUEST_TOPIC = payload_topics.GATEWAY_MAIN_TOPIC + self.ATTRIBUTES_REQUEST
        self.GATEWAY_ATTRIBUTES_RESPONSE_TOPIC = payload_topics.GATEWAY_MAIN_TOPIC + self.ATTRIBUTES_RESPONSE
