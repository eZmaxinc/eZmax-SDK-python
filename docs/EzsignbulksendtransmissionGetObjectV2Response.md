# EzsignbulksendtransmissionGetObjectV2Response

Response for GET /2/object/ezsignbulksendtransmission/{pkiEzsignbulksendtransmissionID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsignbulksendtransmissionGetObjectV2ResponseMPayload**](EzsignbulksendtransmissionGetObjectV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignbulksendtransmission_get_object_v2_response import EzsignbulksendtransmissionGetObjectV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignbulksendtransmissionGetObjectV2Response from a JSON string
ezsignbulksendtransmission_get_object_v2_response_instance = EzsignbulksendtransmissionGetObjectV2Response.from_json(json)
# print the JSON string representation of the object
print(EzsignbulksendtransmissionGetObjectV2Response.to_json())

# convert the object into a dict
ezsignbulksendtransmission_get_object_v2_response_dict = ezsignbulksendtransmission_get_object_v2_response_instance.to_dict()
# create an instance of EzsignbulksendtransmissionGetObjectV2Response from a dict
ezsignbulksendtransmission_get_object_v2_response_from_dict = EzsignbulksendtransmissionGetObjectV2Response.from_dict(ezsignbulksendtransmission_get_object_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


