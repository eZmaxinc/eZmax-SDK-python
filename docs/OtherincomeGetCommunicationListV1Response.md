# OtherincomeGetCommunicationListV1Response

Response for GET /1/object/otherincome/{pkiOtherincomeID}/getCommunicationList

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayloadGetList**](CommonResponseObjDebugPayloadGetList.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**OtherincomeGetCommunicationListV1ResponseMPayload**](OtherincomeGetCommunicationListV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.otherincome_get_communication_list_v1_response import OtherincomeGetCommunicationListV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of OtherincomeGetCommunicationListV1Response from a JSON string
otherincome_get_communication_list_v1_response_instance = OtherincomeGetCommunicationListV1Response.from_json(json)
# print the JSON string representation of the object
print OtherincomeGetCommunicationListV1Response.to_json()

# convert the object into a dict
otherincome_get_communication_list_v1_response_dict = otherincome_get_communication_list_v1_response_instance.to_dict()
# create an instance of OtherincomeGetCommunicationListV1Response from a dict
otherincome_get_communication_list_v1_response_form_dict = otherincome_get_communication_list_v1_response.from_dict(otherincome_get_communication_list_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


