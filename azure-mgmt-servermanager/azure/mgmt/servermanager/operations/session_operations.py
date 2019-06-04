# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

import uuid
from msrest.pipeline import ClientRawResponse
from msrest.polling import LROPoller, NoPolling
from msrestazure.polling.arm_polling import ARMPolling

from .. import models


class SessionOperations(object):
    """SessionOperations operations.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    :ivar api_version: Client API Version. Constant value: "2016-07-01-preview".
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self.api_version = "2016-07-01-preview"

        self.config = config


    def _create_initial(
            self, resource_group_name, node_name, session, user_name=None, password=None, retention_period=None, credential_data_format=None, encryption_certificate_thumbprint=None, custom_headers=None, raw=False, **operation_config):
        session_parameters = models.SessionParameters(user_name=user_name, password=password, retention_period=retention_period, credential_data_format=credential_data_format, encryption_certificate_thumbprint=encryption_certificate_thumbprint)

        # Construct URL
        url = self.create.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', min_length=3, pattern=r'[a-zA-Z0-9]+'),
            'nodeName': self._serialize.url("node_name", node_name, 'str', max_length=256, min_length=1, pattern=r'^[a-zA-Z0-9][a-zA-Z0-9_.-]*$'),
            'session': self._serialize.url("session", session, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct body
        body_content = self._serialize.body(session_parameters, 'SessionParameters')

        # Construct and send request
        request = self._client.put(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200, 201, 202]:
            raise models.ErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('SessionResource', response)
        if response.status_code == 201:
            deserialized = self._deserialize('SessionResource', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized

    def create(
            self, resource_group_name, node_name, session, user_name=None, password=None, retention_period=None, credential_data_format=None, encryption_certificate_thumbprint=None, custom_headers=None, raw=False, polling=True, **operation_config):
        """Creates a session for a node.

        :param resource_group_name: The resource group name uniquely
         identifies the resource group within the user subscriptionId.
        :type resource_group_name: str
        :param node_name: The node name (256 characters maximum).
        :type node_name: str
        :param session: The sessionId from the user.
        :type session: str
        :param user_name: Encrypted User name to be used to connect to node.
        :type user_name: str
        :param password: Encrypted Password associated with user name.
        :type password: str
        :param retention_period: Session retention period. Possible values
         include: 'Session', 'Persistent'
        :type retention_period: str or
         ~azure.mgmt.servermanager.models.RetentionPeriod
        :param credential_data_format: Credential data format. Possible values
         include: 'RsaEncrypted'
        :type credential_data_format: str or
         ~azure.mgmt.servermanager.models.CredentialDataFormat
        :param encryption_certificate_thumbprint: Encryption certificate
         thumbprint.
        :type encryption_certificate_thumbprint: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: The poller return type is ClientRawResponse, the
         direct response alongside the deserialized response
        :param polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :return: An instance of LROPoller that returns SessionResource or
         ClientRawResponse<SessionResource> if raw==True
        :rtype:
         ~msrestazure.azure_operation.AzureOperationPoller[~azure.mgmt.servermanager.models.SessionResource]
         or
         ~msrestazure.azure_operation.AzureOperationPoller[~msrest.pipeline.ClientRawResponse[~azure.mgmt.servermanager.models.SessionResource]]
        :raises:
         :class:`ErrorException<azure.mgmt.servermanager.models.ErrorException>`
        """
        raw_result = self._create_initial(
            resource_group_name=resource_group_name,
            node_name=node_name,
            session=session,
            user_name=user_name,
            password=password,
            retention_period=retention_period,
            credential_data_format=credential_data_format,
            encryption_certificate_thumbprint=encryption_certificate_thumbprint,
            custom_headers=custom_headers,
            raw=True,
            **operation_config
        )

        def get_long_running_output(response):
            deserialized = self._deserialize('SessionResource', response)

            if raw:
                client_raw_response = ClientRawResponse(deserialized, response)
                return client_raw_response

            return deserialized

        lro_delay = operation_config.get(
            'long_running_operation_timeout',
            self.config.long_running_operation_timeout)
        if polling is True: polling_method = ARMPolling(lro_delay, **operation_config)
        elif polling is False: polling_method = NoPolling()
        else: polling_method = polling
        return LROPoller(self._client, raw_result, get_long_running_output, polling_method)
    create.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServerManagement/nodes/{nodeName}/sessions/{session}'}

    def delete(
            self, resource_group_name, node_name, session, custom_headers=None, raw=False, **operation_config):
        """Deletes a session for a node.

        :param resource_group_name: The resource group name uniquely
         identifies the resource group within the user subscriptionId.
        :type resource_group_name: str
        :param node_name: The node name (256 characters maximum).
        :type node_name: str
        :param session: The sessionId from the user.
        :type session: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorException<azure.mgmt.servermanager.models.ErrorException>`
        """
        # Construct URL
        url = self.delete.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', min_length=3, pattern=r'[a-zA-Z0-9]+'),
            'nodeName': self._serialize.url("node_name", node_name, 'str', max_length=256, min_length=1, pattern=r'^[a-zA-Z0-9][a-zA-Z0-9_.-]*$'),
            'session': self._serialize.url("session", session, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.delete(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200, 204]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    delete.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServerManagement/nodes/{nodeName}/sessions/{session}'}

    def get(
            self, resource_group_name, node_name, session, custom_headers=None, raw=False, **operation_config):
        """Gets a session for a node.

        :param resource_group_name: The resource group name uniquely
         identifies the resource group within the user subscriptionId.
        :type resource_group_name: str
        :param node_name: The node name (256 characters maximum).
        :type node_name: str
        :param session: The sessionId from the user.
        :type session: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: SessionResource or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.servermanager.models.SessionResource or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorException<azure.mgmt.servermanager.models.ErrorException>`
        """
        # Construct URL
        url = self.get.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', min_length=3, pattern=r'[a-zA-Z0-9]+'),
            'nodeName': self._serialize.url("node_name", node_name, 'str', max_length=256, min_length=1, pattern=r'^[a-zA-Z0-9][a-zA-Z0-9_.-]*$'),
            'session': self._serialize.url("session", session, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('SessionResource', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServerManagement/nodes/{nodeName}/sessions/{session}'}